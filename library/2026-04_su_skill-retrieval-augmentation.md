---
title: "Skill Retrieval Augmentation for Agentic AI"
authors: "Su, W.; Long, J.; Ai, Q.; Tang, Y.; Wang, C.; Tu, Y.; Liu, Y."
year: 2026
source: arXiv
doi_url: "https://arxiv.org/abs/2604.24594"
date_analyzed: 2026-04-29
tags: [AI-agents, AI-skills, LLM]
relevance: alta
type: tecnico
---

## Tesis central

Los sistemas actuales de agentes LLM equipan al modelo con skills enumerando todas las disponibles en el contexto (el paradigma SKILL.md/in-context injection). Este enfoque no escala: a medida que el corpus de skills crece, el presupuesto de contexto se agota y la precisión del modelo para identificar la skill correcta cae abruptamente. El paper formula **Skill Retrieval Augmentation (SRA)**: en lugar de exponer todas las skills en contexto, el agente las recupera dinámicamente desde un corpus externo grande, bajo demanda. El pipeline tiene tres etapas acopladas: recuperación, incorporación y aplicación de skills.

## Novedad real

Dos contribuciones genuinamente nuevas:

1. **SRA-Bench**: primer benchmark que evalúa de forma *descompuesta* el pipeline completo (5.400 instancias, 636 gold skills, corpus de 26.262 skills con distractores realistas). Permite diagnosticar dónde falla el sistema — no solo si falla.

2. **Hallazgo empírico sobre incorporación**: el cuello de botella no es la recuperación sino la *incorporación*. Los modelos cargan skills a tasas casi idénticas independientemente de (a) si la gold skill está entre los resultados recuperados, y (b) si el modelo podría resolver la tarea sin skill externa. Este es el "need-awareness gap" y el "relevance-awareness gap" — ningún modelo actual los resuelve bien, ni siquiera los frontier.

## Técnica implementable

**¿Qué implementar?** Recuperación semántica de skills en lugar de enumeración en contexto  
**Destino:** Claude Code skill system (el sistema de skills del usuario ya sufre el problema exacto que describe el paper — 150+ skills enumeradas en system-reminder)  
**Complejidad:** media  

**Pasos:**
1. Generar embeddings de todos los SKILL.md existentes (descripción + primeras 200 palabras del contenido)
2. Almacenar en un vector store local (ChromaDB o similar, sin infraestructura externa)
3. Al recibir una query del usuario, recuperar top-5 skills por similitud semántica
4. Inyectar solo esas 5 en el contexto en lugar de las 150+
5. Agregar un paso explícito de "need-awareness": el modelo evalúa si realmente necesita una skill externa antes de cargarla

**Prerequisitos:** Python, sentence-transformers o embeddings API, ChromaDB

## Citas clave

> "as of April 26, 2026, platforms such as SkillsMP host more than one million distinct skills, and agents are expected to maintain large and lifelong skill libraries that continue to grow. Under this setting, the conventional practice of exposing all candidate skills in context begins to collapse under two compounding bottlenecks: the hard architectural limits of context windows, and the sharp degradation in reasoning and selection accuracy when the model is confronted with a massive volume of skills." (p. 2)

> "skill loading is not functioning as a targeted compensatory mechanism for missing capability, but is instead triggered in a largely indiscriminate manner." (p. 15)

> "In practical systems, these components may correspond to artifacts such as a skill title, a one-line summary, SKILL.md, scripts, and static assets." (p. 4) *(el paper nombra explícitamente el formato SKILL.md que usa el usuario)*

> "scalable skill augmentation is fundamentally a problem of controlled, selective, and need-aware skill utilization, rather than retrieval alone." (p. 16)

## Limitaciones del paper

- El benchmark (SRA-Bench) cubre dominios técnicos (matemáticas, código, lógica, medicina) — no legal ni investigación teórica. Los hallazgos sobre need-awareness son válidos pero no probados en dominios jurídicos.
- El análisis de "relevance-awareness" y "need-awareness" es descriptivo: identifica el problema pero no propone una solución concreta para resolverlo. La agenda de investigación (sección 7) son direcciones, no implementaciones.
- Los modelos evaluados son open-source + GPT-5.4/GLM-5.1. No hay datos sobre Claude. La generalización es razonable pero no verificada.
- "Parametric Skill Augmentation" (sección 7) es especulativa — no hay implementación.

## Next actions

- [ ] **Implementar recuperación semántica de skills**: construir un indexador de SKILL.md con embeddings y reemplazar la enumeración masiva en system-reminder. Complejidad media, alto impacto inmediato.
- [ ] **Agregar need-awareness check al skill de /paper-intake**: antes de cargar Notion MCP o git tools, el skill evalúa explícitamente si los necesita para la tarea actual.
- [ ] **Citar en paper sobre SCM o AI-skills**: el paper provee evidencia empírica directa de por qué los modelos generalistas fallan en skill selection — útil para argumentar la necesidad de Small Concept Models especializados.
- [ ] **Seguir a Qingyao Ai (Tsinghua)**: autor correspondiente, trabaja en IR + agentic AI. Potencial para cross-citations.
- [ ] **Revisar SRA-Bench**: el corpus de 26.262 skills y las anotaciones gold son open source (HuggingFace WeihangSu/SRA-Bench). Puede ser útil para validar el sistema de skills del usuario contra benchmarks externos.
