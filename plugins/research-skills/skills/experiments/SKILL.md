---
name: experiments
description: Use when creating or continuing a persistent AI/ML experiment record and managing its protocol, lineage, execution state, and evidence. Not for standalone result investigation, a standalone pilot or report, or design discussion without a requested record.
---

# Experiments

Manage one requested, persistent experiment record. Its local Markdown document
holds the plan, execution history, and final analysis. A question about existing
results, a pilot, or a report does not require this record. Do not create one
unless the user asks to manage the experiment over time or requests a durable
experiment document.

Separately, if project instructions configure a canonical work-item repository,
preserve every request and discussion, protocol decision, experiment link,
evidence, code SHA, and next action there. Check whether a compatible
document-routing skill is actually available before using it; no named router
is a prerequisite. A router handles work-item and experiment-document file
operations; this skill owns the experiment's scientific content, template,
configured root, and lifecycle. If no router is available, use project
`AGENTS.md`, the local `.docs-schema` when present, and ordinary file tools.
The work item does not replace this experiment record.
When parallel agents run independent research tasks, give each a linked child
work item if the local schema supports one; each agent records its own timeline
and returns its path, protocol decisions, evidence, and code SHA. The
coordinator owns the root and shared Git integration. An experiment document
still has one scientific writer when several agents contribute to it. Under
an older work-item schema, send timestamped handoffs to one record writer.
Apply the same ownership rules when no document router is installed.

## Configuration and boundaries

Read applicable repository and local instructions before creating or continuing
a record. Use their document and artifact locations, terminology, execution
resources, and optional spec/change system. Do not infer a repository, server,
or worktree root from another project.

One experiment has one code repository. Its document may live in the configured
project or separate document repository; that location does not authorize
reading or executing code from a second code repository. Keep the work item and
experiment record linked without treating them as the same document.

This skill owns the research protocol, evidence, and record lifecycle, not implementation. Do not create, modify,
or delete source code, notebooks, tests, experiment scripts, dependencies, or
runtime configuration as a side effect of managing it. Use existing entrypoints
for authorized execution. If a required capability is missing, record the
prerequisite and stop the affected execution. Handle an explicitly requested
implementation as a separate task.

Creating a record does not authorize training, evaluation, publication, or a
separate branch or worktree. Execute only when the request includes
execution. Create isolation only for a concrete conflict, project requirement,
or operation that would contaminate the current checkout. Use the target
repository's GPU execution policy when CUDA is required.

## Related skills and template

For a new record, use [the experiment template](../../templates/experiment.md).
The lifecycle and reporting rules for a managed record are below.
For requested record creation, updates, placement, or review, use an available
document-routing skill. Pass it the template, configured location, lifecycle
state, scientific contract, and authorization boundary below. If none is
available, follow the repository's document conventions with ordinary file
tools. Do not make a documentation plugin a prerequisite for the record.

When a bounded preliminary run is requested, use the independent
[pilot skill](../pilot/SKILL.md). A pilot can run without this record; when both
are requested, place its decisions and evidence in the existing record.

A standalone interpretation or report uses the independent
[report skill](../report/SKILL.md) and need not create or update an experiment
record.

If the request separately includes an update to reader-facing repository
documentation, use an available document router; otherwise follow the
repository's documentation conventions and ordinary file tools. Do not infer
a documentation update from the experiment alone.

## Scientific contract

- Define one central question and a falsifiable hypothesis. Separate the expected
  observation, possible mechanism, decisive gate, alternative explanations, and
  confounders before execution.
- Use the minimum metrics and comparisons needed to decide the hypothesis. Mark
  each additional analysis as primary evidence or a diagnostic observation.
- Read direct primary research or official experimental material when the design
  depends on prior work. Link the relevant claim, equation, figure, or protocol and
  state what is reused or changed. Mark unsupported methods as original proposals.
- Do not revise a preregistered hypothesis or gate after seeing results. Record a
  new idea as post-observation and leave it for a user-decided revision or child
  experiment.
- Treat a pilot classification as a decision about its preregistered gate under
  the selected conditions. Check run validity, gate outcome, and strength of the
  scientific inference separately. A passed gate can justify a next step without
  establishing robustness, mechanism, or generality; a failed gate under limited
  conditions does not by itself refute the hypothesis everywhere.
- Distinguish observations, interpretations, implications, and untested claims.
  Match conclusion strength to the measured conditions and dependent evidence.
- For supplied or reused result artifacts, verify the link to their claimed
  source before attributing values to a model, run, dataset, or intervention.
  Record the supporting run or export evidence, or mark the link unverified.
  Structural validity and correct scoring establish only properties of the
  supplied artifact. When origin is unverified, make artifact-level calculations
  conditional, leave source-level claims unresolved, and forward the missing
  evidence to the linked work item. A completed artifact audit can still have
  an unresolved source-level question.
