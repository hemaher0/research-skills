---
name: report
description: Use when presenting AI/ML research findings in a requested answer, report, or existing record. Reporting can include unresolved findings and does not require another research skill or a completed study.
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
tools. This skill owns scientific presentation. An available
[interpretation](../interpretation/SKILL.md) can guide needed analysis;
without it, verify artifact/source provenance and metric definitions, compare
valid observations and alternatives, and retain scoped claims and uncertainty
directly using the evidence rules below.

## Optional companions

Before following a link to another skill, check the current host's available
skills list and its applicable scope. Read/invoke its actual listed installed
path and name; links here identify the companion, not a source to load instead.
A source or cache file alone does not make that skill available. Use listed companions only when useful; otherwise
perform this skill's method below with project procedures and ordinary tools.
Do not read an unavailable skill or its templates, install it automatically,
route back in a loop, or weaken the required outcome because it is absent.

## Establish the account to communicate

Resolve numeric values and the primary conclusion from the actual artifacts,
not conversation memory. When sources conflict, show the conflict and leave
the conclusion unresolved. Do not substitute an expected value or zero for an
unmeasured result, or retrospectively present a hypothesis as preregistered.

If the requested conclusion has not been established, or the artifacts and
existing analysis disagree, use [interpretation](../interpretation/SKILL.md)
when available to assess evidence. Without it, perform the provenance,
measurement, comparison and alternative checks above directly. A primarily
analytical request can use that available workflow without this one first.
Preserve the distinction
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

When updating a managed experiment record, preserve its existing structure,
identity and scientific lifecycle and read the governing project/record
template. Read [the experiment reporting rules](../experiments/SKILL.md#analysis-and-final-reporting)
only when that skill is available; without it, preserve the record's section
contract, keep setup/execution details in their existing setup/run sections,
and put measurements and scoped interpretation in the result/analysis sections. Managed-experiment requirements do not
apply to standalone answers or reports; the project's applicable document
ownership, placement, format, lifecycle, and validation rules still apply.
Notion synchronization follows the project's configured trigger and existing
user authorization.

If the user also explicitly asks to update reader-facing repository
documentation from the findings, use an available document router. Otherwise
follow the repository's documentation conventions with ordinary file tools.
