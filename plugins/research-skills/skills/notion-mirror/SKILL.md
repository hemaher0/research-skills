---
name: notion-mirror
description: Use when mirroring a local AI/ML experiment document is authorized by a user request or the project's configured synchronization policy. Not for changing scientific status or reverse synchronization.
---

# Notion Mirror

Mirror a local experiment document under the project's configured trigger and
existing authorization. A direct request can authorize a mirror; configured
automatic synchronization can supply standing authorization for new or updated
records, including ongoing ones. Respect explicit exclusions or deferrals.
Do not require another request when that authorization already covers the work.
Record completion alone does not invent an authorization or trigger.

Local Markdown remains authoritative. Read the actual record and preserve its
native scientific state, open questions, negative findings and provisional
conclusions. Do not set `Completed` just to publish it. No `experiments` skill
is required: use the record's governing project configuration, template and
ordinary file tools. Add mirror bookkeeping when an authorized sync is due.

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
with the connector. A private override must respect the project's storage/publication boundary
and record existing authority; it cannot invent a permission or audience.
The destination identifies where experiment
pages belong; the current record's `notion_url`, when present, identifies the
page to update. Fetch the destination immediately before writing and check its
current structure and access.

For a data source, require the configured title, exact record-ID, applicable category,
and native scientific-state property mappings. Check them against the current data-source schema and
use only configured, supported category and relation properties. For a parent
page, require an unambiguous direct-child title pattern containing the exact
Experiment ID. Do not assume a parent page supports custom properties or a
data-source schema.

When the configuration is absent, record `notion_sync_status: Not Configured` in
the local document and preserve its actual scientific status. When the
configured destination is unavailable, record `notion_sync_status: Failed` with
the reason and preserve any previous URL or verification timestamp. Do not
choose another workspace, personal page, or inferred destination.

## Create or update once

Set `notion_sync_status: Pending` in the local source before the attempt. For
a data source, use destination + exact record ID + configured category when
one applies as mirror identity. If `notion_url` exists, fetch it and verify
all identity fields before updating. Otherwise look up that exact identity
using complete results; update only a unique match and create only when none
exists. Preserve unrelated tags. Stop on mismatched identity, ambiguity or an
incomplete lookup; do not adopt an unrelated manually authored page.

For a parent page, verify its configured exact-ID child-title pattern and
inspect direct children completely. Apply the same unique-match/create and
stored-URL checks without inventing data-source properties.

Send the entire source document, excluding mirror-bookkeeping frontmatter
and a duplicate heading rendered as the page title. Retain source path, type,
exact ID and scientific state visibly; preserve other meaningful metadata. Preserve section
order, terminology, equations, tables, figures, citations, lineage links,
conclusions, and claim boundaries. Do not create a summary-only or
independently edited Notion version. Do not reverse-sync Notion edits into the
local source unless the user asks for that separate operation.

For a data source, use only properties declared in that selected configuration and
confirmed in the fetched schema. Map the source's actual scientific state through the verified project mapping.
Resolve an unmapped state from its native workflow rather than guessing or
changing the source state. Populate relation properties only when their pages already exist and
the local links identify them unambiguously; never create another experiment
page solely to fill a relation. For a parent page, use the configured child
title pattern and mirror the document body without inventing custom properties.

## Verify the mirror

Fetch the saved page and compare its destination, Experiment ID, title,
configured category and actual-state values where applicable, hierarchy, primary numeric
values, terminology, equations, tables, figures, links, and conclusion with the
local source. Use an available rendered-page view to check that inline and block
LaTeX display correctly. A matching source payload does not prove correct
rendering.

If the attempt fails, record `notion_sync_status: Failed` and the observed
reason, retaining the URL and previous verification time for an idempotent
retry. Keep scientific status unchanged. If repair is needed, update the same
page and verify it again. Set
`notion_sync_status: Synced`, `notion_url`, and `notion_last_verified_at` in the
local document only after verification succeeds. If rendered verification is
impossible, record that limitation and do not claim full mirror verification.