- A record may finish with pilot-only evidence. Mark the conclusion as limited to
  that pilot, name the conditions and important untested alternatives, and state
  what further evidence would be needed for a broader claim. Do not run an
  expansion merely to make the report sound conclusive.
- Use the user's language for connective prose. Preserve established field terms,
  code identifiers, metric names, mathematical notation, filenames, and commands.

## Local source and completion

Choose the experiment-document root from the local `AGENTS.local.md` setting
when it specifies a path, then the repository default in `AGENTS.md`. Resolve a
relative document path from the main checkout, never from an isolated code
worktree; use an absolute path as written. Use the same precedence for an
experiment artifact root when the local file specifies an override. When
neither file specifies a document root,
use:

```text
references/experiments/YYYY-MM-DD-<topic>/YYYY-MM-DD-<topic>-experiment.md
```

Start from the experiment template and preserve its H1/H2 hierarchy. Update the same
file for the requested phases and final analysis. A pilot is optional; do not
fill unperformed phases with fabricated evidence. Do not create a second local
report solely because the record is complete.
Use the dated filename above for new records in either the default or
configured document root unless the project explicitly sets another filename
convention. Keep an existing `experiment.md` at its current path; do not
rename it automatically. A configured root remains authoritative. Pass the
resolved root and filename to an available document router for file operations.
A code branch or worktree never creates a document branch or moves
the record into the code worktree; retain it at the configured document root.
If that root resolves inside an isolated code worktree, report the configuration
conflict before writing there.

## Experiment lifecycle

### Identity and states

Create one immutable identifier in this form, using local time with its UTC offset
in the document metadata:

```text
exp-YYYYMMDD-HHMMSS-<topic>
```

When a branch or worktree is needed, name it with that identifier:

```text
branch:   experiment/<Experiment-ID>
worktree: <configured-worktree-root>/<Experiment-ID>
```

Use these document states:

| State | Meaning |
| --- | --- |
| `Planned` | Protocol is frozen; no training or evaluation has started. |
| `Running` | Authorized execution is in progress without a separate pilot phase. |
| `Pilot Running` | An explicitly requested bounded pilot is in progress. |
| `Awaiting Decision` | Pilot evidence requires a user decision before more execution. |
| `Awaiting Expansion Approval` | Pilot passed and the larger budget has not been approved. |
| `Expanded Running` | The approved post-pilot experiment is in progress. |
| `Completed` | Evidence and final analysis are complete. |
| `Stopped` | The user ended the experiment without completing the planned evidence. |

Do not insert a pilot merely to move between `Planned`, `Running`, and `Completed`.

### Create or continue the record

Resolve the repository, configured document root, intended path, and current
code identity before routing a document update. Check for an existing record
with the same ID or subject and continue it when appropriate. Use the current
suitable checkout unless a concrete isolation need is present. Record the
current branch, SHA, timestamps
with UTC offset, and dirty state. Record `None` for a branch or worktree created
specifically for this experiment when there is none. If the repository defines a
spec/change system, follow its actual policy; otherwise record `N/A`.

Create a branch or worktree only when the user or repository requires one, or
when conflicting changes, parallel work, or output contamination make isolation
necessary. Before mutating Git, resolve the main checkout, base/start SHA,
worktree root, target branch, and target path. Verify the branch and path do not
already exist and that the worktree root is ignored. Do not stash, commit, reset,
move, or copy unrelated changes. When isolation is needed, use the experiment ID
to name the branch and worktree, then record their actual paths and SHA.

For a root experiment, resolve the configured base branch to the start SHA.
For a child with a branch parent, use that parent's committed tip; if its
worktree is dirty, resolve that state before deriving the child. Never copy
uncommitted parent changes. If the worktree root is not ignored, add its
repository-relative path to the main checkout's local `.git/info/exclude`
instead of editing tracked `.gitignore`. Create the optional worktree with no
upstream:

```bash
git -C <main-checkout> -c branch.autoSetupMerge=false worktree add \
  -b experiment/<Experiment-ID> \
  <configured-worktree-root>/<Experiment-ID> \
  <start-SHA>
```

Do not add or change remotes, fetch, pull, push, set an upstream, open a PR,
merge, or delete the branch/worktree without that separate request. If creation
fails or is interrupted, re-read the document, branch, path, and registered
worktree state before retrying. Clean up only resources certainly created by the
current attempt and only while still unmodified; otherwise preserve and report
the partial state.

### Continue an experiment

Locate an existing experiment by its exact ID, document path, or recorded
branch/worktree. Require discovered identifiers to agree. Do not create a second
document or worktree when a record is incomplete or starts another phase.
Refresh timestamps, current SHA, and dirty state after a meaningful update.
When a linked code branch merges or is abandoned, record its actual final SHA,
outcome, and evidence in this experiment record and forward the event to the
configured work item. Keep the document at its existing path; use the
experiment lifecycle and project instructions to settle its state.

### Parent, child, and related evidence

