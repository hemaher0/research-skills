"""Contract tests for the stable repository-local GPU entrypoint."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins/research-skills/skills/run-gpu/scripts"
INSTALLER = SCRIPTS / "install-gpu-exec"


class GPUExecTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="gpu-launcher-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.main = self.root / "main checkout"
        self.main.mkdir()
        self.git("init", "-b", "main", cwd=self.main)
        self.git("config", "user.email", "test@example.com", cwd=self.main)
        self.git("config", "user.name", "GPU Test", cwd=self.main)
        (self.main / "pyproject.toml").write_text(
            '[project]\nname = "gpu-fixture"\nversion = "0.1.0"\n'
            'requires-python = ">=3.9"\ndependencies = []\n'
            "[tool.uv]\npackage = false\n"
        )
        (self.main / "uv.lock").write_text("fixture-lock\n")
        (self.main / "src").mkdir()
        self.git("add", "pyproject.toml", "uv.lock", cwd=self.main)
        self.git("commit", "-m", "fixture", cwd=self.main)

        shared_python = self.main / ".venv/bin/python"
        shared_python.parent.mkdir(parents=True)
        shared_python.symlink_to(sys.executable)

        result = subprocess.run(
            [str(INSTALLER), "--repository", str(self.main)],
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.wrapper = self.main / ".agents/bin/gpu-exec"
        self.assertEqual(result.stdout.strip(), str(self.wrapper))

        self.bin = self.root / "bin"
        self.bin.mkdir()
        for name in ("bash", "cmp", "dirname", "git", "realpath"):
            target = shutil.which(name)
            if target:
                (self.bin / name).symlink_to(target)

        self.recorder = """#!%s
import json, os, sys
if os.path.basename(sys.argv[0]) == "uv" and sys.argv[1:] == ["lock", "--check"]:
    sys.exit(0)
print(json.dumps({"tool": os.path.basename(sys.argv[0]), "args": sys.argv[1:],
                  "cwd": os.getcwd(), "env": {key: os.environ.get(key) for key in
                  ("CUDA_VISIBLE_DEVICES", "VIRTUAL_ENV", "PYTHONPATH",
                   "CONDA_PREFIX", "CONDA_DEFAULT_ENV")}}))
