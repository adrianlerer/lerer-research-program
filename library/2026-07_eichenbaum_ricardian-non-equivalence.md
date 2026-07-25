---
title: "Ricardian Non-Equivalence"
authors: "Eichenbaum, M. S.; Guerreiro, J.; Obradovic, J."
year: 2026
source: NBER
doi_url: "https://doi.org/10.3386/w34691"
date_analyzed: 2026-07-25
tags: [EGT, multilevel, intentionality, IMT, HANK, fiscal-policy, bounded-rationality]
relevance: alta
type: teoria
---

## Tesis central

El paper sostiene que los hogares no incorporan plenamente las obligaciones tributarias futuras derivadas de transferencias fiscales al decidir su gasto presente. En una encuesta experimental con 6.000 participantes estadounidenses, la propensión planificada a gastar una transferencia universal prácticamente coincide con la propensión marginal a consumir una transferencia individual, mientras las expectativas impositivas apenas se modifican.

Los autores incorporan atención parcial a un modelo HANK. La inatención a impuestos futuros amplifica el gasto, mientras la inatención a efectos de equilibrio general lo amortigua. En sus calibraciones domina el primer efecto, elevando los multiplicadores de transferencias y gasto público respecto del modelo con información completa y expectativas racionales.

## Novedad real

La contribución más fuerte no es demostrar que la equivalencia ricardiana puede fallar, resultado ya conocido, sino identificar experimentalmente un mecanismo concreto y disciplinar con esos momentos un HANK de agentes heterogéneos. El diseño separa una transferencia individual sin consecuencias fiscales agregadas de una transferencia universal financiada mediante déficit.

El apéndice agrega un tercer tratamiento especialmente valioso: cuando se informa expresamente que cada hogar pagará USD 1.400 adicionales en impuestos al año siguiente, aumentan las expectativas tributarias y la propensión a gastar cae de 0,314 a 0,272, pero la equivalencia ricardiana sigue sin restablecerse.

## Conexion con framework EPT/EGT

### Generalized Intentionality Mismatch Theorem

La conexión directa es con GIMT/IMT. La política fiscal es diseñada y modelada desde una representación intertemporal de la restricción presupuestaria estatal, mientras los hogares actúan con una representación parcial de impuestos futuros y efectos sistémicos. La intención de política, la cognición del destinatario y el resultado agregado se ubican en niveles distintos.

El paper permite descomponer el mismatch en dos canales de signo opuesto:

1. La inatención a impuestos futuros amplifica el consumo presente.
2. La inatención a ingresos y tasas de equilibrio general amortigua la respuesta.

Esto matiza una formulación simple de IMT: la heterogeneidad de modelos mentales no produce una distorsión unidireccional. El signo agregado depende de qué desajuste domina y de parámetros como la MPC.

### EGT y juego multinivel

El trabajo aporta una arquitectura micro-macro utilizable: hogares heterogéneos, restricciones de liquidez, expectativas parciales y una respuesta agregada que retroalimenta precios, ingresos y tasas. Sin embargo, no estudia selección evolutiva, estrategias estables ni adaptación a políticas repetidas. La conexión con EGT es una extensión propuesta, no un resultado del paper.

Una agenda EGT legítima sería estudiar si la exposición reiterada a transferencias e impuestos selecciona heurísticas fiscales distintas, si esas estrategias se estabilizan por clase patrimonial o entorno informativo y cómo alteran la eficacia de políticas futuras.

### EPT

La transferencia y su comunicación pueden interpretarse como una intervención institucional que exterioriza el diseño fiscal en el entorno de decisión de los hogares. El tratamiento informativo E3 muestra que modificar ese entorno cambia expectativas y conducta. Esto constituye convergencia estructural con EPT, pero el paper no estudia replicación institucional, herencia, fitness jurídico ni fenotipos extendidos.

### Memetica y WEIRD bias

El paper informa que la mediana dedica una hora semanal a información económica, recibe noticias de menos de dos fuentes y que 70% menciona redes sociales. Es un punto de partida para investigar vehículos meméticos de comprensión fiscal, no evidencia causal de que las redes produzcan no equivalencia ricardiana.

