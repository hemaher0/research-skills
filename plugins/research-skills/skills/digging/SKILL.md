---
name: digging
description: Use when a specific AI/ML research problem, assumption, method, or unexpected phenomenon needs decomposition, implementation inspection, or targeted reproduction to understand it.
---

# Digging

Decompose a specific problem until the uncertain connection is visible. The
outcome may be a clearer question or an unexplained mechanism; understanding
does not require an immediate fix or a successful full reproduction.

## Locate the uncertainty

Identify the observation, argument, or behavior to understand, including the
conditions and its evidence. Separate what was directly observed from what the
user, paper, or agent currently believes explains it. State which connection
is unclear: data to measurement, implementation to behavior, assumption to
derivation, or behavior to scientific explanation.

Trace the relevant path from inputs through transformations and decisions to
the observed quantity. For a method, map the paper's operations to the actual
code, configuration, defaults, data preparation, and evaluation. For a
conceptual problem, unpack definitions, assumptions, dependencies, and where
the argument stops applying. Follow only the parts that bear on the uncertainty.

## Make the problem distinguishable

Choose a contrast that can expose the uncertain link: two affected cases,
changed conditions, an intermediate quantity, a counterexample, an ablation,
or a targeted reproduction. Explain what each comparison could reveal and
which variables or assumptions remain entangled. Several causes can interact;
do not force a single-cause explanation by ignoring those interactions.

Check the existing artifacts and implementation first. Run an analysis or
reproduction only within the requested execution scope. Preserve the conditions
needed to study the phenomenon; a convenient miniature may test software
behavior while failing to represent the research question. If representative
new evidence is needed, use [pilot](../pilot/SKILL.md) for its execution scope.

Track the inspected code revision and relevant inputs. Distinguish a run or
measurement defect from evidence against the scientific explanation. A
working program does not establish the mechanism, and an implementation error
does not by itself refute it. Handle a demonstrated software defect through
the available development/debugging workflow when fixing it is in scope.

## Reassemble what was learned

Return the decomposed parts and the connections actually checked. Identify
which assumption now looks weaker, which alternative remains possible, and
where further inspection or observation would discriminate them. If the
evidence cannot identify a cause, retain that uncertainty explicitly.

Stop at a useful boundary: the requested issue is explained, the missing link
has been localized, or further progress needs unavailable evidence or a new
execution scope. Incorporate the user's domain knowledge and counterexamples
when they change the decomposition.

Use [interpretation](../interpretation/SKILL.md) for conclusions from existing
results, [probing](../probing/SKILL.md) for a provisional explanation, and
[evidence-based-research](../evidence-based-research/SKILL.md) for the next evidence-led attempt. No new
experiment record or durable artifact is required merely to investigate.

## Research basis

[Corral (2026)](https://arxiv.org/abs/2604.18805) separates workflow outcomes
from evidence use, testing, judgment, and revision across bounded scientific
environments. This motivates inspecting the links behind an outcome rather
than treating task completion as scientific understanding.
