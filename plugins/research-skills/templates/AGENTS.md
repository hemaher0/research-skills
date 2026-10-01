# Repository guidance

<!--
Copy the relevant sections into a repository's tracked AGENTS.md and replace every
angle-bracketed value. Keep portable repository policy here; put checkout paths,
environment details, GPU allocations, and Notion destinations in AGENTS.local.md.
Do not put credentials or tokens in either file.
-->

## Experiment records

- Base branch for new root experiments: `<base branch, for example main>`
- Default experiment document root: `<path relative to the main checkout, for example references/experiments>`
- New default record filename: `YYYY-MM-DD-<topic>-experiment.md` inside its dated directory; keep existing `experiment.md` paths.
- Default experiment artifact root: `<repository-relative path or external-output convention>`
- Default worktree root, when isolation is needed: `<repository-relative path or None>`
- Governing terminology or notation sources: `<repository-relative links or None>`
- Optional spec/change system: `<commands and ID mapping, or None>`
- Create a branch or worktree only for a concrete isolation need or a repository
  requirement. When one is created, name it with the Experiment ID and keep its
  root ignored locally.
- The `$experiments` skill owns a Markdown record only when persistent experiment
  management is requested. A standalone `$pilot` or `$report` needs no record.
  A completed record remains its local source of truth.
- A configured canonical work item captures every request and discussion and
  links the experiment. It does not change this scientific record's schema or
  require a document-routing plugin; use the local `.docs-schema` when present
  and ordinary file tools as fallback. The work-item repository and
  experiment-document root may be different. Keep each in its configured
  location; resolve relative experiment-document paths from the main checkout,
  not a code worktree. Do not create a document branch when a code experiment
  needs its own branch or worktree.
- When agents work in parallel, assign each independent task a distinct child
  work item if the local schema supports parent links. Each agent updates only
  its child; the coordinator owns the root and shared Git integration. Give a
  shared experiment or report one writer. Under an older schema, use one record
  writer and timestamped agent handoffs until migration.

## Experiment execution boundary

- `$experiments` supplies the scientific content, template, lifecycle, and
  evidence for requested experiment records; use an available document router
  for placement, writing, and review. If none is available, use the configured
  location, template, and ordinary file tools. Result tables, figures, and
  artifacts stay in their configured experiment locations.
- It must not create, modify, or delete source code, tests, notebooks, experiment
  scripts, dependency declarations, or runtime configuration.
- Use existing repository entrypoints for training, evaluation, and analysis. If
  the frozen protocol requires missing code, record the prerequisite and stop.
- Design discussion alone does not create an experiment document, branch,
  worktree, or run; it still updates a configured topic work item.
  Training and evaluation require a request that includes execution.
- A requested research pilot uses representative real conditions and no more than
  four total training or evaluation runs. Expanded execution requires a
  separately authorized run, time, and compute budget.
