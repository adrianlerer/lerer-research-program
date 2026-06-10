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

His research program applies Dawkins's (1982) Extended Phenotype Theory and Dennett's intentionality hierarchy to legal institutions, producing a suite of quantitative diagnostic instruments validated against empirical datasets from four jurisdictions. He maintains 125 Zenodo DOI records and 62 SSRN records, with all SSRN archive entries cross-referenced to their Zenodo records, and has one article published and one manuscript under review at the *Journal of Computational Law and Legal Technology* (JCLLT).

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

## Papers — Zenodo (125 DOI records, open access)

All papers are freely downloadable. Communities: [law-as-extended-phenotype](https://zenodo.org/communities/law-as-extended-phenotype/) · [small-concept-models](https://zenodo.org/communities/small-concept-models/).

| Date | Title | DOI |
|------|-------|-----|
| 2026-06-10 | Regulatory Prophecy as Parasitic Spontaneous Order: Epistemological Clergy, Panic Memes, and the Distortion of AI Governance | [10.5281/zenodo.20630052](https://doi.org/10.5281/zenodo.20630052) · [PDF](papers/20630052-Regulatory-Prophecy-as-Parasitic-Spontaneous-Order-v2.pdf) |
| 2026-06-09 | The Race to the Bottom as a Between-Level Selection Failure: Listing-Standards Competition, Governance as Extended Phenotype, and the Coalition Behind the Trust Argument | [10.5281/zenodo.20618956](https://doi.org/10.5281/zenodo.20618956) · [PDF](papers/20618956-The-Race-to-the-Bottom-as-Between-Level-Selection-Failure.pdf) |
| 2026-06-09 | Outcome Control as Constitutional Constraint: The Argentine Model for Autonomous Legal Entities | [10.5281/zenodo.20613712](https://doi.org/10.5281/zenodo.20613712) · [PDF](papers/20613712-Outcome-Control-as-Constitutional-Constraint.pdf) |
| 2026-06-09 | JurisRank: Measuring Legal Phenotypic Fitness Through Citation Networks | [10.5281/zenodo.20613103](https://doi.org/10.5281/zenodo.20613103) · [PDF](papers/20613103-JurisRank-Measuring-Legal-Phenotypic-Fitness-Through-Citation-Networks.pdf) |
| 2026-06-09 | The Fatal Conceit of Consensus Networks: Why Decentralized Governance Fails | [10.5281/zenodo.20612976](https://doi.org/10.5281/zenodo.20612976) · [PDF](papers/20612976-The-Fatal-Conceit-of-Consensus-Networks-Why-Decentralized-Governance-Fails.pdf) |
| 2026-06-09 | Agency Problems Under Heterogeneous Intentionality | [10.5281/zenodo.20612974](https://doi.org/10.5281/zenodo.20612974) · [PDF](papers/20612974-Agency-Problems-Under-Heterogeneous-Intentionality.pdf) |
| 2026-06-09 | Environmental Law and the Myth of Corporate Citizenship | [10.5281/zenodo.20612972](https://doi.org/10.5281/zenodo.20612972) · [PDF](papers/20612972-Environmental-Law-and-the-Myth-of-Corporate-Citizenship.pdf) |
| 2026-06-09 | Extending Aumann's Agreement Theorem to Heterogeneous Intentionality | [10.5281/zenodo.20612968](https://doi.org/10.5281/zenodo.20612968) · [PDF](papers/20612968-Extending-Aumann-s-Agreement-Theorem-to-Heterogeneous-Intentionality.pdf) |
| 2026-06-09 | Formal Foundations of Multilevel Game Theory: Price Equation and Replicator Dynamics | [10.5281/zenodo.20612964](https://doi.org/10.5281/zenodo.20612964) · [PDF](papers/20612964-Formal-Foundations-of-Multilevel-Game-Theory-Price-Equation-and-Replicator-Dynamics.pdf) |
| 2026-06-09 | Mises's Fatal Flaw: Binding Deficits and the Memetic Evolution of Fiscal Constitutions | [10.5281/zenodo.20612960](https://doi.org/10.5281/zenodo.20612960) · [PDF](papers/20612960-Mises-s-Fatal-Flaw-Binding-Deficits-and-the-Memetic-Evolution-of-Fiscal-Constitutions.pdf) |
| 2026-06-09 | The WEIRD Machine: Why Western Legal AI Fails in Non-WEIRD Jurisdictions | [10.5281/zenodo.20612958](https://doi.org/10.5281/zenodo.20612958) · [PDF](papers/20612958-The-WEIRD-Machine-Why-Western-Legal-AI-Fails-in-Non-WEIRD-Jurisdictions.pdf) |
| 2026-06-09 | Legal Prices: The Normative Calculation Problem and the Limits of Command-and-Control | [10.5281/zenodo.20612954](https://doi.org/10.5281/zenodo.20612954) · [PDF](papers/20612954-Legal-Prices-The-Normative-Calculation-Problem-and-the-Limits-of-Command-and-Control.pdf) |
| 2026-06-09 | The Praxeological Foundations of Extended Phenotype Theory | [10.5281/zenodo.20612952](https://doi.org/10.5281/zenodo.20612952) · [PDF](papers/20612952-The-Praxeological-Foundations-of-Extended-Phenotype-Theory.pdf) |
| 2026-06-09 | Law as Extended Phenotype: A Game-Theoretic Synthesis | [10.5281/zenodo.20612950](https://doi.org/10.5281/zenodo.20612950) · [PDF](papers/20612950-Law-as-Extended-Phenotype-A-Game-Theoretic-Synthesis.pdf) |
| 2026-06-09 | Blind Breeders: The Extended Phenotype of Unintentional Institutional Design | [10.5281/zenodo.20612948](https://doi.org/10.5281/zenodo.20612948) · [PDF](papers/20612948-Blind-Breeders-The-Extended-Phenotype-of-Unintentional-Institutional-Design.pdf) |
| 2026-06-09 | Archaeological Scaffolding of Law: Institutional Layers and Memetic Stratigraphy | [10.5281/zenodo.20612939](https://doi.org/10.5281/zenodo.20612939) · [PDF](papers/20612939-Archaeological-Scaffolding-of-Law-Institutional-Layers-and-Memetic-Stratigraphy.pdf) |
| 2026-06-09 | Against Multilevel Selection in Legal Evolution: A Defense and Restatement | [10.5281/zenodo.20612935](https://doi.org/10.5281/zenodo.20612935) · [PDF](papers/20612935-Against-Multilevel-Selection-in-Legal-Evolution-A-Defense-and-Restatement.pdf) |
| 2026-06-09 | "General Welfare" and "Common Good" as Evolutionary Attractors in Constitutional Law | [10.5281/zenodo.20612927](https://doi.org/10.5281/zenodo.20612927) · [PDF](papers/20612927-General-Welfare-and-Common-Good-as-Evolutionary-Attractors-in-Constitutional-Law.pdf) |
| 2026-06-09 | Epistemological Clergies: When Orthodoxy Becomes Institutional Selection Pressure | [10.5281/zenodo.20612925](https://doi.org/10.5281/zenodo.20612925) · [PDF](papers/20612925-Epistemological-Clergies-When-Orthodoxy-Becomes-Institutional-Selection-Pressure.pdf) |
| 2026-06-09 | Beyond Stated Preferences: Tacit Consensus as Cultural Lock-in | [10.5281/zenodo.20612923](https://doi.org/10.5281/zenodo.20612923) · [PDF](papers/20612923-Beyond-Stated-Preferences-Tacit-Consensus-as-Cultural-Lock-in.pdf) |
| 2026-06-09 | Uruguay and the Fossilization Meme: Testing EPT Against a Positive Case | [10.5281/zenodo.20612916](https://doi.org/10.5281/zenodo.20612916) · [PDF](papers/20612916-Uruguay-and-the-Fossilization-Meme-Testing-EPT-Against-a-Positive-Case.pdf) |
| 2026-06-09 | If Machiavelli Had Known Darwin: Evolutionary Power and Institutional Design | [10.5281/zenodo.20612914](https://doi.org/10.5281/zenodo.20612914) · [PDF](papers/20612914-If-Machiavelli-Had-Known-Darwin-Evolutionary-Power-and-Institutional-Design.pdf) |
| 2026-06-09 | From Utopianism to Fossilization: The Evolutionary Pathology of Ideal Constitutions | [10.5281/zenodo.20612910](https://doi.org/10.5281/zenodo.20612910) · [PDF](papers/20612910-From-Utopianism-to-Fossilization-The-Evolutionary-Pathology-of-Ideal-Constitutions.pdf) |
| 2026-06-09 | The Golden Ratio Paradox: Why Optimal Institutional Design May Be Evolutionarily Unstable | [10.5281/zenodo.20612906](https://doi.org/10.5281/zenodo.20612906) · [PDF](papers/20612906-The-Golden-Ratio-Paradox-Why-Optimal-Institutional-Design-May-Be-Evolutionarily-Unstab.pdf) |
| 2026-06-09 | Cognitive Mechanisms of Constitutional Entrenchment | [10.5281/zenodo.20612904](https://doi.org/10.5281/zenodo.20612904) · [PDF](papers/20612904-Cognitive-Mechanisms-of-Constitutional-Entrenchment.pdf) |
| 2026-06-09 | The Grundnorm as Evolutionary Attractor | [10.5281/zenodo.20612900](https://doi.org/10.5281/zenodo.20612900) · [PDF](papers/20612900-The-Grundnorm-as-Evolutionary-Attractor.pdf) |
| 2026-06-09 | Before the Command Was Spoken: Law as Pre-Intentional Coordination | [10.5281/zenodo.20612892](https://doi.org/10.5281/zenodo.20612892) · [PDF](papers/20612892-Before-the-Command-Was-Spoken-Law-as-Pre-Intentional-Coordination.pdf) |
| 2026-06-09 | Constitutional Paleontology: Tracing the Evolutionary History of Legal Doctrines | [10.5281/zenodo.20612890](https://doi.org/10.5281/zenodo.20612890) · [PDF](papers/20612890-Constitutional-Paleontology-Tracing-the-Evolutionary-History-of-Legal-Doctrines.pdf) |
| 2026-06-09 | Climbing Mount Improbable: A Viable Path for Argentine Institutional Reform | [10.5281/zenodo.20612887](https://doi.org/10.5281/zenodo.20612887) · [PDF](papers/20612887-Climbing-Mount-Improbable-A-Viable-Path-for-Argentine-Institutional-Reform.pdf) |
| 2026-06-09 | Constitutional Lock-in and the Phenotypic Expression of Legal Resistance | [10.5281/zenodo.20612883](https://doi.org/10.5281/zenodo.20612883) · [PDF](papers/20612883-Constitutional-Lock-in-and-the-Phenotypic-Expression-of-Legal-Resistance.pdf) |
| 2026-06-09 | International Law as Extended Phenotype: Globalist and Sovereignist Memeplexes | [10.5281/zenodo.20612876](https://doi.org/10.5281/zenodo.20612876) · [PDF](papers/20612876-International-Law-as-Extended-Phenotype-Globalist-and-Sovereignist-Memeplexes.pdf) |
| 2026-06-09 | Beyond Iusmorphs: Environmental Compatibility and Institutional Selection | [10.5281/zenodo.20612872](https://doi.org/10.5281/zenodo.20612872) · [PDF](papers/20612872-Beyond-Iusmorphs-Environmental-Compatibility-and-Institutional-Selection.pdf) |
| 2026-06-09 | Beyond Iusmorphs: Advanced Evolutionary Models for Legal Compatibility | [10.5281/zenodo.20612864](https://doi.org/10.5281/zenodo.20612864) · [PDF](papers/20612864-Beyond-Iusmorphs-Advanced-Evolutionary-Models-for-Legal-Compatibility.pdf) |
| 2026-06-09 | The Extinction of the Nineteenth Amendment: A Memetic Analysis | [10.5281/zenodo.20612860](https://doi.org/10.5281/zenodo.20612860) · [PDF](papers/20612860-The-Extinction-of-the-Nineteenth-Amendment-A-Memetic-Analysis.pdf) |
| 2026-06-09 | Normative Ambiguity as Memetic Niche Space | [10.5281/zenodo.20612858](https://doi.org/10.5281/zenodo.20612858) · [PDF](papers/20612858-Normative-Ambiguity-as-Memetic-Niche-Space.pdf) |
| 2026-06-09 | Beyond WEIRD Legal AI: Why Concept-Based Models Outperform Token-Based Approaches | [10.5281/zenodo.20612854](https://doi.org/10.5281/zenodo.20612854) · [PDF](papers/20612854-Beyond-WEIRD-Legal-AI-Why-Concept-Based-Models-Outperform-Token-Based-Approaches.pdf) |
| 2026-06-09 | IusSpace: A Twelve-Dimensional Framework for Mapping Legal Concepts | [10.5281/zenodo.20612852](https://doi.org/10.5281/zenodo.20612852) · [PDF](papers/20612852-IusSpace-A-Twelve-Dimensional-Framework-for-Mapping-Legal-Concepts.pdf) |
| 2026-06-09 | Small Concept Models: A Specialized Framework for Legal AI | [10.5281/zenodo.20612850](https://doi.org/10.5281/zenodo.20612850) · [PDF](papers/20612850-Small-Concept-Models-A-Specialized-Framework-for-Legal-AI.pdf) |
| 2026-06-09 | The Legal Book of the Dead: Memetic Pincers and Institutional Palimpsests | [10.5281/zenodo.20612848](https://doi.org/10.5281/zenodo.20612848) · [PDF](papers/20612848-The-Legal-Book-of-the-Dead-Memetic-Pincers-and-Institutional-Palimpsests.pdf) |
| 2026-06-09 | Good Faith as Legal DNA: The Genealogical Origins of Contractual Loyalty | [10.5281/zenodo.20612844](https://doi.org/10.5281/zenodo.20612844) · [PDF](papers/20612844-Good-Faith-as-Legal-DNA-The-Genealogical-Origins-of-Contractual-Loyalty.pdf) |
| 2026-06-09 | The Legal DNA: How Behavioral and Evolutionary Forces Shape Legal Norms | [10.5281/zenodo.20612842](https://doi.org/10.5281/zenodo.20612842) · [PDF](papers/20612842-The-Legal-DNA-How-Behavioral-and-Evolutionary-Forces-Shape-Legal-Norms.pdf) |
| 2026-06-09 | Why Bad Law Persists: Evolutionarily Stable Strategies in Legal Systems | [10.5281/zenodo.20612840](https://doi.org/10.5281/zenodo.20612840) · [PDF](papers/20612840-Why-Bad-Law-Persists-Evolutionarily-Stable-Strategies-in-Legal-Systems.pdf) |
| 2026-06-09 | Computational Genealogies and Political Attractors | [10.5281/zenodo.20612837](https://doi.org/10.5281/zenodo.20612837) · [PDF](papers/20612837-Computational-Genealogies-and-Political-Attractors.pdf) |
| 2026-06-09 | The Cuckoo's Superestimulus: A Theoretical Framework | [10.5281/zenodo.20612835](https://doi.org/10.5281/zenodo.20612835) · [PDF](papers/20612835-The-Cuckoo-s-Superestimulus-A-Theoretical-Framework.pdf) |
| 2026-06-09 | The Multilayer Parasite: Quantifying Corruption's Institutional Architecture | [10.5281/zenodo.20612833](https://doi.org/10.5281/zenodo.20612833) · [PDF](papers/20612833-The-Multilayer-Parasite-Quantifying-Corruption-s-Institutional-Architecture.pdf) |
| 2026-06-09 | The Peralta Metamorphosis: Quantifying the Evolution of Legal Parasitism | [10.5281/zenodo.20612829](https://doi.org/10.5281/zenodo.20612829) · [PDF](papers/20612829-The-Peralta-Metamorphosis-Quantifying-the-Evolution-of-Legal-Parasitism.pdf) |
| 2026-06-09 | The Extended Phenotype of Populism | [10.5281/zenodo.20612821](https://doi.org/10.5281/zenodo.20612821) · [PDF](papers/20612821-The-Extended-Phenotype-of-Populism.pdf) |
| 2026-06-09 | Evolutionary Genealogy of Corporate Criminal Liability | [10.5281/zenodo.20612819](https://doi.org/10.5281/zenodo.20612819) · [PDF](papers/20612819-Evolutionary-Genealogy-of-Corporate-Criminal-Liability.pdf) |
| 2026-06-06 | Simulation Is Not Adjudication Institutional Admissibility and the Boundary Between Machine Output and Legal Consequence | [10.5281/zenodo.20563879](https://doi.org/10.5281/zenodo.20563879) · [PDF](papers/20563879-Simulation-Is-Not-Adjudication-Institutional-Admissibility-and-the-Boundary-Between-Ma.pdf) |
| 2026-06-01 | Runtime Admissibility Before Reliance: Legitimacy Formation and Legitimacy Execution in Legal AI | [10.5281/zenodo.20501821](https://doi.org/10.5281/zenodo.20501821) · [PDF](papers/20501821-Runtime-Admissibility-Before-Reliance-Legitimacy-Formation-and-Legitimacy-Execution-in.pdf) |
| 2026-05-31 | REGULATORY CAPTURE AS EVOLUTIONARILY STABLE STRATEGY: TOWARD A REGULATORY CAPTURE PRESUMPTION IN DISCRETIONARY REGULATION | [10.5281/zenodo.20479541](https://doi.org/10.5281/zenodo.20479541) · [PDF](papers/20479541-REGULATORY-CAPTURE-AS-EVOLUTIONARILY-STABLE-STRATEGY-TOWARD-A-REGULATORY-CAPTURE-PRESU.pdf) |
| 2026-05-27 | Synthetic Populations as Institutional Stress Tests: Constitutional Lock-In and Model-Specific Phase Transitions in LLM Synthetic Societies | [10.5281/zenodo.20405441](https://doi.org/10.5281/zenodo.20405441) · [DOCX](papers/20405441-Synthetic-Populations-as-Institutional-Stress-Tests-Constitutional-Lock-In-and-Model-S.docx) |
| 2026-05-15 | Absolute Metaphors, Perfect Memes, and the LLMorphism Problem: Two Layers of Legal Genealogy | [10.5281/zenodo.20206138](https://doi.org/10.5281/zenodo.20206138) · [PDF](papers/20206138-Absolute-Metaphors-Perfect-Memes-and-the-LLMorphism-Problem-Two-Layers-of-Legal-Geneal.pdf) |
| 2026-05-08 | Institutions as Distributed Computations: A Unified Framework Integrating Extended Phenotype Theory, Evolutionary Game Theory, and Computational Complexity | [10.5281/zenodo.20077707](https://doi.org/10.5281/zenodo.20077707) · [PDF](papers/20077707-Institutions-as-Distributed-Computations-A-Unified-Framework-Integrating-Extended-Phen.pdf) |
| 2026-05-05 | Collective Moral Disengagement as Evolutionarily Stable Strategy (ESS): Extended Phenotype Theory and the Intra-Corporate Intentionality Paradox | [10.5281/zenodo.20032228](https://doi.org/10.5281/zenodo.20032228) · [PDF](papers/20032228-Collective-Moral-Disengagement-as-Evolutionarily-Stable-Strategy-ESS-Extended-Phenotyp.pdf) |
| 2026-04-29 | Non-Euclidean Normative Space: When Legal Hierarchies Curve Extended Phenotype Theory, Lateral Silencing, and the Geometry of Legal Systems Beyond Kelsen | [10.5281/zenodo.19898938](https://doi.org/10.5281/zenodo.19898938) · [PDF](papers/19898938-Non-Euclidean-Normative-Space-When-Legal-Hierarchies-Curve-Extended-Phenotype-Theory-L.pdf) |
| 2026-04-29 | Strategy Trendslop as Parasitic Spontaneous Order: Why Large Language Models Converge on Managerial Buzzwords Regardless of Context | [10.5281/zenodo.19867851](https://doi.org/10.5281/zenodo.19867851) · [PDF](papers/19867851-Strategy-Trendslop-as-Parasitic-Spontaneous-Order-Why-Large-Language-Models-Converge-o.pdf) |
| 2026-04-28 | Law as Constructed Niche: Reciprocal Causation Between Extended Phenotypes and Selective Environments in Institutional Evolution | [10.5281/zenodo.19839047](https://doi.org/10.5281/zenodo.19839047) · [PDF](papers/19839047-Law-as-Constructed-Niche-Reciprocal-Causation-Between-Extended-Phenotypes-and-Selectiv.pdf) |
| 2026-04-27 | Normative Collapse and Institutional Persistence in Authoritarian Regimes: A Multilevel Selection Framework with Computational Validation | [10.5281/zenodo.19806122](https://doi.org/10.5281/zenodo.19806122) · [PDF](papers/19806122-Normative-Collapse-and-Institutional-Persistence-in-Authoritarian-Regimes-A-Multilevel.pdf) |
| 2026-04-27 | AGENTS AS EXTENDED PHENOTYPES: BEHAVIORAL TRANSFER, ASYMMETRIC INTENTIONALITY, AND THE EVOLUTIONARY STABILITY OF PRIVACY DEGRADATION IN AGENTIC SYSTEMS | [10.5281/zenodo.19802281](https://doi.org/10.5281/zenodo.19802281) · [PDF](papers/19802281-AGENTS-AS-EXTENDED-PHENOTYPES-BEHAVIORAL-TRANSFER-ASYMMETRIC-INTENTIONALITY-AND-THE-EV.pdf) |
| 2026-04-24 | The Lateral Silencing Exaptation: Unenforceable Norms as Extended Phenotypes of Political Control | [10.5281/zenodo.19720028](https://doi.org/10.5281/zenodo.19720028) · [PDF](papers/19720028-The-Lateral-Silencing-Exaptation-Unenforceable-Norms-as-Extended-Phenotypes-of-Politic.pdf) |
| 2026-04-03 | The Epistemic Foundation of the Endogeneity Paradox: Common Knowledge, Intentionality Mismatch, and the Sequential Protocol | [10.5281/zenodo.19394406](https://doi.org/10.5281/zenodo.19394406) · [PDF](papers/19394406-The-Epistemic-Foundation-of-the-Endogeneity-Paradox-Common-Knowledge-Intentionality-Mi.pdf) |
| 2026-04-01 | The Concept Bottleneck as a Deterministic Evaluation Layer: Implementation of Small Concept Models for Legal Reasoning via OpenAI Structured Outputs | [10.5281/zenodo.19373345](https://doi.org/10.5281/zenodo.19373345) · [PDF](papers/19373345-The-Concept-Bottleneck-as-a-Deterministic-Evaluation-Layer-Implementation-of-Small-Con.pdf) |
| 2026-03-30 | Synthetic Minds in Normative Sandboxes: Exaptation, Spandrels, and Multilevel Selection in Agent-Based Legal Simulation | [10.5281/zenodo.19341388](https://doi.org/10.5281/zenodo.19341388) · [PDF](papers/19341388-Synthetic-Minds-in-Normative-Sandboxes-Exaptation-Spandrels-and-Multilevel-Selection-i.pdf) |
| 2026-03-30 | Judicial Lock-in as Evolutionarily Stable Strategy: The CGT Injunction Against Law 27.802 as Confirmatory Evidence for the Constitutional Lock-in Index | [10.5281/zenodo.19340088](https://doi.org/10.5281/zenodo.19340088) · [PDF](papers/19340088-Judicial-Lock-in-as-Evolutionarily-Stable-Strategy-The-CGT-Injunction-Against-Law-27-8.pdf) |
| 2026-03-30 | Predatory Invitations as Extended Phenotype: A Parasitic Spontaneous Order Analysis Across Academic and Literary Publishing | [10.5281/zenodo.19339642](https://doi.org/10.5281/zenodo.19339642) · [PDF](papers/19339642-Predatory-Invitations-as-Extended-Phenotype-A-Parasitic-Spontaneous-Order-Analysis-Acr.pdf) |
| 2026-03-29 | The Intelligence Explosion That Will Calcify: Extended Phenotype Theory, Asymmetric Intentionality, and the Evolutionary Pathologies of Agent Institutions | [10.5281/zenodo.19323303](https://doi.org/10.5281/zenodo.19323303) · [PDF](papers/19323303-The-Intelligence-Explosion-That-Will-Calcify-Extended-Phenotype-Theory-Asymmetric-Inte.pdf) |
| 2026-03-25 | Metaphors as Legal Memes: Extended Phenotype Theory, Heteronomous Bayesian Updating, and the Evolutionary Dynamics of AI Regulatory Language | [10.5281/zenodo.19226108](https://doi.org/10.5281/zenodo.19226108) · [PDF](papers/19226108-Metaphors-as-Legal-Memes-Extended-Phenotype-Theory-Heteronomous-Bayesian-Updating-and.pdf) |
| 2026-03-24 | Obiter Creep: How Marginal Dicta Colonize Ratio Decidendi Through Extended Phenotype Mechanisms | [10.5281/zenodo.19205884](https://doi.org/10.5281/zenodo.19205884) · [PDF](papers/19205884-Obiter-Creep-How-Marginal-Dicta-Colonize-Ratio-Decidendi-Through-Extended-Phenotype-Me.pdf) |
| 2026-03-24 | Lamarckian Replicators in Darwinian Hierarchies: Reconciling Gene-Centered and Multilevel Selection Approaches to Legal Evolution | [10.5281/zenodo.19199269](https://doi.org/10.5281/zenodo.19199269) · [PDF](papers/19199269-Lamarckian-Replicators-in-Darwinian-Hierarchies-Reconciling-Gene-Centered-and-Multilev.pdf) |
| 2026-03-20 | Convergent Institutional Evolution: Organized Crime as Natural Experiment for the Extended Phenotype Theory of Law | [10.5281/zenodo.19122984](https://doi.org/10.5281/zenodo.19122984) · [PDF](papers/19122984-Convergent-Institutional-Evolution-Organized-Crime-as-Natural-Experiment-for-the-Exten.pdf) |
| 2026-03-19 | Strengthening the Foundations of Law as Extended Phenotype: Coalitional Intelligence and the Evolutionary Origins of Legal Institutions | [10.5281/zenodo.19104281](https://doi.org/10.5281/zenodo.19104281) · [PDF](papers/19104281-Strengthening-the-Foundations-of-Law-as-Extended-Phenotype-Coalitional-Intelligence-an.pdf) |
| 2026-03-18 | The Extended Spandrel: Memetic Host Switching and the Paradox of Argentina's Pro-Worker Labor Regime as Extended Phenotype of Extractive Protectionism | [10.5281/zenodo.19098168](https://doi.org/10.5281/zenodo.19098168) · [PDF](papers/19098168-The-Extended-Spandrel-Memetic-Host-Switching-and-the-Paradox-of-Argentina-s-Pro-Worker.pdf) |
| 2026-03-17 | Punctuated Institutional Equilibria: Stasis as Evolutionarily Stable Strategy, Basin Depth, and the Temporal Dynamics of Constitutional Lock-in | [10.5281/zenodo.19077323](https://doi.org/10.5281/zenodo.19077323) · [PDF](papers/19077323-Punctuated-Institutional-Equilibria-Stasis-as-Evolutionarily-Stable-Strategy-Basin-Dep.pdf) |
| 2026-03-14 | Simulating Institutional Dynamics: A Multi-Agent Framework for Predicting Legal Reform Outcomes Using Extended Phenotype Theory | [10.5281/zenodo.19010941](https://doi.org/10.5281/zenodo.19010941) · [PDF](papers/19010941-Simulating-Institutional-Dynamics-A-Multi-Agent-Framework-for-Predicting-Legal-Reform.pdf) |
| 2026-03-11 | Pre-Deployment Normative Evaluation: An Extended Phenotype Framework for Legislative Quality Assurance | [10.5281/zenodo.18947186](https://doi.org/10.5281/zenodo.18947186) · [PDF](papers/18947186-Pre-Deployment-Normative-Evaluation-An-Extended-Phenotype-Framework-for-Legislative-Qu.pdf) |
| 2026-03-10 | Sycophancy as Extended Phenotype: Heteronomous Bayesian Updating, Intentionality Mismatch, and the Evolutionary Stability of Algorithmic Flattery Empirical Support from Cheng et al. (2025) | [10.5281/zenodo.18943464](https://doi.org/10.5281/zenodo.18943464) · [PDF](papers/18943464-Sycophancy-as-Extended-Phenotype-Heteronomous-Bayesian-Updating-Intentionality-Mismatc.pdf) |
| 2026-03-09 | Agentic Fraud as Extended Phenotype: ScamAgent, Parasitic Spontaneous Order, and the Evolutionary Logic of LLM-Mediated Deception | [10.5281/zenodo.18924282](https://doi.org/10.5281/zenodo.18924282) · [PDF](papers/18924282-Agentic-Fraud-as-Extended-Phenotype-ScamAgent-Parasitic-Spontaneous-Order-and-the-Evol.pdf) |
| 2026-03-08 | No Legal Big Bang: Inherited Normative Capital, Continuous Regeneration, and the Asymmetric Membrane Problem in Evolutionary Legal Infrastructure | [10.5281/zenodo.18911041](https://doi.org/10.5281/zenodo.18911041) · [PDF](papers/18911041-No-Legal-Big-Bang-Inherited-Normative-Capital-Continuous-Regeneration-and-the-Asymmetr.pdf) |
| 2026-03-07 | Transformer Architecture for Evolutionary Legal Systems: Why Self-Attention Matches the Multi-Dimensional Structure of Juridical Reasoning, with Application to CriptoIUS | [10.5281/zenodo.18904134](https://doi.org/10.5281/zenodo.18904134) · [PDF](papers/18904134-Transformer-Architecture-for-Evolutionary-Legal-Systems-Why-Self-Attention-Matches-the.pdf) |
| 2026-03-07 | Intentionality Mismatch in Commercial Liability: A Four-Level Evolutionary Analysis of Tapia Araya v. Starbucks (Argentine Supreme Court, 2026) | [10.5281/zenodo.18903217](https://doi.org/10.5281/zenodo.18903217) · [PDF](papers/18903217-Intentionality-Mismatch-in-Commercial-Liability-A-Four-Level-Evolutionary-Analysis-of.pdf) |
| 2026-03-06 | Ley 27802 as a Prospective Test of the EPT/CLI Framework: Labor Reform, Institutional Lock-in, and Predictive Validity in Argentine Law | [10.5281/zenodo.18895179](https://doi.org/10.5281/zenodo.18895179) · [PDF](papers/18895179-Ley-27802-as-a-Prospective-Test-of-the-EPT-CLI-Framework-Labor-Reform-Institutional-Lo.pdf) |
| 2026-03-05 | Spandrels of Accountability: Scheming Propensity Research as Inadvertent Evidence Against the Algorithmic Corporation | [10.5281/zenodo.18882212](https://doi.org/10.5281/zenodo.18882212) · [PDF](papers/18882212-Spandrels-of-Accountability-Scheming-Propensity-Research-as-Inadvertent-Evidence-Again.pdf) |
| 2026-03-05 | DARWIN'S ONE LONG ARGUMENT AND ESCOHOTADO'S THREE LONG VOLUMES: Historical Inference, Institutional Vestiges, and the Methodological Convergence of Evolutionary Biology and Anti-Commercial Genealogy | [10.5281/zenodo.18880937](https://doi.org/10.5281/zenodo.18880937) · [PDF](papers/18880937-DARWIN-S-ONE-LONG-ARGUMENT-AND-ESCOHOTADO-S-THREE-LONG-VOLUMES-Historical-Inference-In.pdf) |
| 2026-03-05 | Law as a Primary Adaptive Platform: Generalized Darwinism, Extended Phenotype Theory, and the Methodological Foundations of Evolutionary Jurisprudence | [10.5281/zenodo.18870552](https://doi.org/10.5281/zenodo.18870552) · [PDF](papers/18870552-Law-as-a-Primary-Adaptive-Platform-Generalized-Darwinism-Extended-Phenotype-Theory-and.pdf) |
| 2026-03-04 | THE STATIC AGENT ASSUMPTION Dynamic Intentionality Classification and the Limits of the Algorithmic Corporation | [10.5281/zenodo.18857385](https://doi.org/10.5281/zenodo.18857385) · [PDF](papers/18857385-THE-STATIC-AGENT-ASSUMPTION-Dynamic-Intentionality-Classification-and-the-Limits-of-th.pdf) |
| 2026-03-03 | PREDATORY INVITATIONS AS EXTENDED PHENOTYPE: A Parasitic Spontaneous Order Framework for Academic Publishing | [10.5281/zenodo.18853667](https://doi.org/10.5281/zenodo.18853667) · [PDF](papers/18853667-PREDATORY-INVITATIONS-AS-EXTENDED-PHENOTYPE-A-Parasitic-Spontaneous-Order-Framework-fo.pdf) |
| 2026-03-03 | Free-Floating Rationales, Normative Hysteresis, and Constitutional Lock-in: Dennett's Contribution to Extended Phenotype Theory and Multilevel Evolutionary Game Theory in Legal Systems | [10.5281/zenodo.18851650](https://doi.org/10.5281/zenodo.18851650) · [PDF](papers/18851650-Free-Floating-Rationales-Normative-Hysteresis-and-Constitutional-Lock-in-Dennett-s-Con.pdf) |
| 2026-03-02 | Multilevel Selection, Hierarchical Causation, and Constitutional Lock-in: Reconciling Gould with Gene-Centered Memetics | [10.5281/zenodo.18829975](https://doi.org/10.5281/zenodo.18829975) · [PDF](papers/18829975-Multilevel-Selection-Hierarchical-Causation-and-Constitutional-Lock-in-Reconciling-Gou.pdf) |
| 2026-02-26 | WHEN THE RED QUEEN STUMBLES: Temporal Asymmetry and the Collapse of Regulatory Coevolution | [10.5281/zenodo.18790245](https://doi.org/10.5281/zenodo.18790245) · [PDF](papers/18790245-WHEN-THE-RED-QUEEN-STUMBLES-Temporal-Asymmetry-and-the-Collapse-of-Regulatory-Coevolut.pdf) |
| 2026-02-25 | Synthetic Chaos as an Institutional Laboratory: Independent Evidence for Extended Phenotype Theory from Autonomous Agent Red-teaming | [10.5281/zenodo.18777434](https://doi.org/10.5281/zenodo.18777434) · [PDF](papers/18777434-Synthetic-Chaos-as-an-Institutional-Laboratory-Independent-Evidence-for-Extended-Pheno.pdf) |
| 2026-02-25 | REGULATORY HYSTERESIS, EXTENDED PHENOTYPE, AND THE LEX ARTIS OF INSTITUTIONAL DESIGN: How Synthetic Agent Simulations Transform State Liability for Defective Normative Production | [10.5281/zenodo.18774354](https://doi.org/10.5281/zenodo.18774354) · [PDF](papers/18774354-REGULATORY-HYSTERESIS-EXTENDED-PHENOTYPE-AND-THE-LEX-ARTIS-OF-INSTITUTIONAL-DESIGN-How.pdf) |
| 2026-02-25 | Constitutional Chimera, Structural Hyperregulation, and Artificial Intelligence as Stress Test | [10.5281/zenodo.18765188](https://doi.org/10.5281/zenodo.18765188) · [PDF](papers/18765188-Constitutional-Chimera-Structural-Hyperregulation-and-Artificial-Intelligence-as-Stres.pdf) |
| 2026-02-24 | The Non-Justiciability Meme: FIFA's Prerogative State and the Four Century Genealogy of a Legal Concept | [10.5281/zenodo.18758065](https://doi.org/10.5281/zenodo.18758065) · [PDF](papers/18758065-The-Non-Justiciability-Meme-FIFA-s-Prerogative-State-and-the-Four-Century-Genealogy-of.pdf) |
| 2026-02-22 | Regulating the Unintentional AI Governance through Multi-Level Evolutionary Game Theory, Extended Phenotype Theory, and Constitutional Self-Restraint | [10.5281/zenodo.18735857](https://doi.org/10.5281/zenodo.18735857) · [PDF](papers/18735857-Regulating-the-Unintentional-AI-Governance-through-Multi-Level-Evolutionary-Game-Theor.pdf) |
| 2026-02-21 | THE POLITICAL MODEL CANVAS: Mapping Argentina's Competing Institutional Regimes | [10.5281/zenodo.18725959](https://doi.org/10.5281/zenodo.18725959) · [PDF](papers/18725959-THE-POLITICAL-MODEL-CANVAS-Mapping-Argentina-s-Competing-Institutional-Regimes.pdf) |
| 2026-02-17 | FROM ONTOGENY TO INSTITUTIONAL CALCIFICATION - Group Membership Bias as the Cognitive Engine of Asymmetric Legal Persistence | [10.5281/zenodo.18673365](https://doi.org/10.5281/zenodo.18673365) · [PDF](papers/18673365-FROM-ONTOGENY-TO-INSTITUTIONAL-CALCIFICATION-Group-Membership-Bias-as-the-Cognitive-En.pdf) |
| 2026-02-16 | From Free Rider to Free Raider: How Non-Enforcement Cascades Destroy Anonymous Cooperation | [10.5281/zenodo.18665967](https://doi.org/10.5281/zenodo.18665967) · [PDF](papers/18665967-From-Free-Rider-to-Free-Raider-How-Non-Enforcement-Cascades-Destroy-Anonymous-Cooperat.pdf) |
| 2026-02-16 | Road to Connivance: Common Knowledge, Inverted Charity, and the Evolutionary Stability of Clientelistic Populism | [10.5281/zenodo.18654069](https://doi.org/10.5281/zenodo.18654069) · [PDF](papers/18654069-Road-to-Connivance-Common-Knowledge-Inverted-Charity-and-the-Evolutionary-Stability-of.pdf) |
| 2026-02-16 | Extended Phenotype Legal Theory: Equilibrium Refinements and Cultural-Legal Index 3.0 | [10.5281/zenodo.18653958](https://doi.org/10.5281/zenodo.18653958) · [PDF](papers/18653958-Extended-Phenotype-Legal-Theory-Equilibrium-Refinements-and-Cultural-Legal-Index-3-0.pdf) |
| 2026-02-12 | Argentina's Fiscal Lock-in: Tax Reform as Extended Phenotype | [10.5281/zenodo.18626683](https://doi.org/10.5281/zenodo.18626683) · [PDF](papers/18626683-Argentina-s-Fiscal-Lock-in-Tax-Reform-as-Extended-Phenotype.pdf) |
| 2026-02-12 | LAW AS EXTENDED PHENOTYPE: REFRAMING LEGAL THEORY THROUGH EVOLUTIONARY EPISTEMOLOGY | [10.5281/zenodo.18626632](https://doi.org/10.5281/zenodo.18626632) · [PDF](papers/18626632-LAW-AS-EXTENDED-PHENOTYPE-REFRAMING-LEGAL-THEORY-THROUGH-EVOLUTIONARY-EPISTEMOLOGY.pdf) |
| 2026-02-12 | From Transaction Costs to Memetic Fitness: Formalizing Douglass North's Institutional Insights Through Extended Phenotype Theory | [10.5281/zenodo.18626473](https://doi.org/10.5281/zenodo.18626473) · [PDF](papers/18626473-From-Transaction-Costs-to-Memetic-Fitness-Formalizing-Douglass-North-s-Institutional-I.pdf) |
| 2026-02-12 | The WEIRD Veil: Why Rawlsian Justice May Not Generalize Beyond Its Cultural Origins | [10.5281/zenodo.18625895](https://doi.org/10.5281/zenodo.18625895) · [PDF](papers/18625895-The-WEIRD-Veil-Why-Rawlsian-Justice-May-Not-Generalize-Beyond-Its-Cultural-Origins.pdf) |
| 2026-02-11 | The Reciprocity Trap: A Game-Theoretic Analysis of How Cooperative Norms Undermine Institutional Integrity | [10.5281/zenodo.18615279](https://doi.org/10.5281/zenodo.18615279) · [PDF](papers/18615279-The-Reciprocity-Trap-A-Game-Theoretic-Analysis-of-How-Cooperative-Norms-Undermine-Inst.pdf) |
| 2026-02-10 | The Canary in the Mine: Game Theory as Diagnostic Instrument for the Erosion of Human Agency | [10.5281/zenodo.18604030](https://doi.org/10.5281/zenodo.18604030) · [PDF](papers/18604030-The-Canary-in-the-Mine-Game-Theory-as-Diagnostic-Instrument-for-the-Erosion-of-Human-A.pdf) |
| 2026-02-10 | From Hive Minds to Administered Minds: A Formal Theory of Agency Collapse and Emergent Macro-Agency | [10.5281/zenodo.18604015](https://doi.org/10.5281/zenodo.18604015) · [PDF](papers/18604015-From-Hive-Minds-to-Administered-Minds-A-Formal-Theory-of-Agency-Collapse-and-Emergent.pdf) |
| 2026-02-10 | Asymmetric Intentionality in Legal Games: When Players Operate at Different Intentional Levels | [10.5281/zenodo.18603990](https://doi.org/10.5281/zenodo.18603990) · [PDF](papers/18603990-Asymmetric-Intentionality-in-Legal-Games-When-Players-Operate-at-Different-Intentional.pdf) |
| 2026-02-10 | The Dennett-Nash Gap in Corporate Enforcement: Why Corporations Recidivate More Than Individuals | [10.5281/zenodo.18603603](https://doi.org/10.5281/zenodo.18603603) · [PDF](papers/18603603-The-Dennett-Nash-Gap-in-Corporate-Enforcement-Why-Corporations-Recidivate-More-Than-In.pdf) |
| 2026-02-10 | Corporate Criminal Liability and the Impossibility of Mens Rea: Why Guilty Minds Require Moral Agents | [10.5281/zenodo.18603564](https://doi.org/10.5281/zenodo.18603564) · [PDF](papers/18603564-Corporate-Criminal-Liability-and-the-Impossibility-of-Mens-Rea-Why-Guilty-Minds-Requir.pdf) |
| 2026-02-10 | Evolutionarily Stable Non-Compliance: A Game-Theoretic Analysis of Corporate Governance Failures | [10.5281/zenodo.18603260](https://doi.org/10.5281/zenodo.18603260) · [PDF](papers/18603260-Evolutionarily-Stable-Non-Compliance-A-Game-Theoretic-Analysis-of-Corporate-Governance.pdf) |
| 2026-02-10 | Agency Heterogeneous Intentionality: How Corporate Structure Transforms Moral Agents into Optimization Outputs | [10.5281/zenodo.18603217](https://doi.org/10.5281/zenodo.18603217) · [PDF](papers/18603217-Agency-Heterogeneous-Intentionality-How-Corporate-Structure-Transforms-Moral-Agents-in.pdf) |
| 2026-02-10 | The Generalized Intentionality Mismatch Theorem: When Law Assumes Moral Agency That Doesn't Exist | [10.5281/zenodo.18603169](https://doi.org/10.5281/zenodo.18603169) · [PDF](papers/18603169-The-Generalized-Intentionality-Mismatch-Theorem-When-Law-Assumes-Moral-Agency-That-Doe.pdf) |
| 2026-02-10 | The Normative Calculation Problem Under Heterogeneous Intentionality: Why Effective Enforcement Requires Price Mechanisms | [10.5281/zenodo.18603037](https://doi.org/10.5281/zenodo.18603037) · [PDF](papers/18603037-The-Normative-Calculation-Problem-Under-Heterogeneous-Intentionality-Why-Effective-Enf.pdf) |
| 2026-02-10 | Game Theory's Hidden Assumption: Intentionality Homogeneity and the Failure of Corporate Criminal Liability | [10.5281/zenodo.18600364](https://doi.org/10.5281/zenodo.18600364) · [PDF](papers/18600364-Game-Theory-s-Hidden-Assumption-Intentionality-Homogeneity-and-the-Failure-of-Corporat.pdf) |
| 2026-02-10 | Beyond WEIRD Bias: Why Token-Based Legal AI Cannot Model Post-Colonial Compliance Dynamics | [10.5281/zenodo.18576911](https://doi.org/10.5281/zenodo.18576911) · [PDF](papers/18576911-Beyond-WEIRD-Bias-Why-Token-Based-Legal-AI-Cannot-Model-Post-Colonial-Compliance-Dynam.pdf) |
| 2026-02-09 | The Dawkins-Hayek Convergence: Spontaneous Order as Extended Phenotype | [10.5281/zenodo.18576674](https://doi.org/10.5281/zenodo.18576674) · [PDF](papers/18576674-The-Dawkins-Hayek-Convergence-Spontaneous-Order-as-Extended-Phenotype.pdf) |
| 2026-02-09 | Law as Language: From Scandinavian Realism to Evolutionary Jurisprudence | [10.5281/zenodo.18576390](https://doi.org/10.5281/zenodo.18576390) · [PDF](papers/18576390-Law-as-Language-From-Scandinavian-Realism-to-Evolutionary-Jurisprudence.pdf) |
| 2026-02-09 | The Extended Phenotype of Artificial Intelligence: An Evolutionary Analysis of Model Collapse and the Anthropic Settlement as Cognitive Selection Pressure | [10.5281/zenodo.18567734](https://doi.org/10.5281/zenodo.18567734) · [PDF](papers/18567734-The-Extended-Phenotype-of-Artificial-Intelligence-An-Evolutionary-Analysis-of-Model-Co.pdf) |
| 2026-02-09 | Two Paths, One Evolution: Testing the Extended Phenotype Theory Across Legal Systems | [10.5281/zenodo.18567507](https://doi.org/10.5281/zenodo.18567507) · [PDF](papers/18567507-Two-Paths-One-Evolution-Testing-the-Extended-Phenotype-Theory-Across-Legal-Systems.pdf) |
| 2026-02-09 | Law as Extended Phenotype: Toward an Evolutionary Theory of Legal Systems | [10.5281/zenodo.18567125](https://doi.org/10.5281/zenodo.18567125) · [PDF](papers/18567125-Law-as-Extended-Phenotype-Toward-an-Evolutionary-Theory-of-Legal-Systems.pdf) |
| 2026-02-09 | The Legislator as Extended Phenotype: A Darwinian Theory of Legal Evolution | [10.5281/zenodo.18566652](https://doi.org/10.5281/zenodo.18566652) · [PDF](papers/18566652-The-Legislator-as-Extended-Phenotype-A-Darwinian-Theory-of-Legal-Evolution.pdf) |
| 2026-02-09 | Jurists as Evolutionary Engineers: Artificial Selection in Legal Doctrine | [10.5281/zenodo.18564668](https://doi.org/10.5281/zenodo.18564668) · [PDF](papers/18564668-Jurists-as-Evolutionary-Engineers-Artificial-Selection-in-Legal-Doctrine.pdf) |
| 2026-02-09 | The Altruism Paradox in Law: How Selfish Genes Create Cooperative Legal Orders | [10.5281/zenodo.18562865](https://doi.org/10.5281/zenodo.18562865) · [PDF](papers/18562865-The-Altruism-Paradox-in-Law-How-Selfish-Genes-Create-Cooperative-Legal-Orders.pdf) |
| 2026-02-09 | Dead Language, Living Law: Latin Legal Maxims as Perfect Memes | [10.5281/zenodo.18556003](https://doi.org/10.5281/zenodo.18556003) · [PDF](papers/18556003-Dead-Language-Living-Law-Latin-Legal-Maxims-as-Perfect-Memes.pdf) |

---

## Papers — SSRN Archive (62 papers, PDF hosted here)

> The SSRN account was suspended in January 2026 for administrative reasons (category mismatch for interdisciplinary papers), unrelated to content. All PDFs are hosted in the [`papers/`](papers/) folder of this repository. Zenodo links identify the durable Zenodo record when available.

| SSRN ID | Title | PDF | Zenodo |
|---------|-------|-----|--------|
| [5387400](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5387400) | The Legislator as Extended Phenotype: A Darwinian Theory of Legal Evolution | [PDF](papers/5387400-The-Legislator-as-Extended-Phenotype-A-Darwinian-T.pdf) | [10.5281/zenodo.18566652](https://doi.org/10.5281/zenodo.18566652) |
| [5391036](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5391036) | Two Paths, One Evolution: Testing the Extended Phenotype Theory Across Legal Systems | [PDF](papers/5391036-Two-Paths-One-Evolution-Testing-the.pdf) | [10.5281/zenodo.18567507](https://doi.org/10.5281/zenodo.18567507) |
| [5402461](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5402461) | Law as Language: From Scandinavian Realism to Evolutionary Jurisprudence | [PDF](papers/5402461-Law-as-Language-From-Scandinavian.pdf) | [10.5281/zenodo.18576390](https://doi.org/10.5281/zenodo.18576390) |
| [5405459](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5405459) | JurisRank: Measuring Legal Phenotypic Fitness Through Citation Networks | [PDF](papers/5405459-JurisRank-Measuring-Legal-Phenotypic-Fitness-Throu.pdf) | [10.5281/zenodo.20613103](https://doi.org/10.5281/zenodo.20613103) |
| [5428374](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5428374) | Evolutionary Genealogy of Corporate Criminal Liability | [PDF](papers/5428374-Evolutionary-Genealogy-of-Corporate-Criminal-Liabi.pdf) | [10.5281/zenodo.20612819](https://doi.org/10.5281/zenodo.20612819) |
| [5454256](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5454256) | The Extended Phenotype of Artificial Intelligence | [PDF](papers/5454256-The-Extended-Phenotype-of-Artificial-Intelligence.pdf) | [10.5281/zenodo.18567734](https://doi.org/10.5281/zenodo.18567734) |
| [5463814](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5463814) | The Extended Phenotype of Populism | [PDF](papers/5463814-THE-EXTENDED-PHENOTYPE-OF-POPULISM.pdf) | [10.5281/zenodo.20612821](https://doi.org/10.5281/zenodo.20612821) |
| [5467928](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5467928) | The Peralta Metamorphosis: Quantifying the Evolution of Legal Parasitism | [PDF](papers/5467928-The-Peralta-Metamorphosis-Quantifying-the-Evolutio.pdf) | [10.5281/zenodo.20612829](https://doi.org/10.5281/zenodo.20612829) |
| [5468569](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5468569) | The Multilayer Parasite: Quantifying Corruption's Institutional Architecture | [PDF](papers/5468569-The-Multilayer-Parasite-Quantifying-Corruptions.pdf) | [10.5281/zenodo.20612833](https://doi.org/10.5281/zenodo.20612833) |
| [5472748](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5472748) | The Cuckoo's Superestimulus: A Theoretical Framework | [PDF](papers/5472748-The-Cuckoos-Superestimulus-A-Theoretical-Framework.pdf) | [10.5281/zenodo.20612835](https://doi.org/10.5281/zenodo.20612835) |
| [5477267](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5477267) | Computational Genealogies and Political Attractors | [PDF](papers/5477267-Computational-Genealogies-and-Political-Attractors.pdf) | [10.5281/zenodo.20612837](https://doi.org/10.5281/zenodo.20612837) |
| [5478426](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5478426) | Why Bad Law Persists: Evolutionarily Stable Strategies in Legal Systems | [PDF](papers/5478426-Why-Bad-Law-Persists-Evolutionary-Stable-Strategie.pdf) | [10.5281/zenodo.20612840](https://doi.org/10.5281/zenodo.20612840) |
| [5478466](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5478466) | The Altruism Paradox in Law: How Selfish Genes Create Cooperative Legal Orders | [PDF](papers/5478466-The-Altruism-Paradox-in-Law-How-Selfish-Genes-Crea.pdf) | [10.5281/zenodo.18562865](https://doi.org/10.5281/zenodo.18562865) |
| [5478467](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5478467) | The Legal DNA: How Behavioral and Evolutionary Forces Shape Legal Norms | [PDF](papers/5478467-The-Legal-DNA-How-Behavioral-and.pdf) | [10.5281/zenodo.20612842](https://doi.org/10.5281/zenodo.20612842) |
| [5486006](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5486006) | Dead Language, Living Law: Latin Legal Maxims as Perfect Memes | [PDF](papers/5486006-Dead-Language-Living-Law-Latin-Legal-Maxims-as.pdf) | [10.5281/zenodo.18556003](https://doi.org/10.5281/zenodo.18556003) |
| [5486466](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5486466) | Good Faith as Legal DNA: The Genealogical Origins of Contractual Loyalty | [PDF](papers/5486466-GOOD-FAITH-AS-LEGAL-DNA-THE-GENEALOGICAL.pdf) | [10.5281/zenodo.20612844](https://doi.org/10.5281/zenodo.20612844) |
| [5492066](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5492066) | Jurists as Evolutionary Engineers: Artificial Selection in Legal Doctrine | [PDF](papers/5492066-JURISTS-AS-EVOLUTIONARY-ENGINEERS-ARTIFICIAL.pdf) | [10.5281/zenodo.18564668](https://doi.org/10.5281/zenodo.18564668) |
| [5496678](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5496678) | The Legal Book of the Dead: Memetic Pincers and Institutional Palimpsests | [PDF](papers/5496678-The-Legal-Book-of-the-Dead-Memetic-Pincers.pdf) | [10.5281/zenodo.20612848](https://doi.org/10.5281/zenodo.20612848) |
| [5555478](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5555478) | Small Concept Models: A Specialized Framework for Legal AI | [PDF](papers/5555478-Small-Concept-Models-A-Specialized-Framework-for.pdf) | [10.5281/zenodo.20612850](https://doi.org/10.5281/zenodo.20612850) |
| [5557838](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5557838) | IusSpace: A Twelve-Dimensional Framework for Mapping Legal Concepts | [PDF](papers/5557838-IusSpace-A-Twelve-Dimensional-Framework-for-Mappin.pdf) | [10.5281/zenodo.20612852](https://doi.org/10.5281/zenodo.20612852) |
| [5576850](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5576850) | Beyond WEIRD Legal AI: Why Concept-Based Models Outperform Token-Based Approaches | [PDF](papers/5576850-Beyond-WEIRD-Legal-AI-Why-Concept-Based-Models.pdf) | [10.5281/zenodo.20612854](https://doi.org/10.5281/zenodo.20612854) |
| [5584450](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5584450) | Beyond WEIRD Bias: Why Token-Based Legal AI Cannot Model Post-Colonial Compliance | [PDF](papers/5584450-Beyond-WEIRD-Bias-Why-Token-Based-Legal-AI.pdf) | [10.5281/zenodo.18576911](https://doi.org/10.5281/zenodo.18576911) |
| [5591832](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5591832) | Normative Ambiguity as Memetic Niche Space | [PDF](papers/5591832-Normative-Ambiguity-as-Memetic-Niche-Space-An.pdf) | [10.5281/zenodo.20612858](https://doi.org/10.5281/zenodo.20612858) |
| [5593470](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5593470) | Law as Extended Phenotype: Toward an Evolutionary Theory of Legal Systems | [PDF](papers/5593470-Law-as-Extended-Phenotype-Toward-an.pdf) | [10.5281/zenodo.18567125](https://doi.org/10.5281/zenodo.18567125) |
| [5599553](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5599553) | The Extinction of the Nineteenth Amendment: A Memetic Analysis | [PDF](papers/5599553-THE-EXTINCTION-OF-THE-NINETEENTH-AMENDMENT.pdf) | [10.5281/zenodo.20612860](https://doi.org/10.5281/zenodo.20612860) |
| [5600750](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5600750) | Beyond Iusmorphs: Advanced Evolutionary Models for Legal Compatibility | [PDF](papers/5600750-Beyond-Iusmorphs-Advanced-Evolutionary-Models.pdf) | [10.5281/zenodo.20612864](https://doi.org/10.5281/zenodo.20612864) |
| [5605730](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5605730) | Beyond Iusmorphs: Environmental Compatibility and Institutional Selection | [PDF](papers/5605730-Beyond-Iusmorphs-Environmental-Compatibility.pdf) | [10.5281/zenodo.20612872](https://doi.org/10.5281/zenodo.20612872) |
| [5612010](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5612010) | International Law as Extended Phenotype: Globalist and Sovereignist Memeplexes | [PDF](papers/5612010-International-Law-as-Extended-Phenotype-Globalist.pdf) | [10.5281/zenodo.20612876](https://doi.org/10.5281/zenodo.20612876) |
| [5624710](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5624710) | Constitutional Lock-in and the Phenotypic Expression of Legal Resistance | [PDF](papers/5624710-Constitutional-Lock-in-and-the-Phenotypic.pdf) | [10.5281/zenodo.20612883](https://doi.org/10.5281/zenodo.20612883) |
| [5635152](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5635152) | Argentina's Fiscal Lock-in: Tax Reform as Extended Phenotype | [PDF](papers/5635152-Argentinas-Fiscal-Lock-in-Tax-Reform-as.pdf) | [10.5281/zenodo.18626683](https://doi.org/10.5281/zenodo.18626683) |
| [5645070](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5645070) | Climbing Mount Improbable: A Viable Path for Argentine Institutional Reform | [PDF](papers/5645070-CLIMBING-MOUNT-IMPROBABLE-A-VIABLE-PATH.pdf) | [10.5281/zenodo.20612887](https://doi.org/10.5281/zenodo.20612887) |
| [5660770](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5660770) | Constitutional Paleontology: Tracing the Evolutionary History of Legal Doctrines | [PDF](papers/5660770-CONSTITUTIONAL-PALEONTOLOGY-TRACING.pdf) | [10.5281/zenodo.20612890](https://doi.org/10.5281/zenodo.20612890) |
| [5695662](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5695662) | Before the Command Was Spoken: Law as Pre-Intentional Coordination | [PDF](papers/5695662-Before-the-Command-Was-Spoken-Law-as.pdf) | [10.5281/zenodo.20612892](https://doi.org/10.5281/zenodo.20612892) |
| [5696484](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5696484) | The Grundnorm as Evolutionary Attractor | [PDF](papers/5696484-The-Grundnorm-as-Evolutionary.pdf) | [10.5281/zenodo.20612900](https://doi.org/10.5281/zenodo.20612900) |
| [5718922](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5718922) | Cognitive Mechanisms of Constitutional Entrenchment | [PDF](papers/5718922-COGNITIVE-MECHANISMS-OF-CONSTITUTIONAL.pdf) | [10.5281/zenodo.20612904](https://doi.org/10.5281/zenodo.20612904) |
| [5728083](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5728083) | The Golden Ratio Paradox: Why Optimal Institutional Design May Be Evolutionarily Unstable | [PDF](papers/5728083-The-Golden-Ratio-Paradox-Why-Optimal-Institutional.pdf) | [10.5281/zenodo.20612906](https://doi.org/10.5281/zenodo.20612906) |
| [5731627](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5731627) | From Utopianism to Fossilization: The Evolutionary Pathology of Ideal Constitutions | [PDF](papers/5731627-FROM-UTOPIANISM-TO-FOSSILIZATION-A.pdf) | [10.5281/zenodo.20612910](https://doi.org/10.5281/zenodo.20612910) |
| [5737383](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5737383) | Law as Extended Phenotype: Reframing Legal Theory Through Evolutionary Epistemology | [PDF](papers/5737383-LAW-AS-EXTENDED-PHENOTYPE-REFRAMING.pdf) | [10.5281/zenodo.18626632](https://doi.org/10.5281/zenodo.18626632) |
| [5741544](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5741544) | If Machiavelli Had Known Darwin: Evolutionary Power and Institutional Design | [PDF](papers/5741544-IF-MACHIAVELLI-HAD-KNOWN-DARWIN-EVOLUTIONARY.pdf) | [10.5281/zenodo.20612914](https://doi.org/10.5281/zenodo.20612914) |
| [5748142](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5748142) | Uruguay and the Fossilization Meme: Testing EPT Against a Positive Case | [PDF](papers/5748142-Uruguay-and-the-Fossilization-Meme-Testing.pdf) | [10.5281/zenodo.20612916](https://doi.org/10.5281/zenodo.20612916) |
| [5750242](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5750242) | From Transaction Costs to Memetic Fitness: Formalizing North's Institutional Insights | [PDF](papers/5750242-FROM-TRANSACTION-COSTS-TO-MEMETIC-FITNESS.pdf) | [10.5281/zenodo.18626473](https://doi.org/10.5281/zenodo.18626473) |
| [5760142](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5760142) | Beyond Stated Preferences: Tacit Consensus as Cultural Lock-in | [PDF](papers/5760142-Beyond-Stated-Preferences-Tacit-Consensus-as-Cultu.pdf) | [10.5281/zenodo.20612923](https://doi.org/10.5281/zenodo.20612923) |
| [5768423](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5768423) | Epistemological Clergies: When Orthodoxy Becomes Institutional Selection Pressure | [PDF](papers/5768423-EPISTEMOLOGICAL-CLERGIES-WHEN-ORTHODOXY.pdf) | [10.5281/zenodo.20612925](https://doi.org/10.5281/zenodo.20612925) |
| [5776925](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5776925) | "General Welfare" and "Common Good" as Evolutionary Attractors in Constitutional Law | [PDF](papers/5776925-General-Welfare-and-Common-Good-as-Evolutionary.pdf) | [10.5281/zenodo.20612927](https://doi.org/10.5281/zenodo.20612927) |
| [5881663](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5881663) | The Dawkins-Hayek Convergence: Spontaneous Order as Extended Phenotype | [PDF](papers/5881663-The-Dawkins-Hayek-Convergence-Spontaneous.pdf) | [10.5281/zenodo.18576674](https://doi.org/10.5281/zenodo.18576674) |
| [5881702](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5881702) | Against Multilevel Selection in Legal Evolution: A Defense and Restatement | [PDF](papers/5881702-Against-Multilevel-Selection-in-Legal-Evolution.pdf) | [10.5281/zenodo.20612935](https://doi.org/10.5281/zenodo.20612935) |
| [5882342](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5882342) | Archaeological Scaffolding of Law: Institutional Layers and Memetic Stratigraphy | [PDF](papers/5882342-ARCHAEOLOGICAL-SCAFFOLDING-OF-LAW.pdf) | [10.5281/zenodo.20612939](https://doi.org/10.5281/zenodo.20612939) |
| [5886142](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5886142) | Blind Breeders: The Extended Phenotype of Unintentional Institutional Design | [PDF](papers/5886142-BLIND-BREEDERS-The-Extended-Phenotype-of.pdf) | [10.5281/zenodo.20612948](https://doi.org/10.5281/zenodo.20612948) |
| [5891884](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5891884) | Law as Extended Phenotype: A Game-Theoretic Synthesis | [PDF](papers/5891884-Law-as-Extended-Phenotype-A-Game-Theoretic.pdf) | [10.5281/zenodo.20612950](https://doi.org/10.5281/zenodo.20612950) |
| [5908462](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5908462) | The Praxeological Foundations of Extended Phenotype Theory | [PDF](papers/5908462-The-Praxeological-Foundations-of-Extended.pdf) | [10.5281/zenodo.20612952](https://doi.org/10.5281/zenodo.20612952) |
| [5908662](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5908662) | Legal Prices: The Normative Calculation Problem and the Limits of Command-and-Control | [PDF](papers/5908662-Legal-Prices-The-Normative-Calculation-Problem-and.pdf) | [10.5281/zenodo.20612954](https://doi.org/10.5281/zenodo.20612954) |
| [5955735](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5955735) | The WEIRD Machine: Why Western Legal AI Fails in Non-WEIRD Jurisdictions | [PDF](papers/5955735-THE-WEIRD-MACHINE-WHY-WESTERN.pdf) | [10.5281/zenodo.20612958](https://doi.org/10.5281/zenodo.20612958) |
| [5960677](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5960677) | Game Theory's Hidden Assumption: Intentionality Homogeneity and Corporate Liability | [PDF](papers/5960677-GAME-THEORYS-HIDDEN-ASSUMPTION-Intentionality.pdf) | [10.5281/zenodo.18600364](https://doi.org/10.5281/zenodo.18600364) |
| [5971914](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5971914) | Mises's Fatal Flaw: Binding Deficits and the Memetic Evolution of Fiscal Constitutions | [PDF](papers/5971914-Misess-Fatal-Flaw-Binding-Deficits-and-the-Memetic.pdf) | [10.5281/zenodo.20612960](https://doi.org/10.5281/zenodo.20612960) |
| [5974555](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5974555) | Formal Foundations of Multilevel Game Theory: Price Equation and Replicator Dynamics | [PDF](papers/5974555-Formal-Foundations-of-Multilevel-Game-Theory.pdf) | [10.5281/zenodo.20612964](https://doi.org/10.5281/zenodo.20612964) |
| [5991115](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5991115) | Extending Aumann's Agreement Theorem to Heterogeneous Intentionality | [PDF](papers/5991115-Extending-Aumanns-Agreement-Theorem-to.pdf) | [10.5281/zenodo.20612968](https://doi.org/10.5281/zenodo.20612968) |
| [5991195](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5991195) | The Generalized Intentionality Mismatch Theorem: When Law Assumes Moral Agency That Doesn't Exist | [PDF](papers/5991195-The-Generalized-Intentionality-Mismatch-Theorem.pdf) | [10.5281/zenodo.18603169](https://doi.org/10.5281/zenodo.18603169) |
| [5991355](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5991355) | Environmental Law and the Myth of Corporate Citizenship | [PDF](papers/5991355-Environmental-Law-and-the-Myth-of-Corporate.pdf) | [10.5281/zenodo.20612972](https://doi.org/10.5281/zenodo.20612972) |
| [5995234](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5995234) | The Normative Calculation Problem Under Heterogeneous Intentionality | [PDF](papers/5995234-The-Normative-Calculation-Problem-Under.pdf) | [10.5281/zenodo.18603037](https://doi.org/10.5281/zenodo.18603037) |
| [5995435](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5995435) | Agency Problems Under Heterogeneous Intentionality | [PDF](papers/5995435-Agency-Problems-Under-Heterogeneous.pdf) | [10.5281/zenodo.20612974](https://doi.org/10.5281/zenodo.20612974) |
| [6000675](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6000675) | Evolutionarily Stable Non-Compliance: A Game-Theoretic Analysis | [PDF](papers/6000675-Evolutionarily-Stable-Non-Compliance-A-Game.pdf) | [10.5281/zenodo.18603260](https://doi.org/10.5281/zenodo.18603260) |
| [6001434](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6001434) | The Fatal Conceit of Consensus Networks: Why Decentralized Governance Fails | [PDF](papers/6001434-The-Fatal-Conceit-of-Consensus-Networks-Why.pdf) | [10.5281/zenodo.20612976](https://doi.org/10.5281/zenodo.20612976) |

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
