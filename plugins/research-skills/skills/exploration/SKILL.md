---
name: exploration
description: Use when investigating scientific precedents, methods, implementations, or conflicting prior evidence for an AI/ML research question.
---

# Exploration

Investigate what prior work actually establishes, under which conditions, and
what remains worth investigating. The question and search vocabulary may
change as the literature becomes clearer.

## Shape the investigation

Translate the user's question into the distinctions that matter: phenomenon,
assumptions, mechanism, method, data, measurement, and operating conditions.
Separate required conditions from tentative interpretations. Treat a user's
unpublished observation as a cue to investigate, not as an established fact or
something to discard because it disagrees with a familiar paper.

Start with the closest precedents, then follow references, citing work,
alternative terminology, and neighboring fields where a relation warrants it.
Check current primary publications and versions when freshness matters. Keep
foundational work when it explains a concept that newer papers merely reuse.
Revise queries when different terminology or a mistaken initial assumption
blocks discovery; keyword overlap alone does not establish relevance.

## Verify the useful claims

For a decision-relevant claim, inspect the actual methods, equations, tables,
figures, appendices, or official implementation. Connect the claim to its exact
source location and conditions. Distinguish an implemented feature, a measured
result, an author's interpretation, and a proposed future capability.

Compare the most relevant precedents by the question they answer and the
conditions that differ. Include contradictory findings, limitations, and
unsuccessful approaches when they change the current research direction.
Inspect public code selectively when it can resolve a material uncertainty
about a method or evaluation; identify the inspected revision and files.
Running an entire reproduction is not necessary for a literature investigation.

When papers appear to disagree, first check definitions, experimental units,
data, comparisons, and conditions. Preserve unresolved conflicts instead of
selecting the source that best fits the initial idea.

## Return a usable map

Explain what is established, conditional, disputed, and still unknown, with
links to the relevant evidence. State which prior work can inform the user's
next inquiry and what would need to change before its result applies.

Bound the search conclusion by the sources, dates, queries, and accessible
material actually examined. Stop when the requested scope is covered or the
remaining search is unlikely to alter the current decision within its budget.
An unsuccessful search supports "not found in this investigation," not a
universal claim of absence or novelty.

Answer in the conversation unless a durable deliverable is requested or project
policy requires a record. Use the project's document conventions and any
available document router for a requested artifact. Use [digging](../digging/SKILL.md)
when a particular problem needs decomposition and
[reinterpretation](../reinterpretation/SKILL.md) when cues need a new framing.
These are follow-up choices, not required stages.

## Research basis

[AutoResearchBench (2026)](https://arxiv.org/abs/2604.25256) studies full-text,
multi-condition literature discovery and search completeness. Its benchmark
supports these distinctions; it does not establish the effectiveness of this
skill or certify that a literature survey is exhaustive.
