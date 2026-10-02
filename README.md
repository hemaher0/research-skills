# Research Skills

Codex skills for AI/ML research. **All skills in this repository are installed,
updated, and removed together as one `research-skills` plugin.**

## Included skills

Research can start from a precedent, an unexplained result, a partial hypothesis,
or a user-provided cue. Select the skill that addresses the current uncertainty;
the list below is not a mandatory sequence. Questions and explanations can
change, and useful findings can remain incomplete.

| Skill | Purpose |
| --- | --- |
| [exploration](plugins/research-skills/skills/exploration/SKILL.md) | Investigate precedents, their evidence, conditions, and conflicts. |
| [digging](plugins/research-skills/skills/digging/SKILL.md) | Decompose a specific problem and inspect its uncertain connections, using targeted reproduction when useful. |
| [interpretation](plugins/research-skills/skills/interpretation/SKILL.md) | Analyze existing results and judge what they support or leave unresolved. |
| [reinterpretation](plugins/research-skills/skills/reinterpretation/SKILL.md) | Recombine research cues into another connection, concept, or question. |
| [probing](plugins/research-skills/skills/probing/SKILL.md) | Develop provisional hypotheses, expose assumptions, and identify informative observations. |
| [evidence-based-research](plugins/research-skills/skills/evidence-based-research/SKILL.md) | Advance an inquiry through purposeful attempts, evidence, and revised judgment. |
| [experiments](plugins/research-skills/skills/experiments/SKILL.md) | Manage the protocol, lineage, execution state, and evidence of a requested persistent experiment record. |
| [pilot](plugins/research-skills/skills/pilot/SKILL.md) | Obtain new evidence under representative conditions within an authorized execution scope. |
| [report](plugins/research-skills/skills/report/SKILL.md) | Present current findings and open questions faithfully in the requested format. |
| [notion-mirror](plugins/research-skills/skills/notion-mirror/SKILL.md) | Mirror a completed local experiment document to its configured Notion destination when requested. |
| [run-gpu](plugins/research-skills/skills/run-gpu/SKILL.md) | Run CUDA work through a stable repository approval prefix and a shared uv or Conda environment. |

## Install for a project

Install the plugin and complete applicable project settings using the steps
below. Preserve existing instructions and established choices.

Keep the marketplace and enablement in the target project using the files
below. Write these project files directly: `codex plugin marketplace add` and
`codex plugin add` save user-level configuration in `~/.codex/config.toml`;
running them from a project directory does not make them project-scoped.
The plugin browser also saves user-level enablement choices.
Neither route is a step in this project-only procedure.

Reuse a suitable source checkout when present. For a first setup, run these
commands from the **target project's root**, with Git access to this repository:

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

Complete the project configuration below, then open the project as trusted and
start a **new Codex session**; restart the desktop app when needed. Codex uses
the project configuration during local marketplace discovery and refresh.
Verify that the plugin's skills are available in that project session.
Project configuration is loaded only for trusted projects.

Codex may keep plugin files in its shared `~/.codex/plugins/cache/`; that cache
location does not determine enablement scope. Existing user-level enablement
remains a separate setting; adding project settings does not remove it.
See the [official project plugin configuration guide](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).

## Project configuration

Writing root `AGENTS.local.md` is a required installation step.

1. Read existing project instructions, the
   [project template](plugins/research-skills/templates/AGENTS.md) and the
   [local configuration template](plugins/research-skills/templates/AGENTS.local.md).
   Create the local file from the template, or merge its research section into
   the existing file. Preserve established settings and other packages' sections.
2. Replace applicable placeholders with actual document/artifact paths, host
   settings and integration configuration. Use established paths or the
   documented record defaults in [experiments](plugins/research-skills/skills/experiments/SKILL.md).
   Resolve relative experiment-document paths from the main checkout.
3. Keep shared research choices in their project configuration and reproducible
   environments in native manifests/setup configuration. Follow
   [run-gpu](plugins/research-skills/skills/run-gpu/SKILL.md) for the shared uv or
   Conda environment and stable wrapper. Where settings already exist,
   reference their actual source and verify its contents. Credentials remain
   with their existing credential store or connector.
4. For Notion mirroring, fill the destination configuration as described below.
   Remove fields for features the project does not use. `Disabled`/`Not Configured`
   denotes an unused integration, not an unknown destination. Required unset
   values keep configuration incomplete.
5. Connect the local file to root instructions using the procedure below.

If root `AGENTS.md` exists, preserve it and add this instruction unless it
already reads or resolves to the local file:

```markdown
Read and follow root AGENTS.local.md when it exists.
```

If `AGENTS.md` is absent, the recommended connection is a relative symbolic
link from the project root, after writing `AGENTS.local.md`:

```bash
ln -s AGENTS.local.md AGENTS.md
```

Preserve existing files and links and avoid self-references. If
`AGENTS.override.md` takes precedence, ensure it reads the local file.

### Notion destination settings

