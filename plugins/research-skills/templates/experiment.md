---
title: "<experiment title>"
experiment_id: "exp-YYYYMMDD-HHMMSS-<topic>"
status: "Planned"
created_at: "<ISO 8601 timestamp with UTC offset>"
updated_at: "<ISO 8601 timestamp with UTC offset>"
---

# Motivation

---

**Key point:** <the current scientific question and why this inquiry is worth pursuing>

- Observations or user-provided cues that motivated the inquiry and what remains unexplained:
- Direct prior research or official sources and how this experiment differs:

# Hypothesis

---

**Key point:** <the provisional hypothesis or exploratory question; state what is still undefined>

- Linked cues and their conditions:
- Proposed relationship or mechanism, when there is one:
- Added assumptions, competing explanations, and unexplained cases:
- Observations that could develop or distinguish the explanation:
- Predeclared decision criterion, if justified:

# Expected Result

---

**Key point:** <what this attempt is intended to reveal, with expectations only where justified>

- Essential observations, measurements, and comparisons:
- Supporting diagnostics and the uncertainty each addresses:
- Expected patterns, if justified, and genuinely unknown outcomes:
- Conditions covered by the intended generalization and conditions not yet tested:

# Experiment

---

**Key point:** <the current phase, verification question, execution scope, and status>

## Setup

**Key point:** <the subject, comparison conditions, and effective settings needed to interpret results>

### Identity and isolation

- Primary execution repository: `<actual repository identifier for this execution>`
- Base branch: `<configured base branch or None>`
- Start SHA: `<full SHA>`
- Experiment branch: `None | <actual branch selected by the project's Git workflow>`
- Worktree: `None | <absolute path recorded for local reproducibility>`
- Current SHA: `<full SHA>`
- Working tree: `clean | dirty`
- Spec/change record: `N/A | <identifier and link>`

For additional code inputs or executions, retain each repository's role and
actual revision/snapshot, and the environment used when executing it. Omit
this table when the primary repository is the only code input.

| Repository | Role in the experiment | Revision or snapshot | Execution environment, if used |
| --- | --- | --- | --- |
| <actual repository> | <reference, baseline, implementation or other contribution> | <actual identity> | <environment reference or not executed> |

### Lineage and setup inheritance

- Branch parent: `None | <Experiment ID and document link>`
- Setup parents: `None | <Experiment ID and document links>`
- Children: `None | <Experiment ID and document links>`
- Related evidence: `None | <actual links>`
- Inherited settings: `None | <key, value, and source link>`
- Conflicts and overrides: `None | <key, source values, selected value, reason, expected effect>`
- Unresolved settings: `None | <key and reason it Needs Confirmation>`

### Scientific setup

- Phase: `<current execution or analysis phase; pilot and expansion are optional>`
- Model and checkpoint, if relevant:
- Dataset, version, split, preprocessing, and evaluation quantity:
- Hardware, precision, and distributed topology:
- Software and code identity:
- Hyperparameters, seeds, context length, and procedure:
- Comparison groups, measurement unit, and aggregation:

### Question and protocol history

| Version and timing | Question, hypothesis, or protocol change | Triggering evidence or reason | Effect on comparisons and claim scope | Protocol or prior-version link |
| --- | --- | --- | --- | --- |

Preserve earlier expectations and protocols. Identify post-observation changes;
record actual preregistration only when it exists. Revisions can stay in this
record, and unresolved questions do not require a terminal verdict.

### Pilot observations and budget, if requested

- Representative condition and selection reason:
- Intended observations and predeclared gate, if any:
- Authorized runs or adaptive execution boundary:
- Estimated wall-clock and compute cost:
- Informative next observations and resource stop boundary:

### Glossary

| Agreed term or symbol | Exact definition, formula, unit, denominator, aggregation | Code correspondence | Agreement source |
| --- | --- | --- | --- |

## Experiment

**Key point:** <the scientific protocol executed, current progress, and material deviations>

### Procedure

1. <the attempt's purpose, current protocol version, and existing entrypoint or analysis step>

### Run ledger

| Attempt/run | Protocol version | Conditions and seed, if applicable | Command/config or analysis | Artifact/log | Validity and observations | Actual resource use |
| --- | --- | --- | --- | --- | --- | --- |

### Pilot review and decision, if performed

- Raw result:
- Validity review:
- Pilot gate classification, if a gate exists: `N/A | Pending | SUPPORTED | REJECTED | INVALID | INCONCLUSIVE`
- Exploratory findings and unexpected reactions:
- Which judgment changed, or why the observation was inconclusive:
- Scope of the decision and evidence still needed for a broader claim:
- Reviewer: `assistant | user`
- Next action and reason; user decision when one is needed beyond the current scope:

### Expansion approval, if requested

- Proposed additional runs, time, and compute:
- Early-stop condition or resource boundary:
- Approval: `Not Requested | Pending | Approved | Declined`
- Approved scope and timestamp:

### Execution record

- Actual steps, protocol versions, and material deviations:
- Reproducibility metadata, paths, logs, and artifacts:
- Result artifact provenance: <evidence linking result files to the claimed run, model, data, and settings, or unverified links and their limits on the conclusion>
- Failed, invalid, skipped, and unmeasured items with their reasons:

# Experiment Result

---

**Key point:** <the conditions verified, primary observation, and current judgment>

## Results

**Key point:** <the most important result actually measured and its comparison conditions>

- Primary measurements, effect size, and uncertainty:
- Decision-relevant table or figure and what it establishes:
- Missing or invalid measurements and their effect on the claim:

## Analysis

**Conclusion:** <the current finding or uncertainty, its evidence scope, and the conditions actually examined>

- Expected and unexpected observations, when an expectation was recorded:
- Useful patterns, negative findings, and unexplained exceptions:
- Changed, retained, or abandoned explanations and the evidence behind that judgment:
- Limitations that change the conclusion:

- Observation → interpretation → decision or design implication:
- Pilot gate outcome versus scientific inference, when a gate was specified:
- Alternative explanations and confounders:
- Evidence dependencies, conflicts, and claim boundary:
- Conditions actually tested and untested generalization:
- Open research cues and the reason for the next inquiry or for shelving it:
- Record closure, if requested: <work finished within the declared scope, remaining scientific questions, and any linked follow-up>