La muestra es estadounidense y de 22 a 65 años. No debe generalizarse a Argentina, Uruguay o América Latina sin replicación local; las instituciones fiscales, inflación, informalidad, confianza y experiencia con crisis pueden modificar drásticamente las expectativas.

## Herramienta formal utilizable

El parámetro de descuento cognitivo `lambda`, donde `lambda = 1` representa información completa y expectativas racionales, puede inspirar un proxy operacional del desajuste de intencionalidad fiscal. No debe identificarse automáticamente `1 - lambda` con una medida general de intencionalidad.

Una formulación propia más limpia sería:

```text
FIG_h = distancia(E_policy[T_(t+h)], E_household[T_(t+h)])
```

donde `FIG_h` es la brecha de intencionalidad fiscal en el horizonte `h`. Su efecto agregado debe interactuar con la MPC y con brechas separadas sobre ingreso, inflación y tasas.

## Evidencia principal

- Encuesta Prolific, 6.000 respuestas, 99% reunidas entre diciembre de 2024 y enero de 2025.
- E1: transferencia individual de USD 1.400, MPC media 0,314.
- E2: transferencia universal de USD 1.400, propensión a gastar 0,328; diferencia frente a E1 de 0,014, `p = 0,18`.
- El tratamiento universal no modifica significativamente expectativas tributarias a uno, dos o seis años.
- E3: transferencia universal con información explícita de un impuesto personal de USD 1.400 al año siguiente; propensión a gastar 0,272, significativamente menor que E1.
- Calibración conservadora: la inatención aumenta aproximadamente 25% el multiplicador de transferencias frente a FIRE.
- Calibración alternativa: incremento aproximado de 50%.
- Multiplicador de gasto público de primer año: 0,95 bajo FIRE y entre 1,09 y 1,15 bajo inatención.

## Citas clave

> "People do not revise their expected tax liabilities to universal transfers and their planned propensity to spend out of transfers equals their marginal propensity to consume." (p. 1)

> "But even with this additional information, Ricardian Equivalence does not hold." (Appendix C.1, p. 11)

## Limitaciones del paper

- Las decisiones son planes declarados ante escenarios hipotéticos, no gasto observado después de una política real.
- La muestra es de Estados Unidos, reclutada en Prolific y limitada a personas de 22 a 65 años.
- El modelo calibra una forma parsimoniosa de descuento cognitivo; otras explicaciones pueden producir patrones semejantes.
- El tratamiento E2 no especifica quién soportará finalmente los impuestos, aunque E3 reduce esa ambigüedad.
- El modelo no incorpora capital ni inversión y no estima desplazamiento de inversión privada.
- La evidencia no demuestra mecanismos evolutivos, meméticos o jurídicos.
- Es un NBER Working Paper y puede cambiar antes de publicación en revista.

## Propuesta de articulo

**Titulo recomendado:** El contribuyente que el modelo supone: no equivalencia ricardiana y desajuste de intencionalidad fiscal.

**Contribucion propia:** reinterpretar la no equivalencia ricardiana como un caso empírico de mismatch multinivel entre el modelo fiscal del diseñador, el modelo mental del hogar y la dinámica emergente del sistema. La tesis nueva no debe ser que el paper prueba GIMT, sino que proporciona evidencia y una formalización económica compatibles con una predicción específica de GIMT.

## Next actions

- [ ] Redactar un artículo puente centrado en GIMT/IMT, con EGT y EPT como agenda secundaria.
- [ ] Citar el NBER Working Paper 34691 mediante su DOI y verificar su versión antes de publicar.
- [ ] Diseñar una réplica argentina con tratamientos sobre transferencias, inflación, impuestos presentes y deuda futura.
- [ ] Formalizar `FIG_h` y distinguir brechas sobre impuestos, ingresos, tasas e inflación.
- [ ] Contrastar el resultado con *The Generalized Intentionality Mismatch Theorem* y *Game Theory's Hidden Assumption*.
- [ ] No presentar `lambda` como medida directa de nivel de intencionalidad sin validación independiente.
