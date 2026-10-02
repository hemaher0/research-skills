---
name: experiments
description: Use when creating or continuing a persistent AI/ML experiment record and managing its protocol, lineage, execution state, and evidence. Not for standalone result investigation, a standalone pilot or report, or design discussion without a requested record.
---

# Experiments

Manage one requested, persistent experiment record. Its local Markdown document
holds the working question, protocol versions, execution history, evidence, and
current analysis. A question about existing
results, a pilot, or a report does not require this record. Do not create one
unless the user asks to manage the experiment over time or requests a durable
experiment document.

Separately, follow the project's work-history capture policy. When it calls
for a work-item update, preserve material goal and protocol decisions, progress,
experiment links, evidence, code identity and continuation state there. A
configured repository alone does not enable capture or require every turn;
selective or disabled capture leaves this requested experiment record and its
required provenance unchanged. Check whether a compatible
document-routing skill is actually available before using it; no named router
is a prerequisite. A router handles work-item and experiment-document file
operations; this skill owns record identity, provenance, lineage, template,
configured root, and lifecycle. If no router is available, use project
`AGENTS.md`, the local `.docs-schema` when present, and ordinary file tools.
The work item does not replace this experiment record.
When capture is required for parallel research tasks, give each a linked child
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

An experiment can draw on several code repositories. Identify each repository's
role and relevant revision or snapshot, and select the execution repository and
environment for each run. The configured document repository owns the record's
location, not code execution authority. Repository access and each run remain
within the research task and resource scope. Keep the work item and experiment
record linked without treating them as the same document.

This skill owns protocol and evidence records. A record-management request
alone does not authorize changing implementation or launching a run. When the
authorized research task also requires execution or implementation, use the
responsible execution/development workflow within that same authority and link
its artifacts and evidence here. Resolve an essential missing capability before
dependent execution without treating record maintenance as a new research goal.

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

A standalone result analysis uses [interpretation](../interpretation/SKILL.md),
and a requested presentation uses [report](../report/SKILL.md). Neither requires
a persistent experiment record. Use [evidence-based-research](../evidence-based-research/SKILL.md) for
iterative direction, [probing](../probing/SKILL.md) for hypothesis development,
[exploration](../exploration/SKILL.md) for precedents, and
[digging](../digging/SKILL.md) or [reinterpretation](../reinterpretation/SKILL.md)
when the current uncertainty calls for them. Record their relevant decisions
when this record is being managed; there is no mandatory sequence.

If the request separately includes an update to reader-facing repository
documentation, use an available document router; otherwise follow the
repository's documentation conventions and ordinary file tools. Do not infer
a documentation update from the experiment alone.

## Scientific contract

- Record the current question, purpose, relevant cues, and unresolved
  uncertainty. A partial hypothesis or an exploratory question is sufficient;
  an expected numerical result or binary decision gate is not compulsory.
- Before each attempt, record the protocol, conditions, observations to collect,
  justified expectations, and authorized resource boundary. Preserve required
  comparisons and replications. Distinguish exploratory from confirmatory work.
- Read direct primary research or official experimental material when the design
  depends on prior work. Link the relevant claim, equation, figure, or protocol and
  state what is reused or changed. Mark unsupported methods as original proposals.
- Preserve earlier questions, hypotheses, expectations, and protocol versions.
  Record a change with its timing, evidence, rationale, affected comparisons,
  and implications for the next attempt. Identify post-observation ideas as
  such; do not rewrite them as predeclared. Only call a protocol preregistered
  when actual registration exists. A project-required frozen protocol remains
  authoritative for its confirmatory comparisons.
- A revised question or method can continue in this record within the authorized
  inquiry. A separately managed execution or independently tracked question may
  justify a linked child; every revision does not require one or new approval.
- Treat a pilot classification, when specified, as a decision about its
  predeclared gate under the selected conditions. Check run validity, gate
  outcome, and strength of scientific inference separately. A passed gate can
  justify a next step without
  establishing robustness, mechanism, or generality; a failed gate under limited
  conditions does not by itself refute the hypothesis everywhere.
- Preserve [interpretation](../interpretation/SKILL.md)'s distinctions among
  observations, explanations, implications, and open claims. Store linked
  artifacts and the judgment they informed, including negative and unexpected
  findings. Closing this record does not resolve every scientific question.
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

Resolve shared experiment-document locations from effective project instructions
or their existing configuration source. Use a selected local `AGENTS.local.md`
path override when it specifies a path within project policy; otherwise use
the shared setting. Installation configuration follows the source README;
record management consumes the effective locations.
Empty/placeholder or `Use Repository Default` overrides leave that setting
in force. Resolve a relative document path from the main checkout, never from an isolated code
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

