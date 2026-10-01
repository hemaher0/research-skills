---
name: run-gpu
description: Use when a Git repository with a shared uv environment requires NVIDIA GPU or CUDA diagnostics, torch.cuda tests, CUDA pytest cases, NCCL, nvidia-smi, or torchrun from its main checkout or linked worktrees.
---

# Run GPU

Run GPU commands through the repository's stable, protected entrypoint. The main
checkout owns one uv environment, and every linked worktree uses that same
environment while importing its own source first. Conda is not an execution or
fallback environment.

When project instructions configure work items, preserve the GPU request,
environment and code identity, observed result, and next action there. Use an
available document router for the update; if none is available, use project
instructions, the local `.docs-schema` when present, and ordinary file tools.
This trace does not create an experiment record or change the GPU execution
boundary below.

## Stable entrypoint and permission

Read the target repository's `AGENTS.md` and `AGENTS.local.md`. Use the local
file's execution environment for the current host to identify the main
checkout, Python environment type, GPU allocation, and stable wrapper path.
Verify the main checkout and worktree relationship with Git and confirm the
environment is the shared uv `.venv` required by this wrapper. A local setting
for another Python environment does not make this wrapper support it.

Verify the recorded wrapper path agrees with the main checkout. The expected
location is:

```text
<main-checkout>/.agents/bin/gpu-exec
```

Every GPU command must begin directly with that exact absolute path. Options and
subcommands may vary after it; the executable path remains the approval prefix.
Do not prepend `env`, variable assignments, `uv`, `bash`, `source`, `cd`, or
another shell launcher. When escalation is required, propose only this stable
wrapper path as the reusable `prefix_rule`. Reuse an existing exact-path approval.

The wrapper binds its authority to the containing main checkout. It accepts only
that checkout and worktrees sharing its Git common directory, and always selects
the main checkout's `.venv`. A repository-specific approval therefore does not
authorize an unrelated checkout.

If the stable wrapper is absent or this skill was updated, deploy the bundled
launcher from the ordinary sandbox before requesting GPU execution permission:

```bash
<installed-skill>/scripts/install-gpu-exec --repository <absolute-main-checkout>
```

The installer copies `gpu-exec` and `gpu_probe.py` to `.agents/bin`; reinstalling
updates their contents without changing the approved entrypoint path. Do not run
the copy in a linked worktree or use the installed plugin-cache wrapper directly
for GPU commands.

## Shared uv environment

The main checkout's `<main-checkout>/.venv` is the only Python environment. Build
or update it from the main checkout with the repository's locked uv procedure.
The GPU wrapper only executes commands: it uses `uv run --active --no-sync` and
never creates, synchronizes, or changes an environment.

For a linked worktree, pass its exact path with `--workdir`. The wrapper sets
`VIRTUAL_ENV` to the main checkout's `.venv` and prepends the selected worktree's
`src` directory to `PYTHONPATH`, ahead of an editable install from the main
checkout. It also requires the worktree and main checkout to have identical
`uv.lock` files. If they differ, stop; decide how to update the shared environment
from the main checkout before retrying. Never sync or install dependencies into
the shared environment from a worktree.

The wrapper checks that the selected project's dependency declarations still
match its lockfile before execution. A missing environment, missing or stale
lockfile, or unavailable dependency is an environment failure. Do not switch to
Conda, system Python, automatic uv sync, or an unlocked execution.

## Commands

Use the stable absolute wrapper path in every example below.

```bash
<main-checkout>/.agents/bin/gpu-exec nvidia-smi
<main-checkout>/.agents/bin/gpu-exec --devices 0 probe
<main-checkout>/.agents/bin/gpu-exec --workdir <linked-worktree> --devices 0 probe
<main-checkout>/.agents/bin/gpu-exec --workdir <linked-worktree> --devices 0 pytest -q tests/test_cuda.py
<main-checkout>/.agents/bin/gpu-exec --workdir <linked-worktree> --devices 0 torchrun --standalone --nproc-per-node=1 train.py
```

The supported modes are:

| Mode | Executed command |
| --- | --- |
| `probe` | Shared-env Python runs the installed `gpu_probe.py` copy |
| `python ...` | `uv run --active --no-sync python ...` |
| `pytest ...` | `uv run --active --no-sync python -m pytest ...` |
| `torchrun ...` | `uv run --active --no-sync python -m torch.distributed.run ...` |
| `nvidia-smi ...` | `nvidia-smi ...`; uv is not required for inventory |

Omitting `--devices` preserves the existing `CUDA_VISIBLE_DEVICES`, including a
scheduler or container allocation. Use `--devices` only for devices authorized in
the local environment. The wrapper does not choose a default mask or worker count.
Specify `--nproc-per-node` to match the intended visible devices.

## Verification and diagnosis

Keep code edits, static checks, and CPU-only tests in the ordinary sandbox. Inspect
device occupancy before a substantial workload and run only experiments or tests
within the user's requested scope.

`nvidia-smi` is inventory evidence. Complete GPU verification with `probe`, which
must perform a real CUDA tensor operation using the shared environment and selected
checkout. For long jobs, poll the existing process instead of starting duplicates.
Diagnose failures in this order: stable-wrapper boundary, shared uv environment and
lock agreement, CUDA-enabled PyTorch build, driver and device visibility, memory,
then distributed settings. Report what was verified and any remaining limitation.
