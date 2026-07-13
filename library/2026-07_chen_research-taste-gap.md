---
title: "Measuring the Gap Between Human and LLM Research Ideas"
authors: "Chen, Z.; Zhao, Y.; Cohan, A."
year: 2026
source: arXiv
doi_url: "https://arxiv.org/abs/2607.01233"
date_analyzed: 2026-07-13
tags: [AI-agents, AI-skills, LLM, research-ideation, creativity, paper-writing, EPT, methodology]
relevance: alta
type: tecnico
---

## Tesis central

El paper sostiene que la evaluación usual de ideas generadas por LLMs mira demasiado el mérito individual de cada propuesta, pero no el patrón agregado de "gusto de investigación" que el modelo tiende a producir. Su hallazgo central es que, ante contextos de literatura comparables, los LLMs producen ideas razonables pero distribucionalmente más estrechas que las humanas: sobrerrepresentan oportunidades de puente y métodos de síntesis/unificación.

## Novedad real

La contribución útil no es otro ranking de novedad o factibilidad, sino una taxonomía bidimensional para auditar el tipo de movimiento intelectual que genera una idea:

- **Opportunity Pattern:** puzzle/contradiction, explanation gap, scope mismatch, evidence gap, bridge opportunity, failure/risk gap, resource bottleneck.
- **Method Paradigm:** synthesis/unification, relax/extend scope, robustification, formal derivation, empirical mapping, artifact/system, optimization/search.

El paper cuantifica que los humanos se distribuyen de modo más amplio, mientras que los modelos se concentran en el par puente/síntesis. Ese sesgo es relevante para cualquier programa que use IA para idear papers, porque el resultado puede sonar sofisticado y aun así reducir la variedad real de preguntas y métodos.

## Técnica implementable

**¿Qué implementar?** Un gate de diversidad creativa para ideas y papers EPT/EGT.  
**Destino:** skill `research-taste-diversifier`, revisión pre-Zenodo, prompts de Claude/Perplexity.  
**Complejidad:** baja-media.  

**Pasos:**
1. Extraer cada idea en dos campos: motivación y método.
2. Clasificar la motivación por oportunidad y el método por paradigma.
3. Marcar como riesgo el par `Bridge Opportunity` + `Synthesis / Unification`, salvo que el paper justifique un mecanismo, medición, predicción falsable, artefacto o formalización nueva.
4. Generar al menos tres variantes no predeterminadas antes de aceptar la arquitectura del paper.
5. Integrar la variante elegida al flujo `paper-assistant-review` para revisión de evidencia, citas, validación y overclaiming.

## Conexión con el programa EPT/EGT

El paper encaja con dos necesidades del programa:

1. **Mejor evaluación de papers antes de subirlos:** no basta con detectar errores de citas, DOI o validación; también hay que detectar si el paper es otro puente conceptual sin nueva presión empírica, formal o institucional.
2. **Mejor generación creativa:** el programa EPT/EGT ya tiene muchos trabajos de síntesis. La próxima mejora de calidad vendrá de mover más ideas hacia contradicciones, explicación causal, evidencia, formalización, artefactos, validación y límites de alcance.

Aplicado al corpus propio, el paper sugiere revisar si ciertas piezas son demasiado "bridge papers" y, cuando lo sean, agregar una operación más fuerte: medición, modelo formal, caso negativo, benchmark, dataset, instrumento operativo o predicción falsable.

## Ideas para papers propios

- AI as a research-taste niche constructor: cómo los LLMs modifican las presiones selectivas del acervo memético científico y jurídico.
- The bridge/synthesis trap in legal-AI scholarship: por qué unir marcos no siempre crea una contribución robusta.
- Research taste as institutional phenotype: los patrones de oportunidad y método como señales de selección dentro de comunidades académicas.
- EPT/EGT corpus audit: mapa de los papers propios por oportunidad y método para detectar saturación de síntesis y déficit de validación.
- Legal theory beyond synthesis: cómo convertir puentes conceptuales en formalización, evidencia, artefactos o predicciones falsables.

## Limitaciones del paper

La taxonomía no debe tratarse como métrica universal de creatividad. El estudio trabaja con papers de ML y Nature Communications, usa reconstrucción asistida por LLMs de trabajos previos y anotación también mediada por modelos. Sirve como heurística fuerte para diseño de workflow, no como prueba de que todo paper humano sea más creativo ni de que todo puente/síntesis sea malo.

## Next actions

- [x] Crear skill `research-taste-diversifier` para Codex y Claude.
- [x] Integrar el gate de diversidad en `paper-assistant-review`.
- [x] Crear prompt pack para Claude/Perplexity.
- [ ] Aplicar la taxonomía al corpus Zenodo/README para detectar saturación temática y metodológica.
- [ ] Usar el gate antes de redactar cada nuevo paper y antes de subirlo a Zenodo.