When isolation is needed, follow the project's Git naming and workspace
procedure. Link the actual branch/worktree to this identifier; a scientific
record identity does not prescribe a Git branch or require a new checkout.

Use these document states:

| State | Meaning |
| --- | --- |
| `Planned` | The question and initial protocol are being prepared; no training or evaluation has started. |
| `Running` | Authorized execution is in progress without a separate pilot phase. |
| `Pilot Running` | An explicitly requested bounded pilot is in progress. |
| `Awaiting Decision` | Progress needs a consequential direction, resource, or scope decision beyond the current authorization. |
| `Awaiting Expansion Approval` | Pilot passed and the larger budget has not been approved. |
| `Expanded Running` | The approved post-pilot experiment is in progress. |
| `Completed` | Work for this record's declared scope is finished and reviewed; findings and open scientific questions are preserved. |
| `Stopped` | The user ended the experiment without completing the planned evidence. |

Do not insert a pilot merely to move between `Planned`, `Running`, and `Completed`.
`Pilot Running`, `Awaiting Expansion Approval`, and `Expanded Running` remain
available for records that track those execution phases; they do not impose a
research sequence. Use `Running` for ordinary authorized iterations. An open
hypothesis is not itself a reason to leave a finished record awaiting approval.

### Create or continue the record

Resolve the repository, configured document root, intended path, and current
code identity before routing a document update. Check for an existing record
with the same ID or subject and continue it when appropriate. Use the current
suitable checkout unless a concrete isolation need is present. Record the
current branch, SHA, timestamps
with UTC offset, and dirty state. Record `None` for a branch or worktree created
specifically for this experiment when there is none. If the repository defines a
spec/change system, follow its actual policy; otherwise record `N/A`.

Use the project's Git workflow to decide whether to reuse or allocate a
workspace, choose its base and name, reconcile interrupted operations, and
perform authorized remote or integration actions. This record does not add a
separate Git permission policy. Record the actual repository, checkout, base
and result snapshots and any material uncommitted inputs. When a child protocol
requires a parent's code, identify the parent's actual required snapshot and
have the Git workflow materialize it; scientific parentage alone does not
select a branch tip. Preserve pending work and evidence through that workflow.

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

Use [interpretation](../interpretation/SKILL.md) for scientific analysis and
[report](../report/SKILL.md) when presenting it. This skill preserves their
evidence links and claim boundaries in the managed record, together with the
history of which observation changed which judgment. A contradiction,
inconclusive comparison, or unchanged judgment belongs in that history too.

For pilot-only evidence, report run validity, what the observed conditions
actually support, and whether a predeclared gate was met when one exists.
`SUPPORTED` and `REJECTED` name pilot-gate outcomes; neither
is an unrestricted verdict on the hypothesis. State the selected conditions,
material missing comparisons or replications, plausible alternatives, and the
next observation needed for a broader claim. A record may be `Completed` at
pilot scope without implying that an expanded study was done or needed.

### Section contract

Preserve the template's H1/H2 names and order. Begin every section and subsection
with its main conclusion or, before completion, its current status and unresolved
question. Make each section understandable to an AI/ML expert who knows the field
but has not read another section or this repository.

- `Motivation`, `Hypothesis`, and `Expected Result` describe the current question,
  provisional explanation, and intended observations. Preserve earlier versions
  with their timing and reasons for change. A hypothesis or expectation that is
  not yet defined is stated as open, not fabricated. Mark retrospective
  reconstruction explicitly when no prior record exists.
- `Experiment / Setup` contains scientific conditions, terminology, lineage,
  inherited settings, code/version identity, and execution environment.
- `Experiment / Experiment` contains the protocol, commands, run ledger, paths,
  logs, deviations, any pilot classification or expansion approval, and
  reproducibility details.
- `Experiment Result / Results` contains only measurements and the context needed
  to understand how they bear on the hypothesis.
- `Experiment Result / Analysis` states the scope-qualified conclusion, evidence,
  interpretation, implications, alternatives, uncertainty, and claim boundary,
  including abandoned explanations and unresolved research cues.
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
  scientific inference and names what was not tested, when a gate was specified;
- failed, skipped, invalid, and unmeasured items are represented accurately;
- repository-specific terminology is replaced or defined;
- execution details appear only in the two `Experiment` subsections;
- earlier expectations and actual observations are distinguishable; findings,
  unexplained reactions, changed judgments, and remaining questions are
  preserved without requiring a successful or fully resolved study;
- the current checkout identity, SHA, dirty state, artifact paths, and timestamps
  are current; branch, worktree, and pilot/expansion decisions are recorded when
  those actions occurred.

Write in connected, conclusion-first prose. Prefer one decision-relevant table over
an exhaustive dump. Keep secondary diagnostics only when they establish validity,
explain the primary result, or bound the conclusion.
