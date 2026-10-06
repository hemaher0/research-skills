---
name: evidence-based-research
description: Use when carrying an AI/ML inquiry through evidence-led iterations and choosing or revising the next attempt, explanation, method, or question.
---

# Evidence-Based Research

Move an inquiry forward through purposeful attempts and evidence-led judgment.
The useful outcome may be a discovered relation, a narrower question, a failed
explanation, or an unresolved issue worth retaining. Questions, methods, and
measurement targets can evolve.

## Choose the current inquiry

Start from the user's research aim, existing cues, prior attempts, and the
uncertainty now limiting understanding. State why this uncertainty matters and
which next attempt could reduce it or reveal something new. Incorporate the
user's observations, domain knowledge, counterexamples, and proposed direction
throughout the inquiry. Explain consequential reframing of the requested aim
and resolve a change beyond its authorized scope before pursuing it.

Use other reasoning skills at the point they help:

| Current need | Skill |
| --- | --- |
| Determine what relevant precedents establish | [exploration](../exploration/SKILL.md) |
| Decompose a particular problem or uncertain link | [digging](../digging/SKILL.md) |
| Understand existing results and their claim boundary | [interpretation](../interpretation/SKILL.md) |
| Reconnect cues or reconsider the framing | [reinterpretation](../reinterpretation/SKILL.md) |
| Develop a provisional explanation and its implications | [probing](../probing/SKILL.md) |

No fixed order or complete hypothesis is required before the first observation.
Motivation, method, and experimental evidence can each prompt further inquiry.

## Ground consequential choices

For a choice that materially affects what an attempt can establish or the cost
of dependent work, connect the scientific purpose to evidence applicable to the
actual conditions. Identify unresolved premises, the consequence of being
wrong, and how and when to check them. Scale the evidence effort to impact,
uncertainty, and reversibility. Primary sources, applicable prior validation,
direct observations, and supported tradeoffs can justify a choice; an
unsupported method remains a proposal to investigate. A default or inherited
choice needs the same applicability judgment as a newly selected one.

Keep user requirements, selected methods, observed facts, and assumptions
distinct through plans, runs, and records. Recording a choice, freezing a
protocol, or executing it does not establish its adequacy or make it a user
requirement. Execution authorization and evidence supporting scientific
suitability answer different questions.

Give a consequential unresolved premise a covering observation and needed-by
point before later work relies on its truth. Authorized exploratory attempts
may obtain that evidence and can remain inconclusive; every inquiry need not
start with a settled design, literature search, pilot, or exhaustive comparison.
Preserve the unresolved state when an observation cannot answer the question.
Use the available development workflow for implementation correctness and this
workflow for scientific applicability. Successful execution or improvement in
one measurement supports only the claims it actually checks. Revisit choices when
observations undermine their basis, before dependent execution or interpretation.

## Connect attempts to feedback

Before an attempt, state its purpose, the conditions or comparison that matter,
and what will be observed. Record an expectation when justified; otherwise
state what is genuinely unknown. Choose the necessary investigation, analysis,
implementation, or representative execution rather than defaulting to a run.
Use existing artifacts when they can answer the current question.

Carry out the attempt within the user's implementation and execution scope.
Use the available development skills for needed code and software verification,
[pilot](../pilot/SKILL.md) for bounded representative runs, and the project's
GPU workflow when required. A planning or discussion request alone does not
authorize training, new repository code, or publication.

Inspect actual results and case-level diagnostics, including unexpected
patterns. Distinguish an execution or measurement defect from valid evidence
against an explanation. Compare an earlier expectation with the observation
without changing the earlier record. Identify what this evidence changes about
the explanation, method, conditions, or question, and why. Evidence may be
inconclusive; unchanged judgment requires a reason, not an invented update.

## Choose what follows

Continue, narrow, branch, revisit the representation, or shelve the inquiry
based on what was learned and what another attempt could reveal. Preserve
negative results and unexplained exceptions as cues. Retain the relation to
earlier attempts so a rejected implementation or revised explanation is not
silently overwritten. Improvement in a benchmark score and improvement in
understanding are separate outcomes.

When attempts cease to produce useful information, inspect the repeated
assumptions, diagnostics, and question before choosing another parameter
change. A fixed number of unsuccessful attempts does not determine when a new
framing is needed. Stop or request an expanded scope when the agreed resource
boundary is reached; continue within an existing authorization without seeking
permission for every iteration.

Keep findings proportionate to the request. Use [experiments](../experiments/SKILL.md)
for requested persistent experiment management and [report](../report/SKILL.md)
for a requested presentation. Otherwise communicate the current findings,
uncertainty, changed judgment, and reason for the next attempt in the
conversation and any project-required record. Every inquiry need not become a
finished study, and every hypothesis need not be resolved before handoff.

## Research basis

[Corral (2026)](https://arxiv.org/abs/2604.18805) motivates checking how evidence
affects judgment rather than relying on task success. [Little Scientist (2026)](https://arxiv.org/abs/2608.16951)
uses iteration and case-level diagnostics in two bioinformatics problems; its
sequential infrastructure changes do not isolate each component's effect.
These sources inform the loop, not a claim that these instructions alone
establish scientific reasoning capability.
