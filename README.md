# Research Skills

Codex skills for AI/ML research. **All skills in this repository are installed,
updated, and removed together as one `research-skills` plugin.**

## Included skills

| Skill | Purpose |
| --- | --- |
| [experiments](plugins/research-skills/skills/experiments/SKILL.md) | Manage the protocol, lineage, execution state, and evidence of a requested persistent experiment record. |
| [pilot](plugins/research-skills/skills/pilot/SKILL.md) | Plan or run a bounded pilot under representative real conditions, with or without an experiment record. |
| [report](plugins/research-skills/skills/report/SKILL.md) | Interpret existing research evidence and report it in the requested format. |
| [notion-mirror](plugins/research-skills/skills/notion-mirror/SKILL.md) | Mirror a completed local experiment document to its configured Notion destination when requested. |
| [run-gpu](plugins/research-skills/skills/run-gpu/SKILL.md) | Run CUDA work through a stable repository approval prefix and the main checkout's shared uv environment. |

## Install for a project

Use a repository marketplace and project configuration. Run these commands from
the **target project's root**, with Git access to this repository:

```bash
mkdir -p .agents/vendor .agents/plugins .codex
git clone --branch main https://github.com/hemaher0/research-skills.git .agents/vendor/research-skills
```

Create or merge the following into the target project's
`.agents/plugins/marketplace.json`:

