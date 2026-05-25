# Prompts

## Instrucciones generales para todos los prompts
- Objetivo: redactar secciones del marco teórico con nivel de Tesis (mayor profundidad, rigor matemático, citas y vinculación directa al estudio paramétrico ya desarrollado).
- Estilo: académico, formal; usar signos de sección claros; emplear KaTeX para todas las ecuaciones ($...$ o $$...$$).
- Fuentes: priorizar artículos revisados por pares, normas aplicables y capítulos de libros técnicos; incluir referencias completas. Incluir mínimo 8–15 referencias en la revisión extensa.
- Alineación obligatoria: en cada sección hay que cotejar y justificar explícitamente las decisiones y valores usados en el análisis paramétrico — extraer los parámetros y ejemplos numéricos de [notebooks/analisis_parametrico.ipynb](notebooks/analisis_parametrico.ipynb) (por ejemplo: `P_u`, `M_u`, `e`, `e_crit`, `Y`, `t_req`, casos numéricos mostrados).
- Entregable: para cada prompt generar un texto final (subsección) y un breve anexo con: 1) lista de ecuaciones derivadas, 2) tablas de parámetros del notebook utilizados y su justificación, 3) lista de referencias citadas.

---

## 1) Contexto y alcance (Intro del Marco Teórico)
Prompt:
- Redacta una subsección que motive el cambio de "tesina" a **Tesis**, explicando el nuevo nivel de profundidad, objetivos de contribución y exigencia metodológica.
- Incluir: relevancia técnica del problema (placas base bajo flexocompresión), impacto práctico y científico, y delimitación clara del alcance (qué se cubre y qué queda fuera).
- Estructura: (a) contexto general, (b) antecedentes inmediatos, (c) razones para ampliar a Tesis, (d) vínculo explícito con el estudio paramétrico existente.
- Requisito numérico: 400–700 palabras; citar al menos 5 fuentes clave (normas, artículos recientes).
- Alinear con notebook: extraer y mencionar el objetivo práctico que sigue el notebook y cómo éste motiva el marco teórico (referenciar [notebooks/analisis_parametrico.ipynb](notebooks/analisis_parametrico.ipynb)).

Checklist de salida:
- Explicación del alcance y contribución.
- Mapa de correspondencia con el estudio paramétrico (línea por línea: objetivo práctico → fundamento teórico requerido).

---

## 2) Objetivos y preguntas de investigación
Prompt:
- Formular Objetivo General y 3–5 Objetivos Específicos que deriven del estudio paramétrico y de las carencias detectadas en la bibliografía.
- Proponer hipótesis verificables que el análisis paramétrico puede confirmar o refutar (p. ej. relación entre excentricidad $e$ y espesor requerido $t_{req}$).
- Incluir: medidas observables del notebook que validan cada objetivo (por ejemplo: `P_u`, `M_u`, `t_req`, criterios de falla).
- Extensión: 200–400 palabras; añadir una tabla breve (2 columnas) que empareje cada objetivo con la(s) celdas/funciones del notebook a usar (p. ej. `disenar_placa_base()`).

---

## 3) Revisión bibliográfica y estado del arte
Prompt:
- Redacta una revisión crítica organizada en subtemas: (A) Historia y evolución de criterios de diseño de placas base; (B) Modelos teóricos clásicos (bloque de compresión, teoría de placas); (C) Estudios experimentales relevantes; (D) Estudios numéricos y análisis paramétricos recientes; (E) Comparativa de normas y vacíos.
- Para cada subtema: resumir aportes, metodologías y limitaciones; evaluar calidad de evidencia y reproducibilidad.
- Requisito: incluir una tabla comparativa que liste al menos 12 estudios (año, método, rango de parámetros, principales conclusiones) y otra tabla que compare las normas relevantes (columna: apartado/norma, fórmula/criterio, supuestos).
- Extensión: 1200–2000 palabras; citar 15–25 referencias (mezcla de clásicos y recientes).
- Alineación con notebook: identificar estudios que han analizado los mismos parámetros que aparecen en [notebooks/analisis_parametrico.ipynb](notebooks/analisis_parametrico.ipynb) y comentar diferencias metodológicas.

