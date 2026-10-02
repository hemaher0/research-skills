---
name: notion-mirror
description: Use when the user explicitly requests mirroring a completed local AI/ML experiment document to its configured Notion destination. Not for experiment completion, report writing, or result investigation alone.
---

# Notion Mirror

Mirror a local experiment document only when the user requests this action and
the document has reached `Completed`. Completing an experiment does not trigger
publication. The local Markdown file remains the source of truth; the Notion
page receives a complete mirror after the local document's final review.
`Completed` describes the local record's scoped work and review, not resolution
of every hypothesis. Preserve its open questions, negative findings, and
provisional conclusions in the mirror.
Read the completed record directly; running the `experiments` skill is not a
prerequisite. Add mirror metadata to the document's YAML frontmatter only when
the mirror is requested.

Route local experiment-record metadata edits through an available document
router, passing the status rules below; the Notion page operation remains this
skill's responsibility. Follow the project's work-history capture policy.
When it calls for a work-item update, preserve the mirror request, destination,
result, source link, and next action there too. A configured storage location
does not enable capture; selective or disabled capture does not prevent the
requested mirror or its required experiment metadata. If no router is
available, use project instructions and the
configured experiment template and location for record edits, plus the local
`.docs-schema` when present and ordinary file tools for a configured work-item
trace. Do not create another work-item history or experiment record for the
mirror.

## Destination contract

Resolve the Notion mirror configuration from effective project instructions
and their designated integration source. Read a selected private configuration
override in `AGENTS.local.md` when present. Use the established project
configuration unless a completed authorized override selects another source.
A placeholder is not a selected destination. Required destination values must
resolve from actual inline fields or a verified existing configuration source.
An unused integration is a project feature choice; an unknown destination is
incomplete configuration, not a disabled feature. Installation follows the
source README; mirroring consumes settings rather than initializing them.
Use existing configured destination fields without copying or silently moving
them during installation. The selected configuration declares the exact
destination URL/type and applicable title/property mappings; credentials stay
with the connector. A private override must respect the project's storage and
publication boundary, and cannot authorize a mirror or choose another audience.
The destination identifies where experiment
pages belong; the current record's `notion_url`, when present, identifies the
page to update. Fetch the destination immediately before writing and check its
current structure and access.

For a data source, require the configured title, Experiment ID, and Completed
status property mappings. Check them against the current data-source schema and
use only configured, supported category and relation properties. For a parent
page, require an unambiguous direct-child title pattern containing the exact
Experiment ID. Do not assume a parent page supports custom properties or a
data-source schema.

When the configuration is absent, record `notion_sync_status: Not Configured` in
the local document and leave its scientific status as `Completed`. When the
configured destination is unavailable, record `notion_sync_status: Failed` with
the reason and preserve any previous URL or verification timestamp. Do not
choose another workspace, personal page, or inferred destination.

## Create or update once

Set `notion_sync_status: Pending` in the local source before the attempt. If
`notion_url` is present, fetch that exact page and verify that it belongs to
the configured destination before updating it. Stop on a destination mismatch
rather than moving or overwriting an unrelated page. Otherwise inspect the
configured data-source entries by their Experiment ID property, or the
configured parent page's direct children by the exact ID parsed from their
titles according to that pattern. Update a unique match; create a page only
when no exact match exists. Stop on ambiguous matches instead of creating a
duplicate.

Send the entire completed document, excluding local YAML frontmatter or any
heading that the destination itself renders as its title. Preserve section
order, terminology, equations, tables, figures, citations, lineage links,
conclusions, and claim boundaries. Do not create a summary-only or
independently edited Notion version. Do not reverse-sync Notion edits into the
local source unless the user asks for that separate operation.

For a data source, use only properties declared in that selected configuration and
confirmed in the fetched schema. Map `Completed` to the configured Notion
status. Populate relation properties only when their pages already exist and
the local links identify them unambiguously; never create another experiment
page solely to fill a relation. For a parent page, use the configured child
title pattern and mirror the document body without inventing custom properties.

## Verify the mirror

Fetch the saved page and compare its destination, Experiment ID, title,
configured property values where applicable, hierarchy, primary numeric
values, terminology, equations, tables, figures, links, and conclusion with the
local source. Use an available rendered-page view to check that inline and block
LaTeX display correctly. A matching source payload does not prove correct
rendering.

If repair is needed, update the same page and verify it again. Set
`notion_sync_status: Synced`, `notion_url`, and `notion_last_verified_at` in the
local document only after verification succeeds. If rendered verification is
impossible, record that limitation and do not claim full mirror verification.