Fill these actual values when Notion mirroring is used:

- Destination URL and destination type: parent page or data source.
- For a parent page: the child-title pattern containing the exact Experiment ID.
- For a data source: its identifier, title and Experiment ID property mappings,
  and the status property and value corresponding to Completed.

Use the existing selected integration configuration when present. Otherwise,
write these destination fields directly in root `AGENTS.local.md`. If stored
elsewhere, fill the configuration-source field with that actual file's path
and verify that its required destination fields are filled. A pointer to a
nonexistent file, a placeholder URL or "use defaults" does not configure
Notion. The destination contract is in
[notion-mirror](plugins/research-skills/skills/notion-mirror/SKILL.md).

Before completing installation, read the completed local file and referenced
configuration. Verify that applicable values are filled, no placeholders
remain, configured paths resolve, and effective instructions read the local
file. Check actual marketplace paths/name and skill availability in a new
session. Verify the GPU wrapper when GPU setup is used, and report any
unverified Notion access. Installation does not run a research workload or
create a Notion page.

Reasoning skills supply scientific judgment; `experiments` supplies record
identity, provenance, lineage, format, and lifecycle. Forward document discovery,
placement, writing, editing, and review to an available document router;
otherwise use project conventions and ordinary file tools. Experiment records
and work records do not replace each other.

An experiment may use several repositories; preserve each contribution's code
identity and the execution environment for each run. Git naming, isolation,
remote operations and integration follow the project's Git workflow rather
than a separate experiment-specific procedure.

Unless project configuration selects another location, new experiment records
use this path relative to the main checkout:

```text
references/experiments/YYYY-MM-DD-<topic>/YYYY-MM-DD-<topic>-experiment.md
```

Configured roots and filename conventions take precedence. Keep existing
record paths when continuing an experiment.

## Usage

Skills may be selected automatically for relevant requests or invoked explicitly:

```text
Use $exploration to investigate the closest precedents and the conditions under which their conclusions hold.
Use $digging to trace the assumptions and implementation behind this unexplained behavior.
Use $interpretation to analyze these results, including variation, exceptions, and the evidence limits.
Use $reinterpretation to examine whether these research cues suggest a different connection or question.
Use $probing to develop a provisional explanation and identify an observation that would clarify it.
Use $evidence-based-research to investigate this question iteratively and revise the next attempt based on what is learned.
Use $experiments to create a local record and manage this research's plan and results over time.
Use $pilot to plan the essential comparisons and representative execution needed to investigate this question.
Use $pilot to execute the agreed pilot and report its results in this conversation.
Use $report to present the current findings and open questions in this conversation.
Use $report to present the reviewed analysis in the existing experiment record.
Use $notion-mirror to mirror the completed local experiment document to its configured Notion destination.
Use $run-gpu to inspect GPU status and verify a CUDA tensor operation in this repository's selected shared uv or Conda environment.
```

### Environment and workflow requirements

- **Reasoning skills:** Work in the conversation or existing project records
  unless a durable deliverable is requested or required. Investigation does not
  require a persistent experiment, a settled hypothesis, numerical predictions,
  a new run, or a complete paper. Preserve user contributions, negative and
  unexpected findings, and the evidence behind changed or unchanged judgments.
- **evidence-based-research and probing:** `probing` develops the hypothesis and
  its assumptions; `evidence-based-research` chooses and revisits attempts.
  Continue iterations within the authorized inquiry and execution budget, with
  a new scope decision only when
  that boundary needs to change. Code implementation uses the available
  development workflow; research does not require an artificial failing test.
- **experiments:** Update the same Markdown record from planning through final
  analysis only when persistent record management is requested. Create branches
  or worktrees only for a concrete isolation need. Do not change source, tests,
  notebooks, experiment scripts, or dependencies as a side effect of record management.
  Preserve dated question/protocol changes and earlier expectations. `Completed`
  closes the record's declared work, while scientific questions may remain open.
- **pilot:** Works without an `experiments` record. Use existing entrypoints and
  preserve the model, data, evaluation quantity, scale, duration, and environment
  needed for the question. Narrow comparisons while retaining required
  replications. Toy data and arbitrarily shortened runs are software checks.
  Use project policy and the authorized run count or adaptive resource boundary.
  Specify added conditions, runs, time, and compute before expansion beyond that
  boundary.
- **interpretation and report:** `interpretation` analyzes evidence; `report`
  communicates it in the requested format and checks fidelity to the sources.
  Both can return a conversational answer with unresolved questions. Create
  files only for a requested or project-required deliverable; new runs and
  experiment records are not prerequisites.
- **notion-mirror:** Use only when mirroring a completed local experiment
  document is requested. It is not a prerequisite for other research skills.
  Notion access and a selected destination configuration are required.
  Private/host overrides in the installation's `AGENTS.local.md` are optional.
  Missing settings or access do not change the local experiment's completed status.
