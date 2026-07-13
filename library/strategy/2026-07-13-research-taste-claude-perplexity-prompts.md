# Research-Taste Prompts for EPT/EGT Paper Ideation

Date: 2026-07-13  
Source: Chen, Zhao, and Cohan (2026), "Measuring the Gap Between Human and LLM Research Ideas", arXiv:2607.01233.

## Purpose

Use these prompts to avoid the default LLM pattern of generating fluent bridge/synthesis papers. The goal is not to ban synthesis, but to force alternative research moves before choosing a paper architecture.

## Claude Prompt: Creative Research-Taste Diversification

```text
Act as a research-taste auditor and creative co-designer for my EPT/EGT legal theory program.

Do not merely improve style. Your task is to diagnose the research move and generate stronger alternatives.

Input:
- Working title:
- Abstract or rough idea:
- Intended contribution:
- Existing EPT/EGT concepts involved:

Classify the idea on two axes:

Opportunity Pattern:
1. Puzzle / Contradiction
2. Explanation Gap
3. Scope Mismatch
4. Evidence Gap
5. Bridge Opportunity
6. Failure / Risk Gap
7. Resource Bottleneck

Method Paradigm:
1. Synthesis / Unification
2. Relax / Extend Scope
3. Robustification
4. Formal Derivation
5. Empirical Mapping
6. Artifact / System
7. Optimization / Search

Then:
1. State whether the current idea has bridge/synthesis default risk.
2. Identify any surface stitching, generic framework language, or weak bottleneck specificity.
3. Generate at least five alternative versions using different opportunity/method pairs.
4. For each version, state what new evidence, formal move, dataset, artifact, case, prediction, or citation path would make it real.
5. Select the strongest version for a paper, and explain why it is stronger than the original.
6. List what not to overclaim.

Return:
- Taste profile.
- Bias flags.
- Alternative matrix.
- Recommended paper architecture.
- Minimal next drafting plan.
```

## Claude Prompt: Pre-Zenodo Originality Gate

```text
Before I upload this manuscript to Zenodo, apply a research-taste diversity gate.

Classify the manuscript's central contribution by:
- Opportunity Pattern
- Method Paradigm

Flag:
- bridge/synthesis default risk;
- surface stitching;
- boilerplate framework language;
- weak bottleneck specificity;
- absence of mechanism, measurement, formal derivation, artifact, or falsifiable prediction.

If the manuscript is mainly Bridge Opportunity + Synthesis / Unification, do not reject it automatically. Instead, answer:
1. Is the bridge necessary and non-obvious?
2. Does it create a new mechanism, measure, formal distinction, artifact, dataset, or prediction?
3. What one addition would most improve the paper before upload?

End with:
- upload now;
- upload after minor strengthening;
- hold for substantive creative revision.
```

## Perplexity Prompt: Non-Default Literature Search

```text
I am developing an EPT/EGT legal theory paper and want to avoid a generic bridge/synthesis contribution.

Working idea:
[paste title + abstract or 5 claims]

Search for literature and evidence that would support non-default versions of this idea across these research moves:
1. Puzzle / Contradiction
2. Explanation Gap
3. Scope Mismatch
4. Evidence Gap
5. Failure / Risk Gap
6. Resource Bottleneck
7. Formal Derivation
8. Empirical Mapping
9. Artifact / System

Do not rewrite the paper. Give:
- canonical sources for each promising move;
- recent sources or datasets;
- rival theories or objections;
- whether the idea already exists under another name;
- URLs and citations;
- which move looks most original and evidence-grounded.

Separate verified source facts from your inferences.
```

## Combined Workflow

1. Use Claude to classify the current idea and generate non-default alternatives.
2. Use Perplexity only on title, abstract, claims, and bibliography unless the author approves sharing the full manuscript.
3. Feed Perplexity's source findings back to Claude.
4. Choose the paper architecture.
5. Run `paper-assistant-review` for validation, citations, DOI/Zenodo hygiene, CLI/TCI discipline, and overclaiming.

