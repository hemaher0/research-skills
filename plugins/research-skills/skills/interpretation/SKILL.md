---
name: interpretation
description: Use when analyzing existing AI/ML research results, choosing meaningful transformations or comparisons, and judging what the evidence supports or leaves unresolved.
---

# Interpretation

Determine what the available results mean under the conditions actually
observed. A useful outcome can be a narrower conclusion, a surprising pattern,
or a clearly unresolved question.

## Establish what the evidence represents

Read the primary artifacts and available run or export evidence. Check the
connection to the claimed model, intervention, data, configuration, and
execution. Correct calculations and matching sample IDs establish properties
of the supplied artifact, not its claimed origin. If that link is unverified,
make calculations conditional on the artifact and leave source-level claims
unresolved. Use the project's available provenance; no particular manifest or
signature format is compulsory.

Distinguish computational validity, measurement validity, and scientific
inference. Verify the experimental unit, comparison, aggregation, denominator,
direction, and unit for consequential metrics. Inspect data integrity,
confounders, evaluation leakage, and analysis defaults where they could change
the conclusion. Preserve missing, invalid, and unmeasured values as such.

Use direct calculations or existing analysis tools. Keep ad hoc processing in a
temporary workspace unless a reusable analysis artifact is requested or the
project's workflow requires one. Existing-result analysis alone does not
authorize training or an expanded evaluation run.

## Examine the structure of the results

Start with the question and existing comparisons. Inspect effect sizes,
variation, case-level or subgroup differences, exceptions, and repeated
observations when relevant. Closely related metrics, samples, or seeds may
share failure modes and should not be counted as independent corroboration.

Choose transformations because they expose a particular ambiguity: for
example, normalization to compare scales, residuals to examine an unexplained
component, or paired differences to separate average change from who benefits.
Explain what a transformation retains or removes and whether it changes the
quantity being studied. Keep the source measurements recoverable.

Check plausible alternative processing or grouping choices when they could
reverse the conclusion. Identify post-observation analyses as exploratory;
preserve the earlier comparison and account for selection and repeated search
before making confirmatory claims. Do not manufacture a numerical prediction
when none was made.

## Update the conclusion

Separate observations, compatible explanations, and decisions. Match the
conclusion to the measured conditions and evidence: correlation, geometry,
surrogate metrics, or one condition alone do not establish causal mechanism,
downstream benefit, or generality. Examine evidence that disagrees with the
current explanation as well as evidence that agrees.

Carry a discovered limitation into the primary conclusion and recommendations,
not only a caveat paragraph. Explain which judgment changes and why; if the
evidence does not discriminate the alternatives, state why it cannot justify
a change. For a pilot, distinguish run validity, any predeclared gate outcome,
and the scientific claim the result actually supports.

Return the useful patterns, scoped conclusion, conflicting evidence, and
remaining questions. Suggest the observation that could resolve a material gap
without automatically launching it. Use [report](../report/SKILL.md) for a
requested research presentation and [reinterpretation](../reinterpretation/SKILL.md)
when multiple cues suggest a different connection or question. Existing-result
analysis does not require a new run, repository script, or experiment record.

## Research basis

[DISCERN (2026)](https://arxiv.org/abs/2609.33357) evaluates data integrity,
analysis verification, and hypothesis judgment separately, including failures
to carry recognized limitations into conclusions. Its bounded, predominantly
life-science tasks do not establish reliable end-to-end discovery.
