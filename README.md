# Research Skills

Codex skills for AI/ML research. Install selected skills for one project or
for your user account. An optional `research-skills` plugin bundles the set.

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
| [notion-mirror](plugins/research-skills/skills/notion-mirror/SKILL.md) | Mirror a local experiment document under its configured trigger and existing authorization. |
| [run-gpu](plugins/research-skills/skills/run-gpu/SKILL.md) | Run CUDA work through a stable repository approval prefix and a shared uv or Conda environment. |

## Install for a project

Run from the target project's root. Reuse a suitable existing source checkout;
do not clone over one. Each project keeps its own source revision and selected
links, so projects can expose different skill sets independently.

```bash
mkdir -p .agents/vendor .agents/skills
git clone --branch main https://github.com/hemaher0/research-skills.git .agents/vendor/research-skills
```

Select individual skills by linking their complete directories. This example
exposes three skills; change the list to your selection:

```bash
for skill in exploration interpretation report; do
  target=".agents/skills/$skill"
  if [ -e "$target" ] || [ -L "$target" ]; then
    printf 'Preserve existing path: %s\n' "$target" >&2
    continue
  fi
  ln -s "../vendor/research-skills/plugins/research-skills/skills/$skill" "$target"
done
```

Alternatively, expose the complete set:

```bash
for source in .agents/vendor/research-skills/plugins/research-skills/skills/*; do
  [ -f "$source/SKILL.md" ] || continue
  skill="${source##*/}"
  target=".agents/skills/$skill"
  if [ -e "$target" ] || [ -L "$target" ]; then
    printf 'Preserve existing path: %s\n' "$target" >&2
    continue
  fi
  ln -s "../vendor/research-skills/plugins/research-skills/skills/$skill" "$target"
done
```

Preserve the native source tree:
`agents/`, scripts, and package templates are required resources. Copying only
`SKILL.md` or moving a folder away from its package templates loses resources.
The vendor directory is source storage; selected `.agents/skills` links expose
skills to Codex.

Verify a selected link and its path in Codex's skill selector (`/skills` in the
CLI), then invoke it with `$report` or another selected `$<skill-name>`. Codex
detects skill changes; restart it if the selection is stale.

```bash
readlink -f .agents/skills/report
test -f .agents/skills/report/SKILL.md
```

