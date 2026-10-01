---
name: pilot
description: Use when planning or running a bounded AI/ML research pilot to obtain new evidence under representative conditions. Works without an experiments record. Not for inspecting existing results, routine software tests, or code changes alone.
---

# Pilot

A pilot is a small scientific decision, not a prerequisite for answering a
question or changing code. It can stand alone or belong to an existing managed
experiment. Planning a pilot does not authorize execution; run only when the
user's request includes execution. Use the project's existing execution policy
and entrypoints.

When project instructions configure work items, preserve every request and
discussion, protocol, run evidence, classification, and next action there.
Use an available document router for the update; if none is available, use
project instructions, the local `.docs-schema` when present, and ordinary file
tools. This work-item trace is separate from an optional managed experiment
record.

## Scope before execution

- State the question, representative condition, falsifiable hypothesis, and
  observation that would support, reject, or leave it unresolved.
- Select only the essential comparisons and measurements. The initial packet
  contains at most four training or evaluation runs in total, including failed
  or invalid launches. Do not expand it into a sweep, ablation suite, or broad
  benchmark.
- Estimate run count, wall time, and compute cost before launching. Stop when
  the decision gate is met or the budget is exhausted.
- Use the real model, checkpoint, data, planned evaluation quantity, procedure,
  precision, hardware, and distributed topology for the selected condition.
  Reduce the number of conditions, seeds, and diagnostics rather than the
  scientific scale. Toy data or a shortened run is a software check, not pilot
  evidence.

## Keep actions separate

Use existing runnable code first. A pilot request by itself does not authorize
source, notebook, test, script, dependency, or runtime configuration changes.
If the required capability is absent, identify it and stop the affected run.
If implementation is also requested, complete that separately with the smallest
working change that meets the requested condition, verify it, and then run the
pilot within the authorized execution scope. Improve that implementation only
for an observed defect or an agreed requirement.

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
measurements before treating a raw failure as scientific rejection. Classify the
pilot once:

| Classification | Meaning |
| --- | --- |
| `SUPPORTED` | Valid evidence passes the stated gate under the selected conditions. |
| `REJECTED` | Valid evidence fails the stated gate under the selected conditions. |
| `INVALID` | Run, input, environment, or measurement is defective. |
| `INCONCLUSIVE` | Valid evidence cannot decide the gate. |

Preserve the original hypothesis and gate after observing results. Do not tune a
failed candidate or try nearby conditions automatically. For additional runs,
present the proposed conditions, run count, wall time, compute cost, and stop
gate; start only when that expansion is authorized. Report failed, skipped, and
unmeasured items accurately.

The classification records a pilot-gate decision, not a general verdict on the
hypothesis. Report the conditions tested and any important untested conditions
or alternative explanations before recommending expansion or stopping.

If a run is `INVALID`, repair only the demonstrated defect and rerun within the
remaining four-run budget when that repair is in scope; otherwise report the
needed decision. A supported gate can conclude at pilot scope without expansion.
