---
name: run-gpu
description: Use when a Git repository with a shared uv or Conda environment requires NVIDIA GPU or CUDA diagnostics, torch.cuda tests, CUDA pytest cases, NCCL, nvidia-smi, or torchrun from its main checkout or linked worktrees.
---

# Run GPU

Run GPU commands through the repository's stable, protected entrypoint. The main
checkout owns the environment selection: its uv `.venv` or an explicitly
selected Conda prefix. Linked worktrees use that same project environment while
importing their own source first.

Follow the project's work-history capture policy. When it calls for a work-item
update, preserve the GPU request, environment and code identity, observed
result, and next action there. A configured storage location does not enable
capture; selective or disabled capture does not prevent authorized GPU work
or its required execution evidence. Use an
available document router for the update; if none is available, use project
instructions, the local `.docs-schema` when present, and ordinary file tools.
This trace does not create an experiment record or change the GPU execution
boundary below.

## Stable entrypoint and permission

Read effective project instructions and native environment/scheduler
configuration; use a selected host profile in `AGENTS.local.md` when present.
Resolve the main checkout and worktree relationship from actual Git state,
confirm the selected shared environment, and inspect the current permitted allocation.
The dependency declarations, scheduler and host approval controls remain
authoritative; a local snapshot cannot grant devices or execution permission.
Host constraints can narrow the current allocation, never expand it.
No environment override is needed when those sources already resolve it.
GPU work consumes these settings; installation configuration follows the
source README.
Choose the backend from the project's environment procedure. uv is the default;
Conda requires `--backend conda --conda-prefix <absolute-environment-path>`.
If the project identifies an environment by name, resolve its actual prefix
through existing configuration or `conda env list --json` before execution.

Derive and verify the stable wrapper path from the main checkout. Its fixed
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
that checkout and worktrees sharing its Git common directory, and selects
the project environment explicitly. A repository-specific approval therefore does not
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

## Shared environment

Build or update the selected environment through the project's native setup
procedure. The GPU wrapper executes commands without creating, installing,
synchronizing, or updating an environment. Use the same backend and environment
for the main checkout and its linked worktrees. An execution failure does not
select a different backend or the ambient activated environment.

### uv (default)

The main checkout's `<main-checkout>/.venv` is the shared uv environment. Build
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
another backend, system Python, automatic uv sync, or an unlocked execution.

### Conda

Pass `--backend conda --conda-prefix <absolute-environment-path>` before the
command. The prefix must contain an executable `bin/python` and
`conda-meta/history`; the `conda` executable must be on PATH. Existing activation
variables and `VIRTUAL_ENV` do not select or override this environment. The
wrapper uses `conda run --no-capture-output --prefix <prefix>` so output remains
visible while Conda applies the selected environment's activation settings.

Conda execution does not require uv, `.venv`, or `uv.lock`. Verify the selected
prefix against the project's dependency declarations and installed packages
before a research run. When the project has a Conda environment declaration or
lockfile, pass its repository-relative path with `--conda-spec`, for example
`--conda-spec environment.yml`. The wrapper requires that file to exist in both
checkouts with identical bytes. File agreement alone does not prove installed
package agreement. Without that option, the wrapper checks prefix validity;
dependency compatibility remains part of the project preflight.

For a linked worktree, retain the same absolute prefix and pass `--workdir`.
Its `src` is prepended to `PYTHONPATH` as with uv. Stop on missing runtime,
invalid prefix, or a selected specification mismatch; resolve the environment
through the project's setup procedure before retrying.

See the [Conda run reference](https://docs.conda.io/projects/conda/en/stable/commands/run.html)
for prefix selection and output handling.

## Commands

Use the stable absolute wrapper path in every example below.

```bash
<main-checkout>/.agents/bin/gpu-exec nvidia-smi
<main-checkout>/.agents/bin/gpu-exec --devices 0 probe
<main-checkout>/.agents/bin/gpu-exec --workdir <linked-worktree> --devices 0 probe
<main-checkout>/.agents/bin/gpu-exec --workdir <linked-worktree> --devices 0 pytest -q tests/test_cuda.py
<main-checkout>/.agents/bin/gpu-exec --workdir <linked-worktree> --devices 0 torchrun --standalone --nproc-per-node=1 train.py
<main-checkout>/.agents/bin/gpu-exec --backend conda --conda-prefix <absolute-conda-env> --conda-spec environment.yml --workdir <linked-worktree> --devices 0 probe
```

The supported modes are:

| Mode | Executed command |
| --- | --- |
| `probe` | Shared-env Python runs the installed `gpu_probe.py` copy |
| `python ...` | Selected backend runs `python ...` |
| `pytest ...` | Selected backend runs `python -m pytest ...` |
| `torchrun ...` | Selected backend runs `python -m torch.distributed.run ...` |
| `nvidia-smi ...` | `nvidia-smi ...`; no Python environment or backend runtime is required |

Omitting `--devices` preserves the existing `CUDA_VISIBLE_DEVICES`, including a
scheduler or container allocation. Use `--devices` only for devices authorized in
the current allocation or configured host constraint. The wrapper does not
choose a default mask or worker count. Keep job/device observations in the
existing run/work record rather than treating local configuration as inventory.
Specify `--nproc-per-node` to match the intended visible devices.

## Verification and diagnosis

Keep code edits, static checks, and CPU-only tests in the ordinary sandbox. Inspect
device occupancy before a substantial workload and run only experiments or tests
within the user's requested scope.

`nvidia-smi` is inventory evidence. Complete GPU verification with `probe`, which
must perform a real CUDA tensor operation using the shared environment and selected
checkout. For long jobs, poll the existing process instead of starting duplicates.
Diagnose failures in this order: stable-wrapper boundary, selected shared environment and
dependency agreement, CUDA-enabled PyTorch build, driver and device visibility, memory,
then distributed settings. Report what was verified and any remaining limitation.