Use only applicable [project configuration](#project-configuration). Reasoning
skills alone need no new configuration file, GPU launcher or Notion setup.

### Update or remove a project installation

From the same project root, inspect local changes before updating:

```bash
git -C .agents/vendor/research-skills status --short
git -C .agents/vendor/research-skills pull --ff-only
```

Links follow this checkout's updates; other projects keep their own revisions.
Expose newly added skills only when selected. For a pinned revision, follow its
selected revision policy. Redeploy a changed GPU launcher separately.

To remove one skill, confirm its link points into this source checkout before
unlinking it:

```bash
readlink .agents/skills/report
unlink .agents/skills/report
```

Remove other selected links the same way. Preserve unrelated skills, records,
settings and deployed runtime files. Remove the source only when no retained
link or other work needs it.

## Install globally

A user-wide installation exposes the selected skills across projects. Its
source revision is shared; use independent project sources when selections or
revisions should differ. Reuse a suitable existing global checkout.

```bash
mkdir -p "$HOME/.agents/vendor" "$HOME/.agents/skills"
git clone --branch main https://github.com/hemaher0/research-skills.git "$HOME/.agents/vendor/research-skills"
```

Choose individual skills:

```bash
for skill in exploration interpretation report; do
  target="$HOME/.agents/skills/$skill"
  if [ -e "$target" ] || [ -L "$target" ]; then
    printf 'Preserve existing path: %s\n' "$target" >&2
    continue
  fi
  ln -s "../vendor/research-skills/plugins/research-skills/skills/$skill" "$target"
done
```

Alternatively, expose the complete set:

```bash
for source in "$HOME"/.agents/vendor/research-skills/plugins/research-skills/skills/*; do
  [ -f "$source/SKILL.md" ] || continue
  skill="${source##*/}"
  target="$HOME/.agents/skills/$skill"
  if [ -e "$target" ] || [ -L "$target" ]; then
    printf 'Preserve existing path: %s\n' "$target" >&2
    continue
  fi
  ln -s "../vendor/research-skills/plugins/research-skills/skills/$skill" "$target"
done
```

Retain the native vendor tree, including package templates and scripts. Verify
a selected link and its global path in Codex's selector. Invoke standalone
skills with `$<skill-name>`; restart Codex if changes do not appear.

```bash
readlink -f "$HOME/.agents/skills/report"
test -f "$HOME/.agents/skills/report/SKILL.md"
```

Global skills use the current project's configuration. They do not make one
project's paths, GPU environment or Notion destination universal defaults.

### Update or remove a global installation

```bash
git -C "$HOME/.agents/vendor/research-skills" status --short
git -C "$HOME/.agents/vendor/research-skills" pull --ff-only
```

Updates affect every project using these global links; independent project
sources keep their revision. Link newly added skills only when selected and
redeploy each changed project GPU launcher separately.

Confirm ownership before removing a global link:

```bash
readlink "$HOME/.agents/skills/report"
unlink "$HOME/.agents/skills/report"
```

Remove only selected links. Retain source used by other links/work, and leave
project records, settings and deployed launchers to their own lifecycle.

## Discovery and optional routing

Codex scans project `.agents/skills` from the working directory up to the
repository root and user skills in `$HOME/.agents/skills`. It supports linked
skill folders. Same-name local, global and plugin skills are not merged; local
installation does not hide a global copy. For distinct project sets, expose
skills locally and remove or disable overlapping global/plugin copies through
their actual configuration. See the
[official discovery and disable settings](https://learn.chatgpt.com/docs/build-skills).

A companion skill is used only when listed as available by the current host
and applicable to the work. Vendor/cache file existence is not availability.
Each skill retains its own method and uses project procedures or ordinary tools
when a companion is absent. Missing optional skills do not cause errors,
recursive routing, automatic installation, or weaker evidence requirements.
Package templates/scripts remain resources, not companion skills.

## Project configuration

For either installation scope, use the current project's existing instructions
and authoritative settings. Configure only the capability in use. Conversational
reasoning/reporting needs no managed experiment store or new `AGENTS.local.md`.

Use the [project template](plugins/research-skills/templates/AGENTS.md) and
[local override template](plugins/research-skills/templates/AGENTS.local.md)
only for missing project choices. Preserve existing rules and other packages'
sections. Shared research settings and reproducible environments stay in their
native manifests/configuration. Private host overrides may use project-root
`AGENTS.local.md`; if created, connect it through existing `AGENTS.md` or
`AGENTS.override.md`. Preserve existing instructions. If root `AGENTS.md` is
absent and a local file was intentionally created, use
`ln -s AGENTS.local.md AGENTS.md` to connect it.

- Persistent experiment management uses the package
  [experiment template](plugins/research-skills/templates/experiment.md),
  scientific identity/protocol/lifecycle, and the configured document root.
  Unless otherwise configured, new records use
  `references/experiments/YYYY-MM-DD-<topic>/YYYY-MM-DD-<topic>-experiment.md`
  relative to the main checkout. Keep existing record paths.
- GPU work uses each project's native environment/allocation and a separately
  deployed stable launcher as described below.
- Notion mirrors follow configured triggers and existing standing or direct
  authorization. Authorized automatic sync can include ongoing records; do not
  require another request or complete a record just to mirror it.

For Notion, verify the selected integration source and destination URL/type.
For a data source, configure its ID and exact title, record-ID, applicable
category and scientific-state mappings. For a parent page, configure the
exact-ID child-title pattern. Credentials stay with the connector. Omit unused
features; resolve essential missing destination/access before a mirror.
Installation itself does not create records, run workloads or synchronize pages.

Check effective instructions and configuration needed for the actual work.
Use an available compatible document workflow or ordinary file tools for local
record operations. Capture follows project policy; installation does not enable
it. Git naming, workspace isolation, review and publication follow project
instructions and existing authorization. An experiment may use several code
repositories; preserve each revision and the selected execution environment.

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
Use $notion-mirror to mirror this local experiment document under the configured trigger and existing authorization.
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
  [Consequential choices](plugins/research-skills/skills/evidence-based-research/SKILL.md#ground-consequential-choices)
  connect purpose, applicable evidence, unresolved premises, and observations
  needed before dependent work. Evidence effort follows impact, uncertainty,
  and reversibility; defaults, protocol records, and successful execution do not
  establish scientific suitability. This applies without a managed experiment
  record and preserves authorized exploration.
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
- **notion-mirror:** Follow configured triggers and existing authorization,
  including standing authorization for ongoing records. Preserve scientific
  status. The skill is optional: an authorized project mirror can use its
  existing connector and ordinary file tools. Notion access and verified
  destination/identity/state mappings are required. Private overrides belong
  to the current project; a failed mirror does not change scientific status.
- **run-gpu:** Requires Bash and Git. Inventory uses `nvidia-smi` without a
  Python environment. The default uv backend uses the main checkout's
  `pyproject.toml`, `uv.lock`, and `.venv`. The Conda backend uses `conda` and an
  explicit existing environment prefix with Python. CUDA execution requires an
  NVIDIA GPU, a driver, and CUDA-enabled PyTorch in the selected environment.
- Run the installed skill's `install-gpu-exec` once to deploy the stable
  entrypoint at the target repository's `.agents/bin/gpu-exec`. Reinstalling
  after a source or plugin update preserves this path so every GPU command begins with
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
  server. Follow existing SSH and scheduler procedures. Skill installation
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

Deploy only for a project that needs GPU setup. For a project-local source, run
the bundled installer in the ordinary sandbox with that project's main checkout:

```bash
.agents/vendor/research-skills/plugins/research-skills/skills/run-gpu/scripts/install-gpu-exec --repository /absolute/path/to/main-checkout
```

For a global source, deploy the same files to the selected project's main checkout:

```bash
"$HOME/.agents/vendor/research-skills/plugins/research-skills/skills/run-gpu/scripts/install-gpu-exec" --repository /absolute/path/to/main-checkout
```

The installer copies `gpu-exec` and `gpu_probe.py` to the project's `.agents/bin`;
it does not link a source wrapper or build an environment. Redeploy changed
launcher files separately. Unlinking a skill leaves these copies; retain them
while used and remove only the owned copies when GPU support is retired.
Use the printed absolute path, `<main-checkout>/.agents/bin/gpu-exec`, as the
single reusable approval prefix for GPU execution. Put `--workdir`, `--devices`,
the execution mode, and its arguments after this fixed path. Do not execute GPU
commands directly through a wrapper in the plugin cache.

## Optional plugin installation

The plugin package remains at `plugins/research-skills/` and the repository
[marketplace](.agents/plugins/marketplace.json) remains available. Use the
[official plugin guide](https://developers.openai.com/plugins/build/plugins)
when choosing bundle distribution. A plugin exposes its complete skill set and
uses a managed installed copy under `~/.codex/plugins/cache/`; direct links read
their source checkout. Shared plugin caching does not isolate project revisions.

Project and user plugin enablement are separate settings. Preserve existing
marketplace entries and its actual name when configuring a project. CLI/browser
user installation choices are user-scoped. Refresh/update/remove through the
chosen plugin route and inspect actual paths if also using direct skills.
Project runtime files and records remain separately owned.

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
Direct links follow source updates; plugin refresh uses the selected plugin
route. A manifest version change is not required merely for a local update. An edit or push alone
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