sys.exit(int(os.environ.get("GPU_TEST_EXIT", "0")))
""" % sys.executable
        self.add_command("uv")
        self.add_command("nvidia-smi")
        self.env = {
            "PATH": str(self.bin),
            "CUDA_VISIBLE_DEVICES": "GPU-scheduler-assigned",
            "PYTHONPATH": "/site/custom-modules",
            "CONDA_PREFIX": "/ambient/conda",
            "CONDA_DEFAULT_ENV": "ambient",
        }

    @staticmethod
    def git(*args, cwd):
        result = subprocess.run(
            ["git", *args], cwd=cwd, capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            raise AssertionError(result.stderr)
        return result.stdout.strip()

    def add_command(self, name):
        path = self.bin / name
        path.write_text(self.recorder)
        path.chmod(0o755)

    def run_wrapper(self, *args, cwd=None):
        return subprocess.run(
            [str(self.wrapper), *args],
            cwd=cwd or self.main,
            env=self.env,
            capture_output=True,
            text=True,
            timeout=10,
        )

    def payload(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def add_worktree(self):
        worktree = self.root / "linked worktree"
        self.git("worktree", "add", "-b", "feature", str(worktree), cwd=self.main)
        return worktree

    def test_installer_keeps_one_stable_executable_path(self):
        original = self.wrapper.read_bytes()
        result = subprocess.run(
            [str(INSTALLER), "--repository", str(self.main)],
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(self.wrapper))
        self.assertEqual(self.wrapper.read_bytes(), original)
        self.assertTrue(os.access(self.wrapper, os.X_OK))

    def test_installer_does_not_follow_a_conflicting_symlink(self):
        outside = self.root / "outside-wrapper"
        outside.write_text("preserve me\n")
        self.wrapper.unlink()
        self.wrapper.symlink_to(outside)
        result = subprocess.run(
            [str(INSTALLER), "--repository", str(self.main)],
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 73, result.stderr)
        self.assertEqual(outside.read_text(), "preserve me\n")

    def test_main_checkout_uses_shared_environment_without_sync(self):
        data = self.payload(self.run_wrapper("python", "-c", "print('ok')"))
        self.assertEqual(data["cwd"], str(self.main))
        self.assertEqual(
            data["args"],
            ["run", "--active", "--no-sync", "python", "-c", "print('ok')"],
        )
        self.assertEqual(data["env"]["VIRTUAL_ENV"], str(self.main / ".venv"))
        self.assertEqual(
            data["env"]["PYTHONPATH"],
            f"{self.main / 'src'}:/site/custom-modules",
        )
        self.assertIsNone(data["env"]["CONDA_PREFIX"])
        self.assertIsNone(data["env"]["CONDA_DEFAULT_ENV"])

    def test_linked_worktree_uses_same_environment_and_its_own_source(self):
        worktree = self.add_worktree()
        (worktree / "src").mkdir()
        data = self.payload(
            self.run_wrapper("--workdir", str(worktree), "pytest", "-q")
        )
        self.assertEqual(data["cwd"], str(worktree))
        self.assertEqual(
            data["args"],
            ["run", "--active", "--no-sync", "python", "-m", "pytest", "-q"],
        )
        self.assertEqual(data["env"]["VIRTUAL_ENV"], str(self.main / ".venv"))
        self.assertEqual(
            data["env"]["PYTHONPATH"],
            f"{worktree / 'src'}:/site/custom-modules",
        )

    def test_unrelated_checkout_is_outside_approved_boundary(self):
        unrelated = self.root / "unrelated"
        unrelated.mkdir()
        self.git("init", "-b", "main", cwd=unrelated)
        result = self.run_wrapper("--workdir", str(unrelated), "python", "-V")
        self.assertEqual(result.returncode, 77, result.stderr)
        self.assertIn("not the main checkout", result.stderr)

    def test_worktree_with_different_lock_cannot_use_shared_environment(self):
        worktree = self.add_worktree()
        (worktree / "uv.lock").write_text("different-lock\n")
        result = self.run_wrapper("--workdir", str(worktree), "python", "-V")
        self.assertEqual(result.returncode, 78, result.stderr)
        self.assertIn("uv.lock differs", result.stderr)

    def test_devices_change_after_the_same_executable_prefix(self):
        for mask in ("1", "0,2", "GPU-a,MIG-b", ""):
            with self.subTest(mask=mask):
                data = self.payload(
                    self.run_wrapper("--devices", mask, "python", "-V")
                )
                self.assertEqual(data["env"]["CUDA_VISIBLE_DEVICES"], mask)

    def test_torchrun_and_probe_use_shared_environment(self):
        torchrun = self.payload(
            self.run_wrapper(
                "torchrun", "--standalone", "--nproc-per-node=2", "train.py"
            )
        )
        self.assertEqual(
            torchrun["args"],
            [
                "run",
                "--active",
                "--no-sync",
                "python",
                "-m",
                "torch.distributed.run",
                "--standalone",
                "--nproc-per-node=2",
                "train.py",
            ],
        )
        probe = self.payload(self.run_wrapper("probe"))
        self.assertEqual(
            probe["args"],
            [
                "run",
                "--active",
                "--no-sync",
                "python",
                str(self.main / ".agents/bin/gpu_probe.py"),
            ],
        )

    def test_inventory_preserves_allocation_and_does_not_require_uv(self):
        (self.bin / "uv").unlink()
        data = self.payload(
            self.run_wrapper("nvidia-smi", "--query-gpu=name", "--format=csv")
        )
        self.assertEqual(data["tool"], "nvidia-smi")
        self.assertEqual(data["args"], ["--query-gpu=name", "--format=csv"])
        self.assertEqual(
            data["env"]["CUDA_VISIBLE_DEVICES"], "GPU-scheduler-assigned"
        )

    def test_invalid_arguments_and_missing_environment_fail_before_execution(self):
        for args in (
            (),
            ("--workdir",),
            ("--devices",),
            ("--unknown",),
            ("bad-mode",),
            ("probe", "unexpected"),
        ):
            with self.subTest(args=args):
                result = self.run_wrapper(*args)
                self.assertEqual(result.returncode, 64, result.stderr)
                self.assertEqual(result.stdout, "")

        (self.main / ".venv/bin/python").unlink()
        result = self.run_wrapper("python", "-V")
        self.assertEqual(result.returncode, 69, result.stderr)
        self.assertIn("shared uv environment", result.stderr)


@unittest.skipUnless(shutil.which("uv"), "uv is required for the integration test")
class RealUVTests(unittest.TestCase):
    def test_linked_worktree_runs_from_main_checkout_environment(self):
        with tempfile.TemporaryDirectory(prefix="gpu-real-uv-") as directory:
            root = Path(directory)
            main = root / "main"
            main.mkdir()
            subprocess.run(["git", "init", "-b", "main"], cwd=main, check=True,
                           capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"],
                           cwd=main, check=True)
            subprocess.run(["git", "config", "user.name", "GPU Test"],
                           cwd=main, check=True)
            (main / "pyproject.toml").write_text(
                '[project]\nname = "gpu-real-fixture"\nversion = "0.1.0"\n'
                'requires-python = ">=3.9"\ndependencies = []\n'
                "[tool.uv]\npackage = false\n"
            )
            (main / "src").mkdir()
            env = dict(os.environ)
            for key in tuple(env):
                if key.startswith("UV_") or key in (
                    "VIRTUAL_ENV",
                    "CONDA_PREFIX",
                    "CONDA_DEFAULT_ENV",
                    "PYTHONPATH",
                ):
                    del env[key]
            env.update(
                UV_PYTHON=sys.executable,
                UV_CACHE_DIR=str(root / "cache"),
                UV_OFFLINE="1",
                UV_PYTHON_DOWNLOADS="never",
            )
            lock = subprocess.run(
                ["uv", "lock", "--offline"], cwd=main, env=env,
                capture_output=True, text=True, timeout=30
            )
            self.assertEqual(lock.returncode, 0, lock.stderr)
            sync = subprocess.run(
                ["uv", "sync", "--locked", "--offline"], cwd=main, env=env,
                capture_output=True, text=True, timeout=30
            )
            self.assertEqual(sync.returncode, 0, sync.stderr)
            subprocess.run(["git", "add", "pyproject.toml", "uv.lock"],
                           cwd=main, check=True)
            subprocess.run(["git", "commit", "-m", "fixture"], cwd=main,
                           check=True, capture_output=True)
            worktree = root / "worktree"
            subprocess.run(["git", "worktree", "add", "-b", "feature", str(worktree)],
                           cwd=main, check=True, capture_output=True)
            (worktree / "src").mkdir()
            install = subprocess.run(
                [str(INSTALLER), "--repository", str(main)],
                capture_output=True, text=True, timeout=10
            )
            self.assertEqual(install.returncode, 0, install.stderr)
            wrapper = main / ".agents/bin/gpu-exec"
            code = (
                "import json, os, sys; "
                "print(json.dumps({'prefix': sys.prefix, "
                "'venv': os.environ.get('VIRTUAL_ENV'), "
                "'path0': os.environ.get('PYTHONPATH', '').split(':')[0]}))"
            )
            result = subprocess.run(
                [str(wrapper), "--workdir", str(worktree), "python", "-c", code],
                cwd=root, env=env, capture_output=True, text=True, timeout=30
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual(data["prefix"], str(main / ".venv"))
            self.assertEqual(data["venv"], str(main / ".venv"))
            self.assertEqual(data["path0"], str(worktree / "src"))


if __name__ == "__main__":
    unittest.main()
