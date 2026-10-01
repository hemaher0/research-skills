---
name: report
description: Use when presenting AI/ML research findings in a requested answer, report, or existing record. Use interpretation for result analysis; reporting does not require a completed study.
---

# Report

Communicate the current findings faithfully for the requested audience and
format. Read the evidence and any existing interpretation before presenting
them. An existing experiment record and a finished study are optional. For an
answer request, respond in the conversation.
Create or update a local document only when that artifact is requested. Do not
create a branch, worktree, experiment record, new run, or Notion page as a
prerequisite to reporting.
Follow the project's work-history capture policy. When it calls for a work-item
update, preserve the request, interpretation, evidence links, uncertainty,
and next action there. A configured storage location does not enable capture;
selective or disabled capture does not prevent the requested report. Use an
available document router for the update; if none is available, use project
instructions, the local `.docs-schema` when present, and ordinary file tools.
This trace does not create a separate experiment record.
For parallel work covered by capture policy, record independent tasks in
separate linked child work items when the local schema supports them. Return
each child path and its interpretation, evidence, uncertainty, and next action
to the coordinator.
Give a shared report one writer; under an older work-item schema, also give
the work item one writer and hand off the events. This applies even when no
document router is installed.
For a requested document, use an available document router for placement,
writing, and review, passing the evidence and claim rules below. If none is
available, follow the repository's document conventions with ordinary file
tools. This skill owns the scientific presentation; result analysis belongs to
[interpretation](../interpretation/SKILL.md).

## Establish the account to communicate

Resolve numeric values and the primary conclusion from the actual artifacts,
not conversation memory. When sources conflict, show the conflict and leave
the conclusion unresolved. Do not substitute an expected value or zero for an
unmeasured result, or retrospectively present a hypothesis as preregistered.

If the requested conclusion has not been established, or the artifacts and
existing analysis disagree, use [interpretation](../interpretation/SKILL.md)
to assess the available evidence. A request to analyze results primarily routes
there; it does not need a report workflow first. Preserve its distinction
between observations, explanations, implications, and unresolved claims, along
with evidence dependencies, definitions, and tested conditions.

Retain provenance limits in the headline and conclusions. When a result's
claimed source is unverified, present calculations as conditional on that
artifact rather than attributing improvement to its claimed model or run.

When the evidence comes only from a pilot, distinguish any specified gate
outcome from the broader hypothesis and state the tested conditions and
untested scope. An exploratory pilot may have observations without a gate.

If the evidence cannot settle the question, report the current uncertainty and
the observation that could clarify it. Preserve changes of question or
explanation and their reasons when they help the audience understand the
findings. No new run or repository analysis code is needed merely to make the
report sound conclusive.

## Output

Lead with the conclusion or its current uncertainty. Include only the methods,
measurements, provenance, alternatives, and limitations needed to understand
that conclusion. A compact table may help when it clarifies a comparison.
Represent failed, invalid, skipped, and unmeasured items accurately.
Match terminology, numerical values, links, and claim scope to the source
artifacts after writing. Keep limitations in the main account wherever they
change its conclusion. An unresolved question, discarded explanation, or
unexpected result can be the central finding; a polished success narrative is
not required.

When the request explicitly updates a managed experiment record, read
[the experiment reporting rules](../experiments/SKILL.md#analysis-and-final-reporting) and
preserve that record's structure. Those record-specific section and metadata
requirements do not apply to a standalone answer or report. Notion
synchronization is a separate requested action.

If the user also explicitly asks to update reader-facing repository
documentation from the findings, use an available document router. Otherwise
follow the repository's documentation conventions with ordinary file tools.
