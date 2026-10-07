---
name: pilot
description: Use when planning or running a bounded AI/ML research pilot to obtain new evidence under representative conditions. Works without an experiments record. Not for inspecting existing results, routine software tests, or code changes alone.
---

# Pilot

A pilot obtains new evidence for a bounded research question under the
representative conditions that question requires. Its scope can be narrow while
its model, data, scale, and execution duration remain substantial. It can stand
alone or belong to an existing managed experiment. Planning does not authorize
execution; run when the user's request includes it, using the project's
execution policy and entrypoints.

Follow the project's work-history capture policy. When it calls for a work-item
update, preserve the covered requests and discussions, protocol, run evidence,
classification, and next action there. A configured storage location does not
enable capture; selective or disabled capture does not prevent authorized
pilot work or its required evidence.
Use an available document router for the update; if none is available, use
project instructions, the local `.docs-schema` when present, and ordinary file
tools. This work-item trace is separate from an optional managed experiment
record.

## Optional companions

Before following a link to another skill, check the current host's available
skills list and its applicable scope. Read/invoke its actual listed installed
path and name; links here identify the companion, not a source to load instead.
A source or cache file alone does not make that skill available. Use listed companions only when useful; otherwise
perform this skill's method below with project procedures and ordinary tools.
Do not read an unavailable skill or its templates, install it automatically,
route back in a loop, or weaken the required outcome because it is absent.

## Scope before execution

- Connect each consequential condition to the scientific purpose and
  applicable evidence; identify unresolved premises, consequences and the
  observations needed before dependent work. State which premises this attempt
  examines. An available [evidence-based-research](../evidence-based-research/SKILL.md#ground-consequential-choices)
  can help; apply these checks directly without it.
- State the question, the reason for this attempt, representative conditions,
  and what will be observed. Include the working hypothesis and an expectation
  when justified; exploratory observations can precede a clear hypothesis.
- Select essential comparisons and measurements. Establish the run count or
  adaptive execution boundary, wall time, and compute budget from project
  policy and the user's authorized scope.
  Include failed and invalid attempts in actual resource accounting.
- Decide what would make further execution useful, unnecessary, or out of scope.
  Keep any predeclared decision criterion unchanged for the runs it governs;
  record a revised criterion as a new, dated comparison. Stop at the authorized
  boundary or when further attempts would not inform the selected question.
- Use the real model, checkpoint, data, planned evaluation quantity, procedure,
  precision, hardware, and distributed topology for the selected condition.
  Narrow comparisons before changing the scale needed for the phenomenon.
  Preserve required replications and measurements as well. Toy data or an
  arbitrarily shortened run is a software check, not representative pilot
  evidence. A naturally short process is valid when it covers the phenomenon.

## Keep actions separate

Before a costly pilot, inspect its actual computation/data path for avoidable
repeated work, movement or serialization. Reuse applicable profiles or obtain
bounded matched-workload timings when needed. Correct evidenced inefficiencies
within authority while preserving the scientific procedure; verify affected
outputs/numerics and training gradients or updates, repository checks, and
claimed time/memory effects under matched conditions. An available
[evidence-based-research](../evidence-based-research/SKILL.md#check-implementation-efficiency-before-costly-execution)
can help; this check still applies without it. Preserve representative
conditions; performance checks do not substitute for scientific observations.

Use existing runnable capabilities when they satisfy the protocol. Necessary
bounded implementation or preparation can proceed within the authorized goal,
representative conditions and resource budget through the responsible
development/environment workflow. Verify that preparation before relying on
its results and record material effects on the protocol. Existing authorization
covers necessary prerequisites within that scope.

Resolve a missing essential input or authority before dependent execution.
A change to the agreed scientific question, comparisons, interpretation-critical
conditions or resource scope needs the appropriate decision before that run.
Do not substitute a different phenomenon or an arbitrary toy/shortened condition
to make an unavailable capability appear covered.

Do not create an experiment record, report file, branch, worktree, or Notion page
solely because this skill is active. Use an existing record when the user asks to
update it. Create a persistent document only when requested; otherwise report
the protocol, evidence, and decision in the conversation and configured work
item. A worktree requires a
concrete isolation need, such as conflicting changes or outputs that would
contaminate the current checkout. Keep necessary run outputs in the project's
configured artifact location.
For a requested persistent document, use an available document router for
placement, writing, and review, passing the pilot protocol and evidence limits
below. If none is available, follow the repository's document conventions with
ordinary file tools.

## Review the evidence

Check the protocol, existing implementation, environment, inputs, controls, and
measurements before treating a raw failure as scientific rejection. Record run
validity separately from the scientific interpretation. Use
[interpretation](../interpretation/SKILL.md) when available to analyze valid
observations. Without it, verify artifact provenance and metric definitions,
compare effects/variation and alternatives, and separate observed results,
gate decisions and scoped scientific claims using the rules below.
Assess whether the observations answer the pilot's question. An execution check
or initial change does not establish an unexamined premise. Preserve that gap
when planning follow-up work, including when execution is already authorized;
resolve it before dependent work treats it as established.

When a pilot has a predeclared decision gate, record its outcome under the
selected conditions using the project's classification or these labels:

| Classification | Meaning |
| --- | --- |
| `SUPPORTED` | Valid evidence passes the stated gate under the selected conditions. |
| `REJECTED` | Valid evidence fails the stated gate under the selected conditions. |
| `INVALID` | Run, input, environment, or measurement is defective. |
| `INCONCLUSIVE` | Valid evidence cannot decide the gate. |

For an exploratory pilot without such a gate, report the observed pattern,
uncertainty, and what it makes worth examining next; do not manufacture a binary
verdict. Preserve prior expectations and protocol versions. Report failed,
skipped, and unmeasured items accurately.

Any classification records a pilot-gate decision, not a general verdict on the
hypothesis. Report the conditions tested, unexpected reactions, important
untested conditions, and alternative explanations.

For an invalid run, repair a demonstrated defect and rerun only when both are
within the existing implementation and execution scope. Further informative
attempts within the agreed conditions and budget can continue without repeated
approval. An available [evidence-based-research](../evidence-based-research/SKILL.md) can
help choose the next inquiry, and an available [probing](../probing/SKILL.md)
can help revise a hypothesis. Without them, identify the judgment changed by
valid observations, remaining alternatives and the next useful comparison
directly; preserve prior hypotheses and evidence. For expansion beyond the
authorized boundary, present the changed conditions, runs, time, and compute
before obtaining the required scope decision. A pilot can end with unresolved
questions and does not require a larger study.
