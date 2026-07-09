---
title: "Towards Automating Scientific Review with Google's Paper Assistant Tool"
authors: "Jayaram, R.; Tyler, D.; Woodruff, D.; Cortes, C.; Matias, Y.; Mirrokni, V.; Cohen-Addad, V."
year: 2026
source: arXiv
doi_url: "https://arxiv.org/abs/2606.28277"
date_analyzed: 2026-07-09
tags: [AI-agents, LLM, peer-review, scientific-review, inference-scaling, paper-writing, EPT, methodology]
relevance: alta
type: tecnico
---

## Tesis central

El paper sostiene que la generación científica asistida por IA crea un cuello de botella de validación: la revisión humana tradicional no puede escalar al ritmo de producción. Propone PAT, un sistema agentic de revisión científica que segmenta manuscritos, asigna presupuesto de inferencia según complejidad y sintetiza revisiones profundas con grounding. La intervención más defendible hoy es usar IA como herramienta del autor antes de la presentación, manteniendo responsabilidad humana.

## Novedad real

La novedad no es "usar un LLM para revisar", sino la arquitectura de inferencia escalada: segmentación semántica, presupuesto adaptativo, revisores profundos coordinados por segmento y síntesis global con deduplicación/grounding. El paper aporta además una taxonomía útil de roles de IA en revisión: herramienta para autores, herramienta para revisores, revisor de apoyo y automatización total.

## Técnica implementable

**¿Qué implementar?** PAT-style pre-submission review workflow para papers EPT/EGT.  
**Destino:** Codex/Claude/Perplexity skills y flujo de revisión antes de Zenodo, Substack, journal o libro.  
**Complejidad:** media.  

**Pasos:**
1. Ingestar PDF/DOCX/Markdown y extraer texto localmente.
2. Segmentar el manuscrito por función: tesis, marco teórico, métodos/instrumentos, evidencia, referencias, claims normativos, contribución EPT/EGT.
3. Asignar presupuesto adaptativo: más revisión a fórmulas, validación empírica, claims de originalidad, citas y puntos señalados por Fable.
4. Ejecutar revisiones profundas por segmento: coherencia lógica, soporte empírico, overclaiming, bibliografía, definiciones, falsabilidad, terminología y DOI/Zenodo.
5. Usar Perplexity como grounding externo para citas, novedad, literatura reciente y verificación de referencias.
6. Usar Claude como revisor profundo de arquitectura argumental y consistencia conceptual.
7. Sintetizar hallazgos con severidad: blocking, should fix, consider, style.
8. Exigir decisión humana final: aceptar, corregir, rechazar o dejar como limitación declarada.

## Conexión con el programa EPT/EGT

El paper sirve como infraestructura metodológica para mejorar la calidad del corpus EPT/EGT. Encaja especialmente con la regla Fable 2026-2028: evitar proliferación de instrumentos sin validación, separar teoría de evidencia, resolver ambigüedades CLI/TCI y fortalecer citas Zenodo. También ofrece un caso externo relevante para el frente de IA como constructor de nicho: si herramientas de revisión se vuelven parte del pipeline científico, modifican las presiones selectivas sobre qué papers sobreviven.

## Ideas para papers propios

- AI review tools as niche constructors of scientific and legal memepools.
- Peer review automation as extended phenotype of scientific institutions.
- PAT-style review as a response to documentary inertia and corpus contamination.
- Role taxonomy adapted to legal scholarship: AI as author tool, reviewer aid, supporting doctrinal auditor, or automated publication gate.
- Legal equivalent of AIrXiv: a lower-stakes repository tier for AI-audited legal preprints.

## Limitaciones del paper

El sistema PAT es propietario y depende de Gemini Deep Think; la arquitectura es replicable como patrón, no como implementación exacta. La evaluación reportada se concentra en matemática, teoría de la computación y machine learning, por lo que no prueba traslado directo a derecho, filosofía jurídica o teoría institucional. El paper reconoce riesgos de alucinación, parsing de PDFs, deskilling, sesgo centralizado, gaming adversarial y desigualdad de acceso a compute.

## Next actions

- [x] Crear skill local PAT-style para revisión profunda de manuscritos EPT/EGT.
- [x] Crear prompts operativos para Claude y Perplexity.
- [ ] Aplicar el flujo al próximo paper antes de subirlo a Zenodo.
- [ ] Usar la taxonomía de roles en un futuro paper sobre revisión académica y nicho memético.
- [ ] Considerar un módulo de "pre-Zenodo review" que emita blocking/should-fix/consider antes de publicar.
