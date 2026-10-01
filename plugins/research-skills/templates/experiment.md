---
title: "<experiment title>"
experiment_id: "exp-YYYYMMDD-HHMMSS-<topic>"
status: "Planned"
created_at: "<ISO 8601 timestamp with UTC offset>"
updated_at: "<ISO 8601 timestamp with UTC offset>"
---

# Motivation

---

**Key point:** <the scientific problem to resolve and why this experiment is needed>

- Observations that motivated the experiment and what remains unexplained:
- Direct prior research or official sources and how this experiment differs:

# Hypothesis

---

**Key point:** <one falsifiable hypothesis with the subject, comparison conditions, and expected direction>

- Possible mechanism:
- Observations that would refute the hypothesis:
- Decisive gate frozen before inspecting results:

# Expected Result

---

**Key point:** <which observations would support, refute, or leave the hypothesis unresolved>

- Minimum primary metrics and comparison criteria:
- Supporting diagnostics and the alternative explanation each would rule out:
- Expected patterns and uncertainty:
- Conditions covered by the intended generalization and conditions not yet tested:

# Experiment

---

**Key point:** <the current phase, verification question, execution scope, and status>

## Setup

**Key point:** <the subject, comparison conditions, and effective settings needed to interpret results>

### Identity and isolation

- Repository: `<repository-relative or configured identifier>`
- Base branch: `<configured base branch or None>`
- Start SHA: `<full SHA>`
- Experiment branch: `None | experiment/<Experiment-ID>`
- Worktree: `None | <absolute path recorded for local reproducibility>`
- Current SHA: `<full SHA>`
- Working tree: `clean | dirty`
- Spec/change record: `N/A | <identifier and link>`

### Lineage and setup inheritance

- Branch parent: `None | <Experiment ID and document link>`
- Setup parents: `None | <Experiment ID and document links>`
- Children: `None | <Experiment ID and document links>`
- Related evidence: `None | <actual links>`
- Inherited settings: `None | <key, value, and source link>`
- Conflicts and overrides: `None | <key, source values, selected value, reason, expected effect>`
- Unresolved settings: `None | <key and reason it Needs Confirmation>`

### Scientific setup

- Phase: `Planning | Pilot | Running | Awaiting Decision | Awaiting Expansion Approval | Expanded | Analysis`
- Model and checkpoint:
- Dataset, version, split, preprocessing, and evaluation quantity:
- Hardware, precision, and distributed topology:
- Software and code identity:
- Hyperparameters, seeds, context length, and procedure:
- Comparison groups, measurement unit, and aggregation:

### Pilot gate and budget, if requested

- Representative condition and selection reason:
- Frozen gate:
- Planned pilot runs: `N/A | <number, maximum 4 total>`
- Estimated wall-clock and compute cost:
- Expansion, revision, and stop observations:

### Glossary

| Agreed term or symbol | Exact definition, formula, unit, denominator, aggregation | Code correspondence | Agreement source |
| --- | --- | --- | --- |

## Experiment

**Key point:** <the scientific protocol executed, current progress, and material deviations>

### Procedure

1. <existing entrypoint and frozen experimental step>

### Run ledger

| Run | Phase | Condition and seed | Command/config | Artifact/log | Outcome | Counts toward pilot budget |
| --- | --- | --- | --- | --- | --- | --- |

### Pilot review and decision, if performed

- Raw result:
- Validity review:
- Pilot gate classification under selected conditions: `N/A | Pending | SUPPORTED | REJECTED | INVALID | INCONCLUSIVE`
- Scope of the decision and evidence still needed for a broader claim:
- Reviewer: `assistant | user`
- Next action and user decision:

### Expansion approval, if requested

- Proposed additional runs, time, and compute:
- Early-stop gate:
- Approval: `Not Requested | Pending | Approved | Declined`
- Approved scope and timestamp:

### Execution record

- Actual steps and deviations from the frozen plan:
- Reproducibility metadata, paths, logs, and artifacts:
- Result artifact provenance: <evidence linking result files to the claimed run, model, data, and settings, or unverified links and their limits on the conclusion>
- Failed gate and reason skipped items are `SKIPPED` or `NOT_APPLICABLE`:

# Experiment Result

---

**Key point:** <the conditions verified, primary observation, and current judgment>

## Results

**Key point:** <the most important result actually measured and its comparison conditions>

- Primary measurements, effect size, and uncertainty:
- Decision-relevant table or figure and what it establishes:
- Missing or invalid measurements and their effect on the claim:

## Analysis

**Conclusion:** <a scoped conclusion stating the pilot or expanded evidence stage and conditions actually verified>

- Observations consistent with prior expectations and their evidence, or why they cannot be assessed:
- Observations differing from prior expectations and their evidence, or why they cannot be assessed:
- Benefits established against the experiment's goal, or why they cannot be assessed:
- Limitations established against the experiment's goal, or why they cannot be assessed:

- Observation → interpretation → decision or design implication:
- Pilot gate outcome versus scientific inference, if pilot evidence was used:
- Alternative explanations and confounders:
- Evidence dependencies, conflicts, and claim boundary:
- Conditions actually tested, untested generalization, and user-decided next step:
