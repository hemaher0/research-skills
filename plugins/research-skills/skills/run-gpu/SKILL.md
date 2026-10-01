---
name: run-gpu
description: Use when a Git repository with a shared uv environment requires NVIDIA GPU or CUDA diagnostics, torch.cuda tests, CUDA pytest cases, NCCL, nvidia-smi, or torchrun from its main checkout or linked worktrees.
---

# Run GPU

Run GPU commands through the repository's stable, protected entrypoint. The main
checkout owns one uv environment, and every linked worktree uses that same
environment while importing its own source first. Conda is not an execution or
fallback environment.

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
confirm the shared uv `.venv`, and inspect the current permitted allocation.
The dependency declarations, scheduler and host approval controls remain
authoritative; a local snapshot cannot grant devices or execution permission.
Host constraints can narrow the current allocation, never expand it.
No local file is needed when those sources already resolve the environment.
A configured alternative Python environment does not change wrapper support.

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
Diagnose failures in this order: stable-wrapper boundary, shared uv environment and
lock agreement, CUDA-enabled PyTorch build, driver and device visibility, memory,
then distributed settings. Report what was verified and any remaining limitation.
