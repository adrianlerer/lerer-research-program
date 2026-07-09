# PAT-Inspired Claude and Perplexity Prompts for EPT/EGT Papers

Date: 2026-07-09  
Source: Jayaram et al. (2026), "Towards Automating Scientific Review with Google's Paper Assistant Tool", arXiv:2606.28277.

## Purpose

Use these prompts to implement a PAT-style author-side review workflow for future EPT/EGT papers. The goal is not automated authorship. The goal is early detection of weak claims, missing citations, formula ambiguity, unsupported validation language, and publication-readiness issues.

## Claude Prompt: Deep Manuscript Review

```text
Act as a PAT-style pre-submission reviewer for my EPT/EGT manuscript.

Role boundary: you are a tool for the author, not a final peer reviewer and not the author. I remain responsible for all claims.

Segment the manuscript into: thesis/contribution, literature, theory/framework, methods/instruments, empirical evidence, legal/normative claims, citations, conclusion/limitations.

Allocate review effort adaptively:
- high effort for formulas, indices, validation claims, causal claims, novelty claims, legal/policy prescriptions, and citations;
- medium effort for conceptual coherence, terminology, rival theories, and definitions;
- light effort for style and formatting.

Apply my EPT/EGT preflight operationally, item by item:
- first classify the manuscript genre: empirical validation, theoretical architecture, bridge paper, methodological correction, normative/intervention module, or rival-programme positioning; calibrate the evidentiary standard to that genre;
- do not let IHR, IEI, AIT/GIMT, PSO, DCF, SMD, LSE, holonomy, or TCI be described as empirically validated unless the manuscript provides independent evidence, not merely another self-citation;
- enforce CLI/TCI discipline: CLI and TCI must be distinct constructs, and the manuscript should use the current canonical CLI formula `0.30P + 0.25D + 0.20O + 0.25E`; flag any divergent formula or silent recomputation;
- flag placeholder Zenodo DOIs, `DOI pending`, or obsolete SSRN reliance where a Zenodo DOI exists;
- where topically relevant, flag missing engagement with cultural attraction theory (Sperber, Claidière), Binmore, Young, Bowles-Gintis, path dependence (David, Pierson), or NK landscapes (Kauffman);
- if the paper makes normative or policy claims, require falsable predictions and an intervention mechanism;
- check for Lakatosian Epistemological Declaration, AI Disclosure, and careful wording for papers where no simulation or empirical test was actually executed.

Return:
1. Verdict: ready / ready after minor fixes / needs substantive revision / do not upload yet.
2. Blocking issues.
3. Should-fix issues.
4. Consider issues.
5. Section-by-section action list.
6. Suggested revised abstract only if needed.
```

## Perplexity Prompt: Grounding and Literature Check

```text
I am checking an EPT/EGT legal-theory manuscript before publication.

Do not rewrite the manuscript. Act as a source-grounding and literature-verification assistant.

Tasks:
1. Verify whether the core claim has close recent analogues.
2. Identify canonical sources I should cite.
3. Identify missing rival theories or objections.
4. Check DOI/source existence for cited works if I provide a bibliography.
5. Flag claims that require current evidence.

Use web sources and give URLs. Separate:
- verified source facts;
- plausible but unverified inferences;
- recommended citations;
- risks of overclaiming.

Special focus:
- cultural attraction theory vs. memetics;
- evolutionary game theory of institutions;
- path dependence in law;
- niche construction and extended evolutionary synthesis;
- AI-assisted peer review and scientific validation bottlenecks;
- AI as constructor of the legal/scientific memetic niche.
```

## Combined Workflow

1. Run Claude on the full manuscript for segmented deep review.
2. Run Perplexity only on abstract, claims list, and bibliography unless the user approves sharing the full draft.
3. Feed Perplexity's verified citations back into Claude for a second pass.
4. Produce a final action list with `blocking`, `should fix`, `consider`, and `style`.
5. Only after fixes, decide whether to upload to Zenodo, submit to journal, or convert to Substack.

## Minimal Claim List to Send to Perplexity

When avoiding full-draft sharing, send this instead:

```text
Title:
Abstract:
Five core claims:
1.
2.
3.
4.
5.
Bibliography:
[paste references]
What I need checked:
- source existence;
- recent related work;
- rival theories;
- missing canonical citations;
- overclaim risk.
```
