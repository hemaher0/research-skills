# Local research configuration

<!--
Copy only the sections used by the target repository to AGENTS.local.md.
Replace placeholders with values for that repository. Keep credentials and tokens
out of this file. Repeat the execution environment section for another host
when its paths or resources differ.
-->

## Research document locations

- Experiment document root: `<absolute path, path relative to the main checkout, or Use Repository Default>`
- Experiment artifact root override, if needed: `<absolute path, repository-relative path, or Use Repository Default>`

## Execution environment: `<host or profile name>`

- Host or scheduler: `<hostname, local, cluster profile, or container name>`
- Main checkout: `<absolute path>`
- Experiment worktree root, if used: `<absolute path or None>`
- Manager and environment type: `<shared uv .venv, venv, Conda, container, module, other, or Not Configured>`
- Environment path or activation command: `<absolute path or command, or Not Configured>`
- Dependency manifest and lockfile: `<repository paths or None>`
- GPU count available for jobs: `<integer, dynamically allocated, or None>`
- Allocated or permitted devices: `<device IDs, UUIDs, MIG IDs, scheduler-managed, or None>`
- Scheduler or container allocation: `<name or None>`
- Stable GPU wrapper, if using `$run-gpu`: `<absolute path or Not Configured>`

## Notion experiment mirror

- Completed experiment destination URL: `<Notion parent-page or data-source URL, or Not Configured>`
- Destination type: `<parent page, data source, or Not Configured>`
- Destination ID, if separately available: `<Notion ID or None>`
- Parent-page child title pattern, if using a parent page: `<unambiguous pattern containing {experiment_id} and optionally {title}, or Not Applicable>`
- Data-source title property: `<property name or Not Applicable>`
- Data-source Experiment ID property: `<property name or Not Applicable>`
- Data-source status property and Completed value: `<property name and value, or Not Applicable>`
- Data-source required category properties: `<property/value mappings, or None>`
- Data-source relation properties: `<property names and directions, or None>`

The destination above holds completed experiment pages. Record each mirror
page's own URL in that experiment document's `notion_url` field.
