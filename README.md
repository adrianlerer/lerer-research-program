# Lerer Research Program
## Extended Phenotype Theory of Law · Evolutionary Game Theory · Institutional Design

**Ignacio Adrián Lerer**
Independent Researcher · Buenos Aires, Argentina
ORCID: [0009-0007-6378-9749](https://orcid.org/0009-0007-6378-9749)
Email: adrian@lerer.com.ar
Zenodo communities: [law-as-extended-phenotype](https://zenodo.org/communities/law-as-extended-phenotype/) · [small-concept-models](https://zenodo.org/communities/small-concept-models/)
Substack: [adrianlerer.substack.com](https://adrianlerer.substack.com/)

---

## About the Researcher

Ignacio Adrián Lerer is a lawyer (Universidad de Buenos Aires) and Executive MBA (IAE Business School, Universidad Austral) based in Buenos Aires, Argentina. He is an independent researcher working at the intersection of evolutionary biology, game theory, institutional economics, and law.

His research program applies Dawkins's (1982) Extended Phenotype Theory and Dennett's intentionality hierarchy to legal institutions, producing a suite of quantitative diagnostic instruments validated against empirical datasets from four jurisdictions. He has published over 110 working papers on SSRN and Zenodo since 2024 (69 on Zenodo, 62 on SSRN, with partial overlap between the two repositories), has one article published and one manuscript under review at the *Journal of Computational Law and Legal Technology* (JCLLT).

He is not affiliated with a university. All work is independent research.

---

## The Research Program

### Core Thesis

Legal norms function as **cultural replicators** (memes) subject to Darwinian selection. Their fitness is defined as:

```
Fitness = P(transmission) × P(compliance) × P(enforcement)
```

Institutions are the **extended phenotypes** these replicators build for their own reproduction: specialized courts, university curricula, bar associations, enforcement agencies. These structures persist long after the original norms they served have been formally repealed.

The program integrates five theoretical traditions that have not previously been combined:

1. **Dawkins's Extended Phenotype Theory** (1982) — the causal reach of replicators extends beyond the organism into the environment
2. **Dennett's Intentionality Hierarchy** (1987) — agents operate at different levels of intentional complexity (L0–L3+)
3. **Evolutionary Game Theory** (Maynard Smith 1982, multilevel selection) — ESS analysis, replicator dynamics, Price equation
4. **Hayek's Spontaneous Order** (1973) — institutional patterns emerge without central design
5. **Scott's Infrapolitics** (1985, 1990) — hidden transcripts and everyday resistance as selection mechanisms

### Program Architecture (Lakatos 1978)

**Hard core** (non-negotiable):
- Legal norms are cultural replicators subject to variation, selection, and retention
- Institutions are extended phenotypes of dominant memeplexes
- Multilevel selection operates in legal systems (intra-group and inter-group)
- Agents operate at asymmetric intentionality levels (L1 corporations vs. L3 humans)
- Legal professionals learn norms by observing authoritative reactions, not empirical outcomes (HBU)

**Protective belt** (empirically adjustable):
- Specific CLI component weights
- IHR numerical thresholds
- Dennett-Nash Gap empirical estimates

**Positive heuristic** (expansion directions):
- New jurisdictions (UK, US, Japan, India, South Africa)
- New domains (tax law, environmental law, AI regulation, IP)
- Computational implementation (CriptoIus, JurisRank, IusMorfos)

---

## Theoretical Instruments

### CLI (Constitutional Lock-in Index)

Measures institutional rigidity ex ante (before reform attempt):

```
CLI = 0.30×P + 0.25×D + 0.20×O + 0.25×E
```

- **P** = Precedent density (citation network entrenchment)
- **D** = Doctrinal elaboration (academic consensus volume)
- **O** = Professional organization (bar certification, specialized courts)
- **E** = Enforcement infrastructure (administrative capacity)

**Validation**: R²=0.74, AUC=0.97, 60 labor reform cases, 4 jurisdictions (Argentina, Brazil, Chile, Spain). ICC=0.9335 inter-rater reliability (4 LLMs, n=30 US constitutional provisions).

**Key empirical results**:

| Jurisdiction | CLI | Reform outcome |
|---|---|---|
| Argentina (Art. 14bis) | 0.87–0.89 | 0/24 successful over 4 decades |
| Brazil (CLT pre-2017) | 0.40 | 2017 reform succeeded |
| Chile | 0.24 | 15/17 succeeded, bidirectionally |
| Spain | 0.37–0.51 | 2012 reform succeeded |

Counterintuitive finding: **crisis reinforces lock-in in high-CLI systems** (interaction term β=−2.83, p<0.05). Political economy variables lose significance when CLI is controlled.

**Prospective validation**: Milei 2024 reform program — CLI predicted 12.4% success probability; observed 0% (p=0.003). CGT injunction against Law 27.802 (March 30, 2026) confirmed as observation #24: blocking interval of 24 days, Bayesian posterior updated from P(blocking)=0.92 to **0.94** (95% CI: 0.78–0.99). See [10.5281/zenodo.19340088](https://doi.org/10.5281/zenodo.19340088). The computational validation framework is published in JCLLT: [10.47852/bonviewJCLLT62027951](https://doi.org/10.47852/bonviewJCLLT62027951).

**Thresholds**:
- CLI < 0.30: flexible (ordinary legislation works)
- CLI 0.30–0.50: reformable with difficulty (supermajority + crisis)
- CLI 0.50–0.70: severe lock-in (requires constitutional amendment)
- CLI > 0.70: requires regime change

---

### IHR (Institutional Hysteresis Rate)

Measures irreversible institutional deformation ex post (after reform failure). Scale 0–1.

Distinction from CLI: CLI is structural (ex ante), IHR is historical (ex post, includes infrastructure of formally repealed norms). Argentina Art. 14bis: IHR ≈ 0.87.

**Zombie Law Equilibrium**: when CLI > 0.85 AND Implementation Gap > 0.60 simultaneously — formal reform blocked, informal bypass individually rational, stable equilibrium.

---

### IEI (Institutional Evolvability Index)

Design criterion for building evolvable institutions. Four components (Kirschner & Gerhart 2005):

- **V** (Variation): capacity to generate normative variants = f(1−CLI)
- **S** (Selection): efficacy of outcome-based selection mechanism
- **C** (Conservation): capacity to retain successful innovations
- **M** (Modularity): capacity to reform subsystems without fragmenting the whole

Predicted values: Chile IEI > 0.70, Argentina IEI < 0.30.

---

### AIT + Dennett-Nash Gap

**Intentionality levels** (Dennett 1987):
- L1: behavior predicted by attributing first-order goals — corporations, algorithms, RL agents
- L3: behavior predicted by attributing recursive beliefs about beliefs — adult humans in strategic contexts

**Asymmetric Intentionality Theory (AIT)**: Social coordination mechanisms (shame, reputation, reciprocity) require common knowledge that presupposes L3+. L1 agents are not merely unresponsive — they are **structurally immune**.

**Dennett-Nash Gap**:
```
Δᵢ = SAᵢ + ICSᵢ − MPᵢ + SIPᵢ
```
- SA = Strategic Advantage (exploiting false symmetry assumption)
- ICS = Intentionality Cost Savings (cognitive overhead avoided)
- MP = Mismatch Penalty (losses from misattributing mental states)
- SIP = Social Immunity Premium (structural immunity to social sanctions)

**Empirical estimates**: Tech ToS 15–48% | Argentine executive decrees 40–62% | Sovereign debt ~40pp

---

### HBU (Heteronomous Bayesian Updating)

```
P_A(H|E) = [P(E|H)^w(A) × P(H)] / P(E)    where w(A) > 1
```

Legal professionals (and AI systems trained with RLHF) learn norms by observing **authoritative reactions** (R_a: authority convergence; R_i: institutional elaboration; R_s: coordinated sanctions; R_n: narrative entrenchment) — not empirical outcomes. This generates reform-resistant priors.

Argentina/Brazil comparison: ratio of perceptual to active inference 41:1 (Argentina) vs. 9:1 (Brazil).

---

### PSO (Parasitic Spontaneous Order)

Dawkins-Hayek synthesis: order emerges without central design (Hayek), but the entities generating it optimize for their own fitness, not systemic efficiency (Dawkins). Three activation conditions: visible inequality, organized intermediaries, weakened enforcement.

---

### GIMT (Generalized Intentionality Mismatch Theorem)

Six failure modes in human-institutional interaction:
1. Strategic exploitation (SA dominant)
2. Cognitive cost asymmetry (ICS dominant)
3. Communication breakdown (MP dominant)
4. Social mechanism failure (SIP dominant)
5. Aumann impossibility (when min(Lᵢ, Lⱼ) < 3, posteriors cannot become common knowledge)
6. **Dynamic Classification Failure** (intentionality level changes during interaction — e.g., AI systems transitioning from L1 to L2 during deployment)

---

### JurisRank

Modified PageRank over judicial citation networks with temporal decay. Validated: ρ=0.73, p<0.001, 1,247 Argentine Supreme Court cases. Detects doctrinal crossover points 3–5 years before political visibility.

---

## Computational Infrastructure

- **CriptoIus**: blockchain-based legal precedent system as evolutionary constraint for multi-agent AI governance
- **IusMorfos**: ex ante prediction of reform success probability from CLI components
- **RootFinder**: inverse genealogical tracing through citation networks
- **JurisRank**: PageRank-based doctrinal fitness scoring
- GitHub: [github.com/adrianlerer](https://github.com/adrianlerer)

---

## Papers — Zenodo (72 records, open access)

All papers are freely downloadable. Communities: [law-as-extended-phenotype](https://zenodo.org/communities/law-as-extended-phenotype/) · [small-concept-models](https://zenodo.org/communities/small-concept-models/).

| Date | Title | DOI |
|------|-------|-----|
| 2026-04-29 | Strategy Trendslop as Parasitic Spontaneous Order: Why Large Language Models Converge on Managerial Buzzwords Regardless of Context | [10.5281/zenodo.19867851](https://doi.org/10.5281/zenodo.19867851) |
| 2026-04-28 | Law as Constructed Niche: Reciprocal Causation Between Extended Phenotypes and Selective Environments in Institutional Evolution | [10.5281/zenodo.19839047](https://doi.org/10.5281/zenodo.19839047) |
| 2026-04-27 | Normative Collapse and Institutional Persistence in Authoritarian Regimes: A Multilevel Selection Framework with Computational Validation | [10.5281/zenodo.19806122](https://doi.org/10.5281/zenodo.19806122) |
| 2026-04-27 | Agents as Extended Phenotypes: Behavioral Transfer, Asymmetric Intentionality, and the Evolutionary Stability of Privacy Degradation in Agentic Systems | [10.5281/zenodo.19802281](https://doi.org/10.5281/zenodo.19802281) |
| 2026-04-24 | The Lateral Silencing Exaptation: Unenforceable Norms as Extended Phenotypes of Political Control | [10.5281/zenodo.19720028](https://doi.org/10.5281/zenodo.19720028) |
| 2026-04-08 | **[PUBLISHED — JCLLT]** Computational Detection of Constitutional Drift: Network Analysis and Semantic Measurement of Argentine Supreme Court Jurisprudence (1922–2025) | [10.47852/bonviewJCLLT62027951](https://doi.org/10.47852/bonviewJCLLT62027951) |
| 2026-04-03 | The Epistemic Foundation of the Endogeneity Paradox: Common Knowledge, Intentionality Mismatch, and the Sequential Protocol | [10.5281/zenodo.19394406](https://doi.org/10.5281/zenodo.19394406) |
| 2026-04-01 | The Concept Bottleneck as a Deterministic Evaluation Layer: Implementation of Small Concept Models for Legal Reasoning via OpenAI Structured Outputs | [10.5281/zenodo.19373345](https://doi.org/10.5281/zenodo.19373345) |
| 2026-03-30 | Synthetic Minds in Normative Sandboxes: Exaptation, Spandrels, and Multilevel Selection in Agent-Based Legal Simulation | [10.5281/zenodo.19341388](https://doi.org/10.5281/zenodo.19341388) |
| 2026-03-30 | Judicial Lock-in as Evolutionarily Stable Strategy: The CGT Injunction Against Law 27.802 as Confirmatory Evidence for the Constitutional Lock-in Index | [10.5281/zenodo.19340088](https://doi.org/10.5281/zenodo.19340088) |
| 2026-03-30 | Predatory Invitations as Extended Phenotype: A Parasitic Spontaneous Order Analysis Across Academic and Literary Publishing | [10.5281/zenodo.19339642](https://doi.org/10.5281/zenodo.19339642) |
| 2026-03-29 | The Intelligence Explosion That Will Calcify: Extended Phenotype Theory, Asymmetric Intentionality, and the Evolutionary Pathologies of Agent Institutions | [10.5281/zenodo.19323303](https://doi.org/10.5281/zenodo.19323303) · [PDF](papers/Lerer_2026_Intelligence_Explosion_Calcify.pdf) |
| 2026-03-25 | Metaphors as Legal Memes: EPT, HBU, and the Evolutionary Dynamics of AI Regulatory Language | [10.5281/zenodo.19226108](https://doi.org/10.5281/zenodo.19226108) |
| 2026-03-24 | Obiter Creep: How Marginal Dicta Colonize Ratio Decidendi Through Extended Phenotype Mechanisms | [10.5281/zenodo.19205884](https://doi.org/10.5281/zenodo.19205884) |
| 2026-03-24 | Lamarckian Replicators in Darwinian Hierarchies: Reconciling Gene-Centered and Multilevel Selection Approaches to Legal Evolution | [10.5281/zenodo.19199269](https://doi.org/10.5281/zenodo.19199269) |
| 2026-03-20 | Convergent Institutional Evolution: Organized Crime as Natural Experiment for the Extended Phenotype Theory of Law | [10.5281/zenodo.19122984](https://doi.org/10.5281/zenodo.19122984) |
| 2026-03-19 | Strengthening the Foundations of Law as Extended Phenotype: Coalitional Intelligence and the Evolutionary Origins of Legal Institutions | [10.5281/zenodo.19104281](https://doi.org/10.5281/zenodo.19104281) |
| 2026-03-18 | The Extended Spandrel: Memetic Host Switching and the Paradox of Argentina's Pro-Worker Labor Regime as Extended Phenotype of Extractive Protectionism | [10.5281/zenodo.19098168](https://doi.org/10.5281/zenodo.19098168) |
| 2026-03-17 | Punctuated Institutional Equilibria: Stasis as ESS, Basin Depth, and the Temporal Dynamics of Constitutional Lock-in | [10.5281/zenodo.19077323](https://doi.org/10.5281/zenodo.19077323) |
| 2026-03-14 | Simulating Institutional Dynamics: A Multi-Agent Framework for Predicting Legal Reform Outcomes Using Extended Phenotype Theory | [10.5281/zenodo.19010941](https://doi.org/10.5281/zenodo.19010941) |
| 2026-03-11 | Pre-Deployment Normative Evaluation: An Extended Phenotype Framework for Legislative Quality Assurance | [10.5281/zenodo.18947186](https://doi.org/10.5281/zenodo.18947186) |
| 2026-03-10 | Sycophancy as Extended Phenotype: HBU, Intentionality Mismatch, and the Evolutionary Stability of Algorithmic Flattery | [10.5281/zenodo.18943464](https://doi.org/10.5281/zenodo.18943464) |
| 2026-03-09 | Agentic Fraud as Extended Phenotype: ScamAgent, Parasitic Spontaneous Order, and the Evolutionary Logic of LLM-Mediated Deception | [10.5281/zenodo.18924282](https://doi.org/10.5281/zenodo.18924282) |
| 2026-03-08 | No Legal Big Bang: Inherited Normative Capital, Continuous Regeneration, and the Asymmetric Membrane Problem | [10.5281/zenodo.18911041](https://doi.org/10.5281/zenodo.18911041) |
| 2026-03-07 | Transformer Architecture for Evolutionary Legal Systems: Why Self-Attention Matches Juridical Reasoning, with Application to CriptoIUS | [10.5281/zenodo.18904134](https://doi.org/10.5281/zenodo.18904134) |
| 2026-03-07 | Intentionality Mismatch in Commercial Liability: A Four-Level Evolutionary Analysis of Tapia Araya v. Starbucks (Argentine Supreme Court, 2026) | [10.5281/zenodo.18903217](https://doi.org/10.5281/zenodo.18903217) |
| 2026-03-06 | Ley 27802 as a Prospective Test of the EPT/CLI Framework: Labor Reform, Institutional Lock-in, and Predictive Validity in Argentine Law | [10.5281/zenodo.18895179](https://doi.org/10.5281/zenodo.18895179) |
| 2026-03-05 | Spandrels of Accountability: Scheming Propensity Research as Inadvertent Evidence Against the Algorithmic Corporation | [10.5281/zenodo.18882212](https://doi.org/10.5281/zenodo.18882212) |
| 2026-03-05 | Darwin's One Long Argument and Escohotado's Three Long Volumes: Historical Inference, Institutional Vestiges, and Methodological Convergence | [10.5281/zenodo.18880937](https://doi.org/10.5281/zenodo.18880937) |
| 2026-03-05 | Law as a Primary Adaptive Platform: Generalized Darwinism, EPT, and the Methodological Foundations of Evolutionary Jurisprudence | [10.5281/zenodo.18870552](https://doi.org/10.5281/zenodo.18870552) |
| 2026-03-04 | The Static Agent Assumption: Dynamic Intentionality Classification and the Limits of the Algorithmic Corporation | [10.5281/zenodo.18857385](https://doi.org/10.5281/zenodo.18857385) |
| 2026-03-03 | Predatory Invitations as Extended Phenotype: A Parasitic Spontaneous Order Framework for Academic Publishing | [10.5281/zenodo.18853667](https://doi.org/10.5281/zenodo.18853667) |
| 2026-03-03 | Free-Floating Rationales, Normative Hysteresis, and Constitutional Lock-in: Dennett's Contribution to EPT and Multilevel EGT | [10.5281/zenodo.18851650](https://doi.org/10.5281/zenodo.18851650) |
| 2026-03-02 | Multilevel Selection, Hierarchical Causation, and Constitutional Lock-in: Reconciling Gould with Gene-Centered Memetics | [10.5281/zenodo.18829975](https://doi.org/10.5281/zenodo.18829975) |
| 2026-02-26 | When the Red Queen Stumbles: Temporal Asymmetry and the Collapse of Regulatory Coevolution | [10.5281/zenodo.18790245](https://doi.org/10.5281/zenodo.18790245) |
| 2026-02-25 | Synthetic Chaos as an Institutional Laboratory: Independent Evidence for EPT from Autonomous Agent Red-teaming | [10.5281/zenodo.18777434](https://doi.org/10.5281/zenodo.18777434) |
| 2026-02-25 | Regulatory Hysteresis, Extended Phenotype, and the Lex Artis of Institutional Design | [10.5281/zenodo.18774354](https://doi.org/10.5281/zenodo.18774354) |
| 2026-02-25 | Constitutional Chimera, Structural Hyperregulation, and Artificial Intelligence as Stress Test | [10.5281/zenodo.18765188](https://doi.org/10.5281/zenodo.18765188) |
| 2026-02-24 | The Non-Justiciability Meme: FIFA's Prerogative State and the Four Century Genealogy of a Legal Concept | [10.5281/zenodo.18758065](https://doi.org/10.5281/zenodo.18758065) |
| 2026-02-22 | Regulating the Unintentional: AI Governance through Multi-Level EGT, EPT, and Constitutional Self-Restraint | [10.5281/zenodo.18735857](https://doi.org/10.5281/zenodo.18735857) |
| 2026-02-21 | The Political Model Canvas: Mapping Argentina's Competing Institutional Regimes | [10.5281/zenodo.18725959](https://doi.org/10.5281/zenodo.18725959) |
| 2026-02-17 | From Ontogeny to Institutional Calcification: Group Membership Bias as the Cognitive Engine of Asymmetric Legal Persistence | [10.5281/zenodo.18673365](https://doi.org/10.5281/zenodo.18673365) |
| 2026-02-16 | From Free Rider to Free Raider: How Non-Enforcement Cascades Destroy Anonymous Cooperation | [10.5281/zenodo.18665967](https://doi.org/10.5281/zenodo.18665967) |
| 2026-02-16 | Road to Connivance: Common Knowledge, Inverted Charity, and the Evolutionary Stability of Clientelistic Populism | [10.5281/zenodo.18654069](https://doi.org/10.5281/zenodo.18654069) |
| 2026-02-16 | Extended Phenotype Legal Theory: Equilibrium Refinements and Cultural-Legal Index 3.0 | [10.5281/zenodo.18653958](https://doi.org/10.5281/zenodo.18653958) |
| 2026-02-12 | Argentina's Fiscal Lock-in: Tax Reform as Extended Phenotype | [10.5281/zenodo.18626683](https://doi.org/10.5281/zenodo.18626683) |
| 2026-02-12 | Law as Extended Phenotype: Reframing Legal Theory Through Evolutionary Epistemology | [10.5281/zenodo.18626632](https://doi.org/10.5281/zenodo.18626632) |
| 2026-02-12 | From Transaction Costs to Memetic Fitness: Formalizing Douglass North's Institutional Insights Through EPT | [10.5281/zenodo.18626473](https://doi.org/10.5281/zenodo.18626473) |
| 2026-02-12 | The WEIRD Veil: Why Rawlsian Justice May Not Generalize Beyond Its Cultural Origins | [10.5281/zenodo.18625895](https://doi.org/10.5281/zenodo.18625895) |
| 2026-02-11 | The Reciprocity Trap: A Game-Theoretic Analysis of How Cooperative Norms Undermine Institutional Integrity | [10.5281/zenodo.18615279](https://doi.org/10.5281/zenodo.18615279) |
| 2026-02-10 | The Canary in the Mine: Game Theory as Diagnostic Instrument for the Erosion of Human Agency | [10.5281/zenodo.18604030](https://doi.org/10.5281/zenodo.18604030) |
| 2026-02-10 | From Hive Minds to Administered Minds: A Formal Theory of Agency Collapse and Emergent Macro-Agency | [10.5281/zenodo.18604015](https://doi.org/10.5281/zenodo.18604015) |
| 2026-02-10 | Asymmetric Intentionality in Legal Games: When Players Operate at Different Intentional Levels | [10.5281/zenodo.18603990](https://doi.org/10.5281/zenodo.18603990) |
| 2026-02-10 | The Dennett-Nash Gap in Corporate Enforcement: Why Corporations Recidivate More Than Individuals | [10.5281/zenodo.18603603](https://doi.org/10.5281/zenodo.18603603) |
| 2026-02-10 | Corporate Criminal Liability and the Impossibility of Mens Rea: Why Guilty Minds Require Moral Agents | [10.5281/zenodo.18603564](https://doi.org/10.5281/zenodo.18603564) |
| 2026-02-10 | Evolutionarily Stable Non-Compliance: A Game-Theoretic Analysis of Corporate Governance Failures | [10.5281/zenodo.18603260](https://doi.org/10.5281/zenodo.18603260) |
| 2026-02-10 | Agency Heterogeneous Intentionality: How Corporate Structure Transforms Moral Agents into Optimization Outputs | [10.5281/zenodo.18603217](https://doi.org/10.5281/zenodo.18603217) |
| 2026-02-10 | The Generalized Intentionality Mismatch Theorem: When Law Assumes Moral Agency That Doesn't Exist | [10.5281/zenodo.18603169](https://doi.org/10.5281/zenodo.18603169) |
| 2026-02-10 | The Normative Calculation Problem Under Heterogeneous Intentionality: Why Effective Enforcement Requires Price Mechanisms | [10.5281/zenodo.18603037](https://doi.org/10.5281/zenodo.18603037) |
| 2026-02-10 | Game Theory's Hidden Assumption: Intentionality Homogeneity and the Failure of Corporate Criminal Liability | [10.5281/zenodo.18600364](https://doi.org/10.5281/zenodo.18600364) |
| 2026-02-10 | Beyond WEIRD Bias: Why Token-Based Legal AI Cannot Model Post-Colonial Compliance Dynamics | [10.5281/zenodo.18576911](https://doi.org/10.5281/zenodo.18576911) |
| 2026-02-09 | The Dawkins-Hayek Convergence: Spontaneous Order as Extended Phenotype | [10.5281/zenodo.18576674](https://doi.org/10.5281/zenodo.18576674) |
| 2026-02-09 | Law as Language: From Scandinavian Realism to Evolutionary Jurisprudence | [10.5281/zenodo.18576390](https://doi.org/10.5281/zenodo.18576390) |
| 2026-02-09 | The Extended Phenotype of Artificial Intelligence: Model Collapse and the Anthropic Settlement as Cognitive Selection Pressure | [10.5281/zenodo.18567734](https://doi.org/10.5281/zenodo.18567734) |
| 2026-02-09 | Two Paths, One Evolution: Testing the Extended Phenotype Theory Across Legal Systems | [10.5281/zenodo.18567507](https://doi.org/10.5281/zenodo.18567507) |
| 2026-02-09 | Law as Extended Phenotype: Toward an Evolutionary Theory of Legal Systems | [10.5281/zenodo.18567125](https://doi.org/10.5281/zenodo.18567125) |
| 2026-02-09 | The Legislator as Extended Phenotype: A Darwinian Theory of Legal Evolution | [10.5281/zenodo.18566652](https://doi.org/10.5281/zenodo.18566652) |
| 2026-02-09 | Jurists as Evolutionary Engineers: Artificial Selection in Legal Doctrine | [10.5281/zenodo.18564668](https://doi.org/10.5281/zenodo.18564668) |
| 2026-02-09 | The Altruism Paradox in Law: How Selfish Genes Create Cooperative Legal Orders | [10.5281/zenodo.18562865](https://doi.org/10.5281/zenodo.18562865) |
| 2026-02-09 | Dead Language, Living Law: Latin Legal Maxims as Perfect Memes | [10.5281/zenodo.18556003](https://doi.org/10.5281/zenodo.18556003) |

---

## Papers — SSRN Archive (62 papers, PDF hosted here)

> The SSRN account was suspended in January 2026 for administrative reasons (category mismatch for interdisciplinary papers), unrelated to content. All PDFs are hosted in the [`papers/`](papers/) folder of this repository.

| SSRN ID | Title | PDF |
|---------|-------|-----|
| [5387400](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5387400) | The Legislator as Extended Phenotype: A Darwinian Theory of Legal Evolution | [PDF](papers/5387400-The-Legislator-as-Extended-Phenotype-A-Darwinian-T.pdf) |
| [5391036](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5391036) | Two Paths, One Evolution: Testing the Extended Phenotype Theory Across Legal Systems | [PDF](papers/5391036-Two-Paths-One-Evolution-Testing-the.pdf) |
| [5402461](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5402461) | Constitutional Lock-in and the Phenotypic Expression of Legal Resistance | [PDF](papers/5402461-Law-as-Language-From-Scandinavian.pdf) |
| [5405459](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5405459) | JurisRank: Measuring Legal Phenotypic Fitness Through Citation Networks | [PDF](papers/5405459-JurisRank-Measuring-Legal-Phenotypic-Fitness-Throu.pdf) |
| [5428374](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5428374) | Evolutionary Genealogy of Corporate Criminal Liability | [PDF](papers/5428374-Evolutionary-Genealogy-of-Corporate-Criminal-Liabi.pdf) |
| [5454256](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5454256) | The Extended Phenotype of Artificial Intelligence | [PDF](papers/5454256-The-Extended-Phenotype-of-Artificial-Intelligence.pdf) |
| [5463814](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5463814) | The Extended Phenotype of Populism | [PDF](papers/5463814-THE-EXTENDED-PHENOTYPE-OF-POPULISM.pdf) |
| [5467928](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5467928) | The Peralta Metamorphosis: Quantifying the Evolution of Legal Parasitism | [PDF](papers/5467928-The-Peralta-Metamorphosis-Quantifying-the-Evolutio.pdf) |
| [5468569](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5468569) | The Multilayer Parasite: Quantifying Corruption's Institutional Architecture | [PDF](papers/5468569-The-Multilayer-Parasite-Quantifying-Corruptions.pdf) |
| [5472748](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5472748) | The Cuckoo's Superestimulus: A Theoretical Framework | [PDF](papers/5472748-The-Cuckoos-Superestimulus-A-Theoretical-Framework.pdf) |
| [5477267](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5477267) | Computational Genealogies and Political Attractors | [PDF](papers/5477267-Computational-Genealogies-and-Political-Attractors.pdf) |
| [5478426](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5478426) | Why Bad Law Persists: Evolutionarily Stable Strategies in Legal Systems | [PDF](papers/5478426-Why-Bad-Law-Persists-Evolutionary-Stable-Strategie.pdf) |
| [5478466](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5478466) | The Altruism Paradox in Law: How Selfish Genes Create Cooperative Legal Orders | [PDF](papers/5478466-The-Altruism-Paradox-in-Law-How-Selfish-Genes-Crea.pdf) |
| [5478467](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5478467) | The Legal DNA: How Behavioral and Evolutionary Forces Shape Legal Norms | [PDF](papers/5478467-The-Legal-DNA-How-Behavioral-and.pdf) |
| [5486006](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5486006) | Dead Language, Living Law: Latin Legal Maxims as Perfect Memes | [PDF](papers/5486006-Dead-Language-Living-Law-Latin-Legal-Maxims-as.pdf) |
| [5486466](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5486466) | Good Faith as Legal DNA: The Genealogical Origins of Contractual Loyalty | [PDF](papers/5486466-GOOD-FAITH-AS-LEGAL-DNA-THE-GENEALOGICAL.pdf) |
| [5492066](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5492066) | Jurists as Evolutionary Engineers: Artificial Selection in Legal Doctrine | [PDF](papers/5492066-JURISTS-AS-EVOLUTIONARY-ENGINEERS-ARTIFICIAL.pdf) |
| [5496678](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5496678) | The Legal Book of the Dead: Memetic Pincers and Institutional Palimpsests | [PDF](papers/5496678-The-Legal-Book-of-the-Dead-Memetic-Pincers.pdf) |
| [5555478](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5555478) | Small Concept Models: A Specialized Framework for Legal AI | [PDF](papers/5555478-Small-Concept-Models-A-Specialized-Framework-for.pdf) |
| [5557838](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5557838) | IusSpace: A Twelve-Dimensional Framework for Mapping Legal Concepts | [PDF](papers/5557838-IusSpace-A-Twelve-Dimensional-Framework-for-Mappin.pdf) |
| [5576850](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5576850) | Beyond WEIRD Legal AI: Why Concept-Based Models Outperform Token-Based Approaches | [PDF](papers/5576850-Beyond-WEIRD-Legal-AI-Why-Concept-Based-Models.pdf) |
| [5584450](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5584450) | Beyond WEIRD Bias: Why Token-Based Legal AI Cannot Model Post-Colonial Compliance | [PDF](papers/5584450-Beyond-WEIRD-Bias-Why-Token-Based-Legal-AI.pdf) |
| [5591832](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5591832) | Normative Ambiguity as Memetic Niche Space | [PDF](papers/5591832-Normative-Ambiguity-as-Memetic-Niche-Space-An.pdf) |
| [5593470](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5593470) | Law as Extended Phenotype: Toward an Evolutionary Theory of Legal Systems | [PDF](papers/5593470-Law-as-Extended-Phenotype-Toward-an.pdf) |
| [5599553](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5599553) | The Extinction of the Nineteenth Amendment: A Memetic Analysis | [PDF](papers/5599553-THE-EXTINCTION-OF-THE-NINETEENTH-AMENDMENT.pdf) |
| [5600750](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5600750) | Beyond Iusmorphs: Advanced Evolutionary Models for Legal Compatibility | [PDF](papers/5600750-Beyond-Iusmorphs-Advanced-Evolutionary-Models.pdf) |
| [5605730](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5605730) | Beyond Iusmorphs: Environmental Compatibility and Institutional Selection | [PDF](papers/5605730-Beyond-Iusmorphs-Environmental-Compatibility.pdf) |
| [5612010](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5612010) | International Law as Extended Phenotype: Globalist and Sovereignist Memeplexes | [PDF](papers/5612010-International-Law-as-Extended-Phenotype-Globalist.pdf) |
| [5624710](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5624710) | Constitutional Lock-in and the Phenotypic Expression of Legal Resistance | [PDF](papers/5624710-Constitutional-Lock-in-and-the-Phenotypic.pdf) |
| [5635152](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5635152) | Argentina's Fiscal Lock-in: Tax Reform as Extended Phenotype | [PDF](papers/5635152-Argentinas-Fiscal-Lock-in-Tax-Reform-as.pdf) |
| [5645070](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5645070) | Climbing Mount Improbable: A Viable Path for Argentine Institutional Reform | [PDF](papers/5645070-CLIMBING-MOUNT-IMPROBABLE-A-VIABLE-PATH.pdf) |
| [5660770](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5660770) | Constitutional Paleontology: Tracing the Evolutionary History of Legal Doctrines | [PDF](papers/5660770-CONSTITUTIONAL-PALEONTOLOGY-TRACING.pdf) |
| [5695662](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5695662) | Before the Command Was Spoken: Law as Pre-Intentional Coordination | [PDF](papers/5695662-Before-the-Command-Was-Spoken-Law-as.pdf) |
| [5696484](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5696484) | The Grundnorm as Evolutionary Attractor | [PDF](papers/5696484-The-Grundnorm-as-Evolutionary.pdf) |
| [5718922](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5718922) | Cognitive Mechanisms of Constitutional Entrenchment | [PDF](papers/5718922-COGNITIVE-MECHANISMS-OF-CONSTITUTIONAL.pdf) |
| [5728083](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5728083) | The Golden Ratio Paradox: Why Optimal Institutional Design May Be Evolutionarily Unstable | [PDF](papers/5728083-The-Golden-Ratio-Paradox-Why-Optimal-Institutional.pdf) |
| [5731627](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5731627) | From Utopianism to Fossilization: The Evolutionary Pathology of Ideal Constitutions | [PDF](papers/5731627-FROM-UTOPIANISM-TO-FOSSILIZATION-A.pdf) |
| [5737383](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5737383) | Law as Extended Phenotype: Reframing Legal Theory Through Evolutionary Epistemology | [PDF](papers/5737383-LAW-AS-EXTENDED-PHENOTYPE-REFRAMING.pdf) |
| [5741544](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5741544) | If Machiavelli Had Known Darwin: Evolutionary Power and Institutional Design | [PDF](papers/5741544-IF-MACHIAVELLI-HAD-KNOWN-DARWIN-EVOLUTIONARY.pdf) |
| [5748142](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5748142) | Uruguay and the Fossilization Meme: Testing EPT Against a Positive Case | [PDF](papers/5748142-Uruguay-and-the-Fossilization-Meme-Testing.pdf) |
| [5750242](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5750242) | From Transaction Costs to Memetic Fitness: Formalizing North's Institutional Insights | [PDF](papers/5750242-FROM-TRANSACTION-COSTS-TO-MEMETIC-FITNESS.pdf) |
| [5760142](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5760142) | Beyond Stated Preferences: Tacit Consensus as Cultural Lock-in | [PDF](papers/5760142-Beyond-Stated-Preferences-Tacit-Consensus-as-Cultu.pdf) |
| [5768423](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5768423) | Epistemological Clergies: When Orthodoxy Becomes Institutional Selection Pressure | [PDF](papers/5768423-EPISTEMOLOGICAL-CLERGIES-WHEN-ORTHODOXY.pdf) |
| [5776925](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5776925) | "General Welfare" and "Common Good" as Evolutionary Attractors in Constitutional Law | [PDF](papers/5776925-General-Welfare-and-Common-Good-as-Evolutionary.pdf) |
| [5881663](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5881663) | The Dawkins-Hayek Convergence: Spontaneous Order as Extended Phenotype | [PDF](papers/5881663-The-Dawkins-Hayek-Convergence-Spontaneous.pdf) |
| [5881702](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5881702) | Against Multilevel Selection in Legal Evolution: A Defense and Restatement | [PDF](papers/5881702-Against-Multilevel-Selection-in-Legal-Evolution.pdf) |
| [5882342](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5882342) | Archaeological Scaffolding of Law: Institutional Layers and Memetic Stratigraphy | [PDF](papers/5882342-ARCHAEOLOGICAL-SCAFFOLDING-OF-LAW.pdf) |
| [5886142](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5886142) | Blind Breeders: The Extended Phenotype of Unintentional Institutional Design | [PDF](papers/5886142-BLIND-BREEDERS-The-Extended-Phenotype-of.pdf) |
| [5891884](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5891884) | Law as Extended Phenotype: A Game-Theoretic Synthesis | [PDF](papers/5891884-Law-as-Extended-Phenotype-A-Game-Theoretic.pdf) |
| [5908462](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5908462) | The Praxeological Foundations of Extended Phenotype Theory | [PDF](papers/5908462-The-Praxeological-Foundations-of-Extended.pdf) |
| [5908662](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5908662) | Legal Prices: The Normative Calculation Problem and the Limits of Command-and-Control | [PDF](papers/5908662-Legal-Prices-The-Normative-Calculation-Problem-and.pdf) |
| [5955735](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5955735) | The WEIRD Machine: Why Western Legal AI Fails in Non-WEIRD Jurisdictions | [PDF](papers/5955735-THE-WEIRD-MACHINE-WHY-WESTERN.pdf) |
| [5960677](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5960677) | Game Theory's Hidden Assumption: Intentionality Homogeneity and Corporate Liability | [PDF](papers/5960677-GAME-THEORYS-HIDDEN-ASSUMPTION-Intentionality.pdf) |
| [5971914](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5971914) | Mises's Fatal Flaw: Binding Deficits and the Memetic Evolution of Fiscal Constitutions | [PDF](papers/5971914-Misess-Fatal-Flaw-Binding-Deficits-and-the-Memetic.pdf) |
| [5974555](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5974555) | Formal Foundations of Multilevel Game Theory: Price Equation and Replicator Dynamics | [PDF](papers/5974555-Formal-Foundations-of-Multilevel-Game-Theory.pdf) |
| [5991115](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5991115) | Extending Aumann's Agreement Theorem to Heterogeneous Intentionality | [PDF](papers/5991115-Extending-Aumanns-Agreement-Theorem-to.pdf) |
| [5991195](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5991195) | The Generalized Intentionality Mismatch Theorem: When Law Assumes Moral Agency That Doesn't Exist | [PDF](papers/5991195-The-Generalized-Intentionality-Mismatch-Theorem.pdf) |
| [5991355](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5991355) | Environmental Law and the Myth of Corporate Citizenship | [PDF](papers/5991355-Environmental-Law-and-the-Myth-of-Corporate.pdf) |
| [5995234](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5995234) | The Normative Calculation Problem Under Heterogeneous Intentionality | [PDF](papers/5995234-The-Normative-Calculation-Problem-Under.pdf) |
| [5995435](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5995435) | Agency Problems Under Heterogeneous Intentionality | [PDF](papers/5995435-Agency-Problems-Under-Heterogeneous.pdf) |
| [6000675](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6000675) | Evolutionarily Stable Non-Compliance: A Game-Theoretic Analysis | [PDF](papers/6000675-Evolutionarily-Stable-Non-Compliance-A-Game.pdf) |
| [6001434](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6001434) | The Fatal Conceit of Consensus Networks: Why Decentralized Governance Fails | [PDF](papers/6001434-The-Fatal-Conceit-of-Consensus-Networks-Why.pdf) |

---

## Published Articles

| Title | Journal | DOI |
|-------|---------|-----|
| Computational Detection of Constitutional Drift: Network Analysis and Semantic Measurement of Argentine Supreme Court Jurisprudence (1922–2025) | *Journal of Computational Law and Legal Technology* | [10.47852/bonviewJCLLT62027951](https://doi.org/10.47852/bonviewJCLLT62027951) |

---

## Journals Under Review

| Manuscript | Title | Journal | Status |
|-----------|-------|---------|--------|
| #9516 | Predatory Invitations as Extended Phenotype | JCLLT | Under review |

---

## How to Cite

```
Lerer, I.A. (year). [Title]. [SSRN Working Paper ID / Zenodo DOI].
Available: https://github.com/adrianlerer/lerer-research-program
```