Criterios de rigor:
- Crítica metodológica explícita (sensibilidad a discretización, diferencias en criterios de falla, uso/omisión de no linealidad).
- Señalar huecos que la Tesis pretende cubrir.

---

## 4) Fundamentos físicos y formulación conceptual
Prompt:
- Derivar y explicar los principios físicos que gobiernan la flexocompresión de placas base: equilibrio axial + flexión, distribución de presiones, bloque de compresión, interacción con anclas y tensiones locales.
- Incluir derivaciones matemáticas paso a paso para:
  - relación de excentricidad $e=\dfrac{M_u}{P_u}$;
  - tensiones combinadas: $\sigma_a=\dfrac{P}{A}$, $\sigma_b=\dfrac{M\,y}{I}$, y regla de superposición para diseño (comprobación frente a $f_y$);
  - definición y cálculo de $Y$ (bloque de compresión) y criterio para $e_{crit}$.
- Requisitos matemáticos: mostrar supuestos y límites de validez; no omitir pasos algebraicos importantes; usar KaTeX para todas las expresiones.
- Extensión: 800–1200 palabras + ecuaciones.
- Vinculación práctica: para cada ecuación indicar cómo se implementa o aparece en [notebooks/analisis_parametrico.ipynb](notebooks/analisis_parametrico.ipynb) (p. ej. celda que calcula $t_{req}$).

Validación:
- Incluir un ejemplo numérico corto que replique el caso mostrado en el notebook (por ejemplo: $P_u=10\ \text{ton}$, $M_u=7\ \text{ton·m}$, $e=70\ \text{cm}$) y mostrar cómo las fórmulas conducen a los valores reportados (ej.: $t_{req}=47.7\ \text{mm}$).

---

## 5) Modelos matemáticos y simplificaciones
Prompt:
- Explicar los modelos matemáticos posibles: teoría de placas delgada (Kirchhoff), placas espesas (Mindlin–Reissner), modelación del bloque de compresión plástica, y modelado de anclas (discreto vs. continua).
- Pedir derivaciones para la forma continua del problema (ecuaciones diferenciales gobernantes) y su no-dimensionalización; discutir escalado y parámetros adimensionales relevantes.
- Justificar qué modelo(es) son adecuados para los rangos paramétricos del notebook y por qué (hipótesis sobre linealidad, pequeñas deformaciones, acoplamiento placa–anclas).
- Requisitos: explicar error esperado por las simplificaciones y criterios para su aceptación.
- Extensión: 600–1000 palabras + ecuaciones.

---

## 6) Propiedades materiales y caracterización
Prompt:
- Documentar propiedades materiales usadas (E, $f_y$, $\nu$, densidades) y su origen (norma, ensayo, base de datos).
- Incluir explicación sobre sensibilidad de resultados a variaciones de propiedades (p. ej. $E\pm10\%$) y justificar los valores escogidos en el análisis paramétrico.
- Requisitos prácticos: extraer la "base de datos de materiales" referenciada en el notebook y adjuntar tabla con rangos y factores de seguridad.
- Extensión: 300–600 palabras + tabla.

---

## 7) Metodología numérica y experimental (vincular al notebook)
Prompt:
- Describir con detalle la metodología numérica empleada: algoritmo, tipo de elementos, mallado, condiciones de contorno, criterios de convergencia, parámetros de solución (tolerancias, solvers).
- Explicar calibración y validación: qué casos experimentales o normativos se usan como referencia.
- Incluir: checklist reproducible que permita a otro investigador ejecutar el mismo análisis (referenciar funciones y celdas en [notebooks/analisis_parametrico.ipynb](notebooks/analisis_parametrico.ipynb); por ejemplo `disenar_placa_base()`).
- Requisito: describir control de calidad del postprocesado (cómo se calculan $e_{crit}$, $t_{req}$, etc.).
- Extensión: 500–900 palabras.

---

