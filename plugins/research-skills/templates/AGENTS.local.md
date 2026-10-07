# Local Research Configuration

<!-- Use applicable sections only when the current project needs local overrides.
Install scope does not require this file; existing project sources may already
supply all settings. Create or merge into project-root AGENTS.local.md when needed. Mark configuration complete only after required values or their
existing authoritative sources are resolved. Remove unused fields/headings. Preserve existing values
and other packages' sections. Shared locations, reproducible environment
configuration and mirror contracts stay in their existing configuration sources.
Resolve checkout, environment, wrapper, dependency and allocation facts from
Git, runtime tools and the scheduler. Keep run-specific state in its record.
Do not duplicate settings resolved elsewhere. Connect the file through existing
AGENTS.md, or a recommended AGENTS.md symlink when absent, following the source README.
Never put credentials or assertions of newly granted permissions here. -->

## Research Configuration Status

- Configuration status: `<Complete / Incomplete: identify required unresolved values>`
- Existing research settings source, when applicable: `<actual path to the authoritative research settings>`

## Local Research Locations

- Experiment document root: `<local path override, or Use Repository Default>`
- Experiment artifact root override, if needed: `<local path override, or Use Repository Default>`

## Execution environment: `<host or profile name>`

- Host or scheduler profile: `<existing host/profile reference>`
- Allocated or permitted devices, if a fixed host constraint applies: `<device IDs/UUIDs, or scheduler-managed>`

## Private Notion Configuration (when mirroring is used)

<!-- Keep either the verified existing configuration source or the required
inline values. Remove fields for the other destination type. When mirroring
is unused, omit this section; declare that feature choice in project settings. -->

- Destination configuration source: `<actual existing configuration path, or this file for inline values>`
- Destination URL: `<actual Notion URL>`
- Destination type: `<parent page / data source>`
- Child-title pattern, for a parent page: `<actual pattern containing the exact Experiment ID>`
- Data source identifier, for a data source: `<actual identifier>`
- Title property mapping, for a data source: `<actual property name>`
- Experiment ID property mapping, for a data source: `<actual property name>`
- Synchronization trigger and existing authorization: `<configured event and authorized scope; preserve existing standing authorization>`
- Category property/value, for a data source when applicable: `<actual mapping>`
- Status property and scientific-state mapping, for a data source: `<actual property name and mapping for the source states>`
