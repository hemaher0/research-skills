---
name: report
description: Use when interpreting existing AI/ML research evidence or writing a research report, with or without an experiments record. Not for launching a new pilot or experiment merely because evidence is incomplete.
---

# Report

Read the supplied results and their primary artifacts before drawing a
conclusion. An existing experiment record is optional. Use the requested output
format; for an investigation or answer request, respond in the conversation.
Create or update a local document only when that artifact is requested. Do not
create a branch, worktree, experiment record, new run, or Notion page as a
prerequisite to reporting.
When project instructions configure work items, preserve the request,
interpretation, evidence links, uncertainty, and next action there. Use an
available document router for the update; if none is available, use project
instructions, the local `.docs-schema` when present, and ordinary file tools.
This trace does not create a separate experiment record.
During parallel work, record independent tasks in separate linked child work
items when the local schema supports them. Return each child path and its
interpretation, evidence, uncertainty, and next action to the coordinator.
Give a shared report one writer; under an older work-item schema, also give
the work item one writer and hand off the events. This applies even when no
document router is installed.
For a requested document, use an available document router for placement,
writing, and review, passing the evidence and claim rules below. If none is
available, follow the repository's document conventions with ordinary file
tools. This skill remains responsible for scientific interpretation.

## Evidence and claims

Resolve numeric values and the primary conclusion from the actual artifacts,
not conversation memory. When sources conflict, show the conflict and leave
the conclusion unresolved. Do not substitute an expected value or zero for an
unmeasured result, or retrospectively present a hypothesis as preregistered.

Separate observed results, compatible interpretations, decisions or design
implications, and limitations. Identify shared assumptions across related
metrics and repeated samples. Match the claim to the measured models, data,
seeds, conditions, and evidence; correlational or surrogate evidence alone does
not establish a causal or downstream claim. Define nonstandard terms and
metrics by formula or operational meaning, aggregation, denominator, baseline,
direction, and unit when relevant.

For a supplied or reused result artifact, distinguish a valid calculation from
evidence that the artifact came from the claimed source. Check available run,
export, or source-system evidence linking it to the model or intervention, data,
configuration, and execution. Matching sample IDs and correctly calculated
metrics do not establish that link. If the link is unverified, report the
calculation as conditional on the supplied artifact, leave source-level claims
unresolved, and carry that uncertainty into any linked work item. Accept the
project's available provenance evidence; do not require one particular log,
manifest, checksum, or signature format.

When the evidence comes only from a pilot, distinguish the pilot-gate outcome
from the broader hypothesis and state the tested conditions and untested scope.

If the supplied evidence cannot settle the question, report what remains
unknown and what observation would resolve it. Do not run a pilot or create
persistent analysis code without a separate execution or implementation request.
Start with the available results and direct calculations. Use an existing
analysis tool when a calculation actually needs one; do not add repository code
merely to format or restate a small result.

## Output

Lead with the conclusion or its current uncertainty. Include only the methods,
measurements, provenance, alternatives, and limitations needed to understand
that conclusion. A compact table may help when it clarifies a comparison.
Represent failed, invalid, skipped, and unmeasured items accurately.
When a result artifact's claimed source is unverified, lead with that uncertainty
and phrase comparisons as conditional on the artifact. Do not present the claimed
model or intervention as better or deployment-ready in the headline, conclusion,
or recommendation based on that artifact alone.

When the request explicitly updates a managed experiment record, read
[the experiment reporting rules](../experiments/SKILL.md#analysis-and-final-reporting) and
preserve that record's structure. Those record-specific section and metadata
requirements do not apply to a standalone answer or report. Notion
synchronization is a separate requested action.

If the user also explicitly asks to update reader-facing repository
documentation from the findings, use an available document router. Otherwise
follow the repository's documentation conventions with ordinary file tools.