## 8) Definición y justificación de variables y rangos paramétricos
Prompt:
- Listar todos los parámetros estudiados en el análisis paramétrico (geométricos, materiales, de carga y numéricos). Para cada uno: definición, unidad, rango analizado, justificación bibliográfica/experimental.
- Incluir tabla con columnas: parámetro | símbolo | rango explorado | valor base | referencia/norma | sensibilidad esperada.
- Requisito: extraer los valores concretos del notebook y justificarlos frente a la literatura; si hay valores arbitrarios, discutir alternativas.
- Extensión: tabla + 200–400 palabras de justificación.

---

## 9) Verificación, validación y análisis de incertidumbre
Prompt:
- Explicar estrategias para verificar el código y resultados (tests unitarios, comparación con soluciones analíticas, convergencia de malla) y para validar ante datos experimentales o normas.
- Diseñar un esquema de análisis de incertidumbre (propagación, Monte Carlo o análisis de sensibilidad local) aplicable a los parámetros críticos del notebook.
- Requisito: proponer métricas cuantitativas (RMSE, diferencias relativas, criterios de aceptación) y umbrales razonables.
- Extensión: 400–800 palabras + pseudocódigo o esquema para implementación.

---

## 10) Mapeo teoría → datos (cómo usar el marco teórico para interpretar los resultados)
Prompt:
- Para cada resultado clave del análisis paramétrico, indicar qué sección teórica lo respalda y cómo debe interpretarse: p. ej. cuando $e>e_{crit}$, qué predice la teoría sobre distribución de esfuerzos y espesor requerido.
- Incluir formato sugerido para tablas y figuras comparativas que muestren teoría vs. notebook (columnas: caso, predicción teórica, resultado notebook, error relativo, comentario).
- Requisito: producir al menos 3 ejemplos de mapeo aplicados a casos del notebook (usar los casos numéricos disponibles).
- Extensión: 300–600 palabras + 3 tablas.

---

## 11) Identificación de lagunas y contribución esperada de la Tesis
Prompt:
- Partiendo de la revisión y del mapeo teoría→datos, identificar 4–6 lagunas científicas o técnicas (p. ej. no linealidad plástica combinada con excentricidad extrema; efecto de anclas en tensión local).
- Para cada laguna: explicar cómo el trabajo propuesto (y el análisis paramétrico) la aborda; definir contribución original esperada.
- Extensión: 300–500 palabras.

---

## 12) Síntesis y conclusiones del marco teórico
Prompt:
- Redactar una síntesis breve y contundente que priorice las implicaciones prácticas y las hipótesis que la Tesis verificará.
- Incluir una lista priorizada de “recomendaciones teóricas” que guíen el análisis de resultados y la discusión final.
- Extensión: 200–300 palabras.

---

## 13) Referencias, criterios de inclusión y apéndices técnicos
Prompt:
- Elaborar criterios de inclusión/exclusión para la bibliografía (tipo de estudio, rigor metodológico, relevancia temporal).
- Generar una primera lista anotada de 20–30 referencias clave con una línea de síntesis para cada una (por qué es relevante).
- Definir qué derivaciones y datos irán al Apéndice (p. ej. deducciones largas, tablas numéricas del notebook, scripts relevantes).
- Extensión: lista + 300 palabras de justificación.

---

## Instrucciones de entrega y control de calidad (final)
- Para cada prompt: entregar (A) texto final de la subsección, (B) anexo técnico con ecuaciones y ejemplo numérico que reproduzca un caso del notebook, (C) tabla que mapee variables del notebook a los símbolos teóricos usados.
- Validación mínima: revisiones por pares internas (2 revisores), comprobación de coherencia dimensional y verificación numérica con al menos un caso del notebook.
- Recordatorio estricto: No editar ni sobrescribir archivos `.txt` del repositorio. Si deseas, puedo guardar este contenido en un archivo llamado `Prompts` (sin extensión) — dime si quieres que lo haga.

---

¿Quieres que genere ahora el texto completo de la primera subsección (Contexto y alcance)?