- A **branch parent**, when branches are used, supplies the Git start commit.
  At most one is allowed.
- A **setup parent** supplies configuration values to the current experiment.
- A **child** inherits setup from the current experiment.
- A **related document** supplies rationale or evidence without setup inheritance.

Classify each link once according to setup inheritance. Compare nested setup at the
lowest meaningful key, such as `parameters.batch_size`. Inherit a missing value
only when all setup parents agree. A value explicitly declared by the child wins,
but record the override as a conflict. When setup parents disagree and the child
does not declare a value, record `Needs Confirmation` and ask the user rather than
using list order.

A child without a new branch can still inherit setup from a parent record.

For every inherited or conflicting value, record the key, values, source links,
selected value, reason, and expected effect. Keep actual links to branch parents,
setup parents, children, and related documents in the experiment record.

## Analysis and final reporting

### Evidence and claims

Resolve the primary conclusion and numeric values from actual artifacts rather than
conversation memory. If primary sources conflict, expose the conflict and leave the
conclusion unresolved. Never fill a missing result from an expectation, use zero for
an unmeasured value, or rewrite a preregistered hypothesis after observing results.

Keep these levels distinct:

1. observed result;
2. interpretation consistent with the result;
3. decision or design implication;
4. limitation or untested claim.

Repeated samples, seeds, or closely related metrics improve precision but do not
automatically provide a different kind of evidence. Identify shared assumptions and
failure modes. Do not turn correlational, geometric, surrogate, or single-condition
evidence into causal, functional, downstream, or generalization claims.

For pilot-only evidence, report three separate judgments: whether the run is
valid, whether the predeclared gate was met, and what the observed conditions
actually support. `SUPPORTED` and `REJECTED` name pilot-gate outcomes; neither
is an unrestricted verdict on the hypothesis. State the selected conditions,
material missing comparisons or replications, plausible alternatives, and the
next observation needed for a broader claim. A record may be `Completed` at
pilot scope without implying that an expanded study was done or needed.

### Section contract

Preserve the template's H1/H2 names and order. Begin every section and subsection
with its main conclusion or, before completion, its current status and unresolved
question. Make each section understandable to an AI/ML expert who knows the field
but has not read another section or this repository.

- `Motivation`, `Hypothesis`, and `Expected Result` retain their preregistered
  content. Mark retrospective reconstruction explicitly when no prior record exists.
- `Experiment / Setup` contains scientific conditions, terminology, lineage,
  inherited settings, code/version identity, and execution environment.
- `Experiment / Experiment` contains the protocol, commands, run ledger, paths,
  logs, deviations, any pilot classification or expansion approval, and
  reproducibility details.
- `Experiment Result / Results` contains only measurements and the context needed
  to understand how they bear on the hypothesis.
- `Experiment Result / Analysis` states the scope-qualified conclusion, evidence,
  interpretation, implications, alternatives, uncertainty, and claim boundary.
  If result origin is unverified, open with that limitation and keep comparisons
  conditional on the artifact rather than attributing improvement to its claimed
  source.

Keep implementation and execution provenance out of `Results` and `Analysis`; they
remain available in `Experiment`. If an execution defect compromises evidence,
describe its scientific consequence as unresolved validity, a confounder, or an
inconclusive result.

### Terminology

Use the repository's governing terminology source and the experiment's glossary.
Each nonstandard term or symbol must include its exact definition, code
correspondence when applicable, and agreement source. Define nonstandard metrics by
aggregation, denominator, baseline, direction, and unit.

Preserve established field terminology when translation would reduce precision.
Replace repository-specific aliases and shorthand with standard terms or define
them operationally on first use. Do not invent a metaphor, label, abbreviation,
metric, or notation. Keep an internal name in parentheses only when traceability
requires it.

### Completion gate

Before setting `Completed`, confirm:

- every primary value matches its artifact and every table column is defined;
- each source-level claim has an evidenced link from result artifact to source,
  or is explicitly conditional with the missing link and next evidence named;
- observations, interpretations, implications, and limitations are distinguishable;
- each section begins with its own conclusion and contains enough local context;
- the claim stays within measured models, data, seeds, conditions, and evidence;
- a pilot-only conclusion identifies the gate outcome separately from the
  scientific inference and names what was not tested;
- failed, skipped, invalid, and unmeasured items are represented accurately;
- repository-specific terminology is replaced or defined;
- execution details appear only in the two `Experiment` subsections;
- the Analysis separates observations that matched expectations, observations
  that differed, benefits, and limitations, or states why an item cannot be
  assessed;
- the current checkout identity, SHA, dirty state, artifact paths, and timestamps
  are current; branch, worktree, and pilot/expansion decisions are recorded when
  those actions occurred.

Write in connected, conclusion-first prose. Prefer one decision-relevant table over
an exhaustive dump. Keep secondary diagnostics only when they establish validity,
explain the primary result, or bound the conclusion.