- **run-gpu:** Requires Bash and Git. Inventory uses `nvidia-smi` without a
  Python environment. The default uv backend uses the main checkout's
  `pyproject.toml`, `uv.lock`, and `.venv`. The Conda backend uses `conda` and an
  explicit existing environment prefix with Python. CUDA execution requires an
  NVIDIA GPU, a driver, and CUDA-enabled PyTorch in the selected environment.
- Run the installed skill's `install-gpu-exec` once to deploy the stable
  entrypoint at the target repository's `.agents/bin/gpu-exec`. Reinstalling
  after a plugin update preserves this path so every GPU command begins with
  the same approval prefix.
- The main checkout and linked worktrees share the selected project environment
  and prioritize the selected worktree's `src`. uv uses
  `uv run --active --no-sync` and requires matching `uv.lock` files. Conda uses
  `--backend conda --conda-prefix <absolute-environment-path>` and
  `conda run --no-capture-output --prefix`; `--conda-spec <repository-relative-file>`
  checks main/worktree declaration agreement when selected. Verify installed
  packages through the project's setup procedure. The wrapper does not install
  dependencies or switch backends after a failure.
- Without a GPU selection, preserve the existing `CUDA_VISIBLE_DEVICES`. Use
  `--devices` only for explicit device selection. The caller's options determine
  the number of `torchrun` processes. Respect scheduler and container allocations.
- On a remote server, use the wrapper and repository paths installed on that
  server. Follow existing SSH and scheduler procedures. Plugin installation
  does not grant GPU access.

`run-gpu` resolves checkout and wrapper paths from Git, verifies the selected shared
environment for Python execution, and checks the current allocation. A local host profile supplies
only necessary constraints or connection context. Verify allocated devices at execution time.
Notion mirroring requires a destination URL and the identifiers and properties
appropriate for that destination type.

Reasoning, pilot execution, reporting, and persistent record management are
independent capabilities. Skill selection alone does not create
runs, code changes, local documents, worktrees, or Notion pages.

A requested pilot can include necessary bounded preparation within the agreed
question, representative conditions and execution budget. Use the responsible
development/environment workflow and verify that preparation. Resolve a
material change of scientific conditions or authority before affected execution.

Work-item updates follow the project's history capture policy, including GPU
work and Notion mirroring. A configured repository alone does not enable
all-turn capture. Selective or disabled capture does not prevent requested
research records, reports, execution, or mirrors and their required evidence.
Update reader-facing documentation only when requested.

### Install the GPU entrypoint

From the main checkout, run the project's installer in the ordinary sandbox:

```bash
.agents/vendor/research-skills/plugins/research-skills/skills/run-gpu/scripts/install-gpu-exec --repository /absolute/path/to/main-checkout
```

Use the printed absolute path, `<main-checkout>/.agents/bin/gpu-exec`, as the
single reusable approval prefix for GPU execution. Put `--workdir`, `--devices`,
the execution mode, and its arguments after this fixed path. Do not execute GPU
commands directly through a wrapper in the plugin cache.

## Update or remove from a project

From the target project's root, update its source checkout:

```bash
git -C .agents/vendor/research-skills pull --ff-only
```

Restart the app if using the desktop client and start a new Codex session so
the local plugin is refreshed. Run `install-gpu-exec` again if its bundled
launcher changed.

To disable it for this project, set
`plugins."research-skills@project-skills".enabled = false` in
`.codex/config.toml`, using the project's actual marketplace name. To remove
the project setup, remove that configuration entry and only the `research-skills`
entry from `.agents/plugins/marketplace.json`. Keep other plugins' entries.
The source checkout can be removed separately once it is no longer needed.
If the GPU entrypoint was installed and is no longer used, also remove its
deployed `.agents/bin/gpu-exec` and `.agents/bin/gpu_probe.py` files. Plugin removal
does not remove those repository-local copies.

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
    ├── exploration/
    ├── digging/
    ├── interpretation/
    ├── reinterpretation/
    ├── probing/
    ├── evidence-based-research/
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
Every included skill has an `agents/openai.yaml` for its name, selection
description, and example prompt. The reasoning skills include their research
basis and evidence limits in `SKILL.md`; no separate workflow document is required.
Place optional `agents/` or `scripts/` alongside them and reusable templates
in `plugins/research-skills/templates/`. Keep **one plugin** in the marketplace.

Manage `version` in `.codex-plugin/plugin.json` when preparing a release.
Local plugin refresh follows the source-update and restart steps above; a
manifest version change is not required for that refresh. An edit or push alone
does not require a new release.

## Development checks

```bash
python3 -m unittest discover -s tests -v
```

Tests verify stable entrypoint installation, repository and worktree boundaries,
the shared uv/Conda environment selection, declaration agreement, command
forwarding, and failure handling without starting GPU workloads. When `conda`
is available, they check real activation and execution with a temporary prefix
and linked worktree. When `uv` is available, they also check real
`uv run --active --no-sync` execution in a temporary project and linked worktree
that need no external dependencies.