```json
{
  "name": "project-skills",
  "plugins": [
    {
      "name": "research-skills",
      "source": {
        "source": "local",
        "path": "./.agents/vendor/research-skills/plugins/research-skills"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Keep existing marketplace entries. When using multiple skill repositories, add
their entries to the same `plugins` array. Paths resolve from the target
project's root. If its marketplace already has a different `name`, keep that
name and use it in the configuration keys below.

Merge this setting into the target project's `.codex/config.toml`:

```toml
[plugins."research-skills@project-skills"]
enabled = true
```

Open the target project as a trusted project in Codex, restart the app if using
the desktop client, and start a **new Codex session**. Project configuration is
loaded only for trusted projects. The marketplace source and enablement belong
to this project; Codex may still store installed copies in its shared cache.
See the [official repository marketplace and project configuration guide](https://developers.openai.com/plugins/build/plugins).

## Project configuration

1. Projects that use work records choose one canonical work-item repository
   and record format. Without a document router, continue using project
   instructions, the local `.docs-schema` when present, and ordinary file tools.
2. Merge the relevant sections of the [research AGENTS.md template](plugins/research-skills/templates/AGENTS.md)
   and [AGENTS.local.md template](plugins/research-skills/templates/AGENTS.local.md)
   into the project's files. Fill in actual experiment document and artifact
   paths, execution environments, GPU allocations, and Notion destinations.
   Installation does not create these files automatically. The templates are
   available in `.agents/vendor/research-skills/plugins/research-skills/templates/`.
3. The work-item repository and experiment document root may differ. Resolve
   relative experiment document paths from the main checkout. If experiment
   code needs a branch or worktree, keep document records on their configured
   primary branch and connect the two records with links.

Research skills supply scientific judgment and the format, lifecycle, and
evidence standards for experiment records. Forward document discovery,
placement, writing, editing, and review to an available document router;
otherwise use project conventions and ordinary file tools. Experiment records
and work records do not replace each other.

## Usage

Skills may be selected automatically for relevant requests or invoked explicitly:

```text
Use $experiments to create a local record and manage this research's plan and results over time.
Use $pilot to plan the smallest representative run that can assess this hypothesis through an existing entrypoint.
Use $pilot to execute the agreed pilot and report its results in this conversation.
Use $report to interpret the evidence already available and explain it in this conversation.
Use $report to complete the analysis in the existing experiment record.
Use $notion-mirror to mirror the completed local experiment document to its configured Notion destination.
Use $run-gpu to inspect GPU status and verify a CUDA tensor operation in this repository's shared uv environment.
```

### Environment and workflow requirements

- **experiments:** Update the same Markdown record from planning through final
  analysis only when persistent record management is requested. Create branches
  or worktrees only for a concrete isolation need. Do not change source, tests,
  notebooks, experiment scripts, or dependencies as a side effect of record management.
- **pilot:** Works without an `experiments` record. Use existing entrypoints and
  preserve the model, data, evaluation quantity, and execution environment.
  Run no more than four training or evaluation runs in total. Before expanded
  execution, specify the additional runs, time, and compute and obtain a
  separate scope decision.
- **report:** Interpret existing evidence. Handle investigation and answer
  requests in the conversation; create local files only when a document
  deliverable is requested. A new pilot or experiment record is not a prerequisite.
- **notion-mirror:** Use only when mirroring a completed local experiment
  document is requested. It is not a prerequisite for other research skills.
  Notion access and destination-specific settings in the repository's
  `AGENTS.local.md` are required. Missing settings or access do not change the
  local experiment's completed status.
- **run-gpu:** Uses Bash, Git, `uv`, and the main checkout's `pyproject.toml`,
  `uv.lock`, and `.venv`. CUDA execution requires an NVIDIA GPU, a driver, and
  CUDA-enabled PyTorch in the shared environment. Conda environments are not used.
- Run the installed skill's `install-gpu-exec` once to deploy the stable
  entrypoint at the target repository's `.agents/bin/gpu-exec`. Reinstalling
  after a plugin update preserves this path so every GPU command begins with
  the same approval prefix.
- The main checkout and linked worktrees share the main checkout's single
  `.venv`. The wrapper uses `uv run --active --no-sync` and prioritizes the
  selected worktree's `src`. It stops if the two checkouts' `uv.lock` files differ.
- Without a GPU selection, preserve the existing `CUDA_VISIBLE_DEVICES`. Use
  `--devices` only for explicit device selection. The caller's options determine
  the number of `torchrun` processes. Respect scheduler and container allocations.
- On a remote server, use the wrapper and repository paths installed on that
  server. Follow existing SSH and scheduler procedures. Plugin installation
  does not grant GPU access.

`run-gpu` reads local settings to identify the current host's repository paths,
shared uv environment, and GPU allocation; it does not run other Python
environment types. Verify dynamically allocated devices at execution time.
Notion mirroring requires a destination URL and the identifiers and properties
appropriate for that destination type.

Pilot execution, interpretation of existing results, and persistent record
management are independent requests. Skill selection alone does not create
runs, code changes, local documents, worktrees, or Notion pages.

If a work-item repository is configured, preserve every request and discussion
in its owning topic record, including GPU work and Notion mirroring. Update
reader-facing documentation only when requested. New experiment records default
to `YYYY-MM-DD-<topic>-experiment.md`; do not rename existing `experiment.md` files automatically.

### Install the GPU entrypoint

From the main checkout, run the project's installer in the ordinary sandbox:

```bash
.agents/vendor/research-skills/plugins/research-skills/skills/run-gpu/scripts/install-gpu-exec --repository /absolute/path/to/main-checkout
```

Use the printed absolute path, `<main-checkout>/.agents/bin/gpu-exec`, as the
single reusable approval prefix for GPU execution. Put `--workdir`, `--devices`,
the execution mode, and its arguments after this fixed path. Do not execute GPU
commands directly through a wrapper in the plugin cache.

## Update for a project

From the target project's root, update its source checkout:

```bash
git -C .agents/vendor/research-skills pull --ff-only
```

Restart the app if using the desktop client and start a new Codex session so
the local plugin is refreshed. Run `install-gpu-exec` again if its bundled
launcher changed.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/research-skills/
├── .codex-plugin/plugin.json
├── templates/
│   ├── AGENTS.md
│   ├── AGENTS.local.md
│   └── experiment.md
└── skills/
    ├── experiments/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── pilot/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── report/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── notion-mirror/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    └── run-gpu/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── scripts/
            ├── install-gpu-exec
            ├── gpu-exec
            └── gpu_probe.py
```

Add new skills at `plugins/research-skills/skills/<skill-name>/SKILL.md`.
Place optional `agents/` or `scripts/` alongside them and reusable templates
in `plugins/research-skills/templates/`. Keep **one plugin** in the marketplace.

For a release that updates installed copies, manage `version` in
`.codex-plugin/plugin.json` so the cache can distinguish the new content.
An edit or push alone does not require a new release.

## Development checks

```bash
python3 -m unittest discover -s tests -v
```

Tests verify stable entrypoint installation, repository and worktree boundaries,
the shared `.venv`, command forwarding, and failure handling without starting
GPU workloads. When `uv` is available, they also check real
`uv run --active --no-sync` execution in a temporary project and linked worktree
that need no external dependencies.
