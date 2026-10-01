# Project Research Configuration

<!-- Merge only project choices into effective instructions or reference an
existing project configuration. Omit settings using domain defaults and
preserve existing rules. Host/private path overrides belong in AGENTS.local.md
when necessary; credentials remain in their existing credential store. -->

## Research Records

- Default experiment document root, if overriding the skill default: `<project-relative location>`
- Default experiment artifact root, if designated: `<project location or existing artifact configuration>`
- Governing terminology or notation sources, if required: `<existing project sources>`

Scientific reasoning, record ownership, execution boundaries, and default
filenames remain in the responsible research skills. Research questions may
evolve and remain unresolved; a persistent record and a finished report are
separate requested deliverables. Execution budgets follow project policy and
the scope authorized for the inquiry. Registered
work history follows the project's document policy and existing local schema.
Branch/worktree policy belongs to the project's Git procedure. Reuse existing
records and selected roots.

## Execution Configuration

Use the repository's native dependency/environment declarations, setup guide,
and scheduler/container configuration. Inspect the actual main checkout,
environment and available allocation when needed; record run-specific revision,
job/device allocation, and evidence in the experiment or work record. The GPU
skill and wrapper own their stable entrypoint and shared uv environment contract.

## Notion Mirror Configuration (when selected)

- Notion mirror configuration source: `<existing project/private integration configuration, or Not Configured>`

The selected configuration declares the exact destination URL/type and either
the parent-page title pattern or required data-source property mappings.
Keep private destinations in an existing private configuration source. The
mirror skill specifies the required fields, verifies the actual destination,
and owns the requested write; credentials stay with the connector. An individual
experiment's mirror URL and result stay in that experiment record.

Read root `AGENTS.local.md` when selected host/path or private configuration
overrides are present. Overrides must remain within project policy and actual
permissions; they do not authorize execution or external publication.
