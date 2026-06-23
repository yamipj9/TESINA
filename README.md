# Tesina — Diseño Comparativo de Placas Base: NTC-acero 2017 vs. NTC-acero 2023

**Autora:** Yamileth Pérez Jaramillo  
**Institución:** Universidad Veracruzana — Facultad de Ingeniería Civil  
**Directora:** Prof. Francisco Cisneros  

---

## Descripción del proyecto

Esta tesina realiza un **estudio comparativo del diseño estructural de placas base de columnas de acero** sometidas a flexocompresión, cuantificando el impacto normativo de la transición de las **NTC-acero 2017** a las **NTC-acero 2023** del Reglamento de Construcciones para la Ciudad de México.

El trabajo integra tres componentes:

1. **Documento académico escrito** (redactado en LaTeX): marco teórico, metodología, casos de estudio, análisis comparativo normativo, conclusiones y referencias bibliográficas.
2. **Notebook de casos de estudio** (`casos_de_estudio.ipynb`): implementación numérica del procedimiento normativo (Capítulo 13, NTC-2023) para verificar y reproducir los resultados del documento escrito.
3. **Notebook de análisis paramétrico** (`notebooks/analisis_parametrico.ipynb`): barridos paramétricos sistemáticos que cuantifican las divergencias entre ambas normas bajo variación de profundidad de empotramiento, diámetro de ancla, densidad de estribos y excentricidad.

---

## Hipótesis

> Una placa base de acero A992 diseñada conforme a la Sección 13 de las NTC-2023, ante una combinación de carga axial de compresión y momento flector de gran excentricidad, **requerirá anclas en tensión** y un **espesor de placa mayor** al correspondiente al caso de compresión centrada. El procedimiento normativo permite determinar de forma analítica y verificable la longitud del bloque de compresiones, la tensión en anclas y el espesor mínimo requerido.

Los cambios específicos introducidos en la NTC-2023 — en particular los factores de confinamiento $R_{et}$ y $R_{ev}$ por estribos — incrementan la resistencia disponible del grupo de anclas sin modificar las ecuaciones de diseño de la placa base en sí, produciendo **resultados idénticos** en el dimensionamiento de placa entre ambas normas y **resultados significativamente más favorables** en la resistencia al cono para configuraciones con estribos.

---

## Alcances

- Análisis del **Caso 1 (gran excentricidad)**: excentricidad real `e > e_crit`, con levantamiento parcial de la placa y anclas en tensión.
- Perfil estudiado: **IR 305×74.5** (acero A992, `F_y = 3 515 kg/cm²`).
- Placa base: **50 × 50 cm**, pedestal de concreto `f'c = 250–280 kg/cm²`.
- Cargas de diseño: `P_u = 10 000–15 000 kg`, `M_u = hasta 1 400 000 kg·cm` (14 ton·m).
- Ecuaciones aplicadas: 13.1.4.1, 13.1.4.2 (f y h), 13.2.1 y 13.3.1 de las NTC-2023; y su equivalente en el Apéndice B de las NTC-2017.
- Análisis paramétrico sobre: profundidad de empotramiento `h_ef` (15–50 cm), diámetro de ancla (3/8" a 2"), espaciado de estribos (8–35 cm) y excentricidad (0–14 ton·m).

---

## Diferencias normativas clave (NTC-acero 2017 vs. 2023)

| # | Aspecto | NTC-2017 (Apéndice B) | NTC-2023 (Capítulo 13) | Impacto |
|---|---------|----------------------|----------------------|---------|
| 1 | **Jerarquía** | Apéndice complementario | Capítulo 13 completo con figuras y comentarios | Elimina ambigüedades; certeza jurídica |
| 2 | **Factores F_R** | F_R^apl = 0.65, F_R^flex = 0.90 | Idénticos | Sin cambio en resultados de placa |
| 3 | **Confinamiento en tensión** | Sin R_et | Añade R_et = N·F_R·(0.5·Ae·√(f'c·Ec)) | NTC-2023 más permisiva: mayor R_t |
| 4 | **Confinamiento en cortante** | Sin R_ev | Añade R_ev = N·F_R·Ae·Fy | NTC-2023 más permisiva: mayor R_v |
| 5 | **Distancia al borde** | 6d_o ≥ 100 mm (todos los grados) | 7d_o ≥ 100 mm para A325/A449 | NTC-2023 más restrictiva para alta resistencia |
| 6 | **FEA** | No contempla | Valida uso de elementos finitos con resortes | Permite optimización numérica de placas rigidizadas |

---

## Estructura del repositorio

```
TESINA/
├── README.md                        ← Este archivo
├── analisis_comparativo.csv         ← Datos numéricos del barrido paramétrico (t_req NTC-2017 vs 2023)
├── analisis_de_resultados.csv       ← Descripción, hallazgos y relevancia de cada figura de resultados
├── descripcion_de_figuras.csv       ← Descripción detallada de todas las figuras del documento escrito
├── diferencias_normas/
│   └── comparativa.md               ← Análisis técnico tabla comparativa NTC-2017 vs NTC-2023
├── notebooks/
│   ├── analisis_parametrico.ipynb   ← Análisis paramétrico comparativo (NTC-2017 vs NTC-2023)
│   └── casos_de_estudio.ipynb       ← Notebook principal de cálculo del Caso 1
├── simulador/
│   └── simulador_carga_momento_placa_base.html  ← Herramienta interactiva HTML
├── tools/                           ← Scripts Python auxiliares (cálculos por bloques)
│   ├── caso1_flexocompresion_bloque1.py
│   ├── caso1_flexocompresion_bloque2.py
│   ├── caso1_flexocompresion_bloque3.py
│   ├── caso1_flexocompresion_bloque4.py
│   ├── exec_notebook.py
│   └── extract_pdf_pages.py
└── tesis_escrita/                   ← Documento LaTeX completo
    ├── main.tex                     ← Archivo raíz (compilar desde aquí)
    ├── build.bat                    ← Script de compilación para Windows
    ├── capitulos/
    │   └── capitulo1.tex … capitulo5.tex
    ├── secciones/
    │   ├── portada.tex
    │   ├── resumen.tex
    │   ├── agradecimientos.tex
    │   ├── dedicatoria.tex
    │   └── conclusiones.tex
    ├── anexos/
    │   ├── anexo1.tex
    │   └── apendiceB.tex
    ├── bibliografia/
    │   └── references.bib
    ├── figuras/                     ← Imágenes del documento (incluye figuras de resultados 010–014)
    └── normas/                      ← PDFs de referencia normativa
```

---

## Análisis paramétrico: `notebooks/analisis_parametrico.ipynb`

El notebook implementa **cuatro barridos paramétricos** y una **tabla comparativa final** que cuantifican las divergencias entre ambas normativas. Sistema de unidades: kg-fuerza / cm (métrico técnico mexicano).

### Funciones de diseño implementadas

| Función | Descripción | Diferencia normativa |
|---------|-------------|---------------------|
| `disenar_placa_base()` | Flexocompresión: Y, T_ua, t_req | **Idéntica** en NTC-2017 y NTC-2023 |
| `resist_tension_cono()` | R_t del cono de concreto en tensión | **NTC-2023 añade R_et** (estribos) |
| `resist_cortante_cono()` | R_v del cono de concreto en cortante | **NTC-2023 añade R_ev** (estribos) |
| `dist_minima_borde()` | Distancia mínima al borde c_min | **NTC-2023: 7d_o** para A325/A449 |

### Parámetros del caso semilla (Barridos 1 y 2)

- Perfil: IR 305×74.5 (A992), placa 50×50 cm, f'c = 280 kg/cm²
- Cargas: P_u = 10 ton, M_u = 7 ton·m (gran excentricidad activada)
- Anclas: 2 anclas en tensión, h_ef = 30 cm, s_anc = 25 cm
- Estribo de referencia: #4 @ 15 cm (2 ramas), G42

### Barridos realizados

| Barrido | Variable principal | Rango | Objetivo |
|---------|-------------------|-------|----------|
| **1** | Profundidad h_ef y densidad de estribos | h_ef: 15–50 cm; #3@20, #4@15, #5@10 | Impacto de R_et en Rt y eficiencia η |
| **2** | Diámetro de ancla y tamaño del dado | d_o: 3/8"–2"; dados: 50–90 cm | Efecto del cambio 6d_o → 7d_o para A325/A449 |
| **3** | Momento último M_u (excentricidad) | M_u: 0–14 ton·m | Umbral e_crit, evolución de Y, T_ua y t_req |
| **4** | f'c y espaciado de estribos (mapa de calor) | f'c: 200–400 kg/cm²; s: 10–30 cm | Magnitud relativa de R_et por zona normativa |

---

## Figuras de resultados

Las siguientes figuras se generan automáticamente por `analisis_parametrico.ipynb` y se guardan en `tesis_escrita/figuras/`.

---

### 010 — Impacto del confinamiento por estribos en la resistencia al cono de concreto en tensión

**Archivo:** `tesis_escrita/figuras/010_Impacto del confinamiento por estribos en la resistencia al cono de concreto en tension..png`

**Descripción:** Evalúa la variable de refuerzo transversal (estribos) en el pedestal y su influencia directa en la capacidad del grupo de anclas ante fuerzas de extracción pura, mitigando la falla frágil del concreto. La figura contiene tres paneles: (1) resistencia R_t vs h_ef para distintas configuraciones de estribo (NTC-2017 sin R_et vs. NTC-2023 con R_et), (2) eficiencia de diseño η = T_ua / R_t, y (3) magnitud del aporte R_et por configuración.

**Hallazgo clave:** El confinamiento efectivo alrededor de las anclas restringe el desarrollo tridimensional del cono de falla. Esto incrementa significativamente la ductilidad local, permitiendo que la falla sea gobernada por la fluencia del acero del ancla en lugar del desprendimiento prematuro del concreto. Al aumentar h_ef, el número de estribos que interceptan el cono (N_est = ⌊h_ef / s_est⌋) crece, amplificando el aporte R_et de forma escalonada.

**Relevancia para ingeniería estructural:** Crítico para el diseño sísmico. Las NTC exigen un diseño por capacidad donde se prefiere la fluencia del acero; el uso de estribos confina el núcleo del dado, un requisito indispensable para detallados de alta ductilidad. Este resultado justifica numéricamente que un dado armado con #4@15 cm puede absorber el 100% de la demanda T_ua con una profundidad de empotramiento reducida respecto a la configuración sin estribos.

---

### 011 — Requisitos de distancia mínima al borde libre: impacto normativo del cambio para anclas

**Archivo:** `tesis_escrita/figuras/011_Requisitos de distancia minima al borde libre impacto normativo del cambio para anclas..png`

**Descripción:** Modela la sensibilidad de la capacidad de anclaje frente a la variable geométrica c_min (distancia al borde libre), evaluando el umbral donde el desprendimiento lateral (side-face blowout) gobierna el diseño. Grafica c_min vs. d_o para grados A307, A36, A325 y A449, con la zona de mayor restricción A325 en NTC-2023 sombreada.

**Hallazgo clave:** Se evidencia una penalización severa en la resistencia disponible a medida que los anclajes se acercan a los bordes del pedestal. Los datos demuestran que las distancias mínimas no son solo tolerancias constructivas, sino límites mecánicos para evitar fallas por tracción diagonal en el recubrimiento. El incremento de 6d_o a 7d_o implica un 16.7% más de separación requerida para anclas A325/A449, lo que se vuelve determinante en dados compactos de 50–60 cm.

**Relevancia para ingeniería estructural:** Impacta directamente el dimensionamiento en planta de los pedestales y zapatas. AISC 360 y NTC exigen factores de modificación por efecto de borde (ψ_ed,N) que castigan la resistencia si no se respeta la geometría mínima. Los análisis muestran casos específicos donde la NTC-2017 indicaba cumplimiento pero la NTC-2023 exige rediseño del dado o reubicación de las anclas.

---

### 012 — Comportamiento bajo variación de excentricidad

**Archivo:** `tesis_escrita/figuras/012_Comportamiento bajo variacion de excentricidad..png`

**Descripción:** Panel de cuatro gráficas que documenta la evolución de los parámetros de diseño de la placa base ante un barrido de momento M_u de 0 a 14 ton·m (P_u = 15 ton fijo): (1) excentricidad real e vs. e_crit con zonas de pequeña/gran excentricidad; (2) longitud del bloque de compresión Y; (3) tensión total en anclas T_ua; (4) espesor requerido t_req con comparativo NTC-2017 vs. NTC-2023.

**Hallazgo clave:** Valida que las ecuaciones de flexocompresión producen resultados idénticos en ambas normas (clarificación algorítmica). La única divergencia aparece en la región de gran excentricidad cuando el momento del lado de tensión M_tens = (T_ua/B)·l supera al momento de compresión M_comp: en ese rango la NTC-2023 exige explícitamente el mayor de ambos, incrementando t_req hasta ~2 mm adicionales en los casos más extremos del barrido.

**Relevancia para ingeniería estructural:** Permite identificar con precisión el umbral M_u,crit donde la conexión transfiere del régimen de compresión pura al de flexocompresión con anclas en tensión, y cuantifica cuándo la formulación unificada de la NTC-2023 produce diferencias medibles respecto al Apéndice B de la NTC-2017.

---

### 013 — Mapa de calor: incremento de resistencia al cono en tensión (NTC-2023 vs. NTC-2017)

**Archivo:** `tesis_escrita/figuras/013_Mapa de calor_Incremento de resistencia al cono de tension-NTC-2023 vs NTC-2017..png`

**Descripción:** Cuantifica la divergencia matemática entre las formulaciones de la NTC-2017 y la NTC-2023 para la resistencia a la tensión, mapeando variaciones según la resistencia del concreto f'c (200–400 kg/cm²) y el espaciado de estribos (10–30 cm) para estribo #4 de 2 ramas. Dos mapas: (1) incremento porcentual de R_t; (2) magnitud absoluta de R_et en toneladas.

**Hallazgo clave:** Revela zonas geométricas específicas donde la NTC-2023 resulta significativamente más permisiva. El incremento porcentual refleja una calibración que reconoce el confinamiento real del dado; las zonas de f'c alto + estribos densos (s ≤ 15 cm) concentran los mayores incrementos de R_et, habilitando anclajes más esbeltos en concretos de mayor resistencia.

**Relevancia para ingeniería estructural:** Fundamental para la actualización de memorias de cálculo. Diseños de placas base que operaban al límite de su capacidad bajo la NTC-2017 podrían evitar el ensanchamiento o profundización del pedestal adoptando la formulación NTC-2023 con el refuerzo transversal correctamente cuantificado.

---

### 014 — Resistencia al cono por cortante R_v: NTC-2017 vs. NTC-2023

**Archivo:** `tesis_escrita/figuras/014_Resistencia al cono por cortante Rv - NTC-2017 vs NTC-2023..png`

**Descripción:** Contrasta la capacidad de carga lateral R_v soportada por los anclajes antes de la falla por cortante en el concreto, evaluando cómo el cambio normativo altera las curvas de resistencia ante el cortante basal para f'c = 250, 300 y 350 kg/cm². Incluye panel de componente R_ev (aporte exclusivo NTC-2023) en función del espaciado de estribos.

**Hallazgo clave:** La NTC-2023 reconoce que los estribos que atraviesan el plano de falla lateral aportan una resistencia adicional R_ev = N·F_R·Ae·Fy cuantificable. El incremento sobre R_v es proporcional a la densidad de estribos y se suma directamente a la componente de concreto, desvinculando parcialmente la resistencia al cortante de la geometría del dado.

**Relevancia para ingeniería estructural:** Dictamina la eficiencia estructural ante cortante basal. La NTC-2023, al incorporar R_ev, elimina el conservadurismo excesivo de la NTC-2017 para dados bien armados, solucionando cuellos de botella severos en zapatas de lindero o con poca distancia al borde. Esto exige optimizar el diseño priorizando arreglos de estribos densos en la zona de influencia del cono de falla.

---

## Conclusiones del análisis comparativo

1. **Las ecuaciones de placa base son idénticas.** La transición NTC-2017 → NTC-2023 no modifica el cálculo de Y, T_ua ni t_req para la placa en sí. La NTC-2023 solo formaliza en una ecuación unificada lo que el Apéndice B de la NTC-2017 describía implícitamente.

2. **R_et y R_ev son los cambios de mayor impacto práctico.** La adición de estos factores de confinamiento por estribos puede incrementar la resistencia al cono entre un 15 % y más del 60 % dependiendo de la densidad de refuerzo y la profundidad de empotramiento, habilitando pedestales más esbeltos y econó­micos en zonas sísmicas.

3. **El cambio 6d_o → 7d_o para A325/A449 es geométricamente limitante.** En dados compactos (≤ 60 cm) con anclas de alta resistencia de diámetro ≥ 7/8", la NTC-2023 puede exigir redimensionamiento del dado o reubicación de anclas que la NTC-2017 no detectaría.

4. **El reconocimiento explícito del MEF** abre la puerta al diseño optimizado de placas con cartabones mediante elementos finitos, trascendiendo el conservadurismo del método de líneas de fluencia (Yield-Line).

---

## Qué hace `casos_de_estudio.ipynb`

El notebook está dividido en **11 celdas** que siguen el procedimiento del Capítulo 13 de las NTC-2023:

| Celda | Tipo | Contenido |
|-------|------|-----------|
| 1 | Código | `import math` |
| 2 | Código | Variables globales de entrada (perfil, placa, cargas, factores) |
| 3 | Markdown | Teoría + fórmulas LaTeX: áreas, aplastamiento, voladizos |
| 4 | Código | Bloque 1: `A1`, `A2`, `f_pu`, `f_pd`, `m`, `n`, `l` |
| 5 | Markdown | Teoría + fórmulas: excentricidad real y crítica |
| 6 | Código | Bloque 2: `e`, `e_crit` |
| 7 | Markdown | Teoría + fórmulas: bloque de compresión `Y`, tensión `T_ua` |
| 8 | Código | Bloque 3: `Y`, `T_ua`, `T_por_ancla` |
| 9 | Markdown | Teoría + fórmulas: momento en placa, espesor mínimo |
| 10 | Código | Bloque 4: `M_u_placa`, `t_req` |
| 11 | Código | Resumen completo de todos los resultados |

---
<<<<<<< HEAD

## Configuración del entorno — Guía para Yamileth (Windows + VS Code)

> **¡No te preocupes si nunca has hecho esto!** Sigue los pasos uno por uno, exactamente como se describen. Si algo no funciona, avísale al profesor.

### Paso 1 — Instalar Python

1. Ve a [https://www.python.org/downloads/](https://www.python.org/downloads/) y descarga la versión más reciente (Python 3.12 o superior).
2. Abre el instalador. **MUY IMPORTANTE:** antes de hacer clic en "Install Now", marca la casilla que dice **"Add Python to PATH"**.
3. Haz clic en "Install Now" y espera a que termine.


### Paso 2 — Instalar VS Code

1. Ve a [https://code.visualstudio.com/](https://code.visualstudio.com/) y descarga VS Code para Windows.
2. Instálalo con las opciones predeterminadas.

### Paso 3 — Instalar extensiones en VS Code

1. Abre VS Code.
2. Haz clic en el ícono de cuadrados en la barra izquierda (o presiona `Ctrl + Shift + X`). Esto abre el panel de extensiones.
3. Busca e instala las siguientes extensiones (escribe su nombre en el buscador y haz clic en "Install"):
   - **Python** (de Microsoft)
   - **Jupyter** (de Microsoft)

### Paso 4 — Descargar el proyecto

Si tienes Git instalado, abre una ventana de **PowerShell** (búscala en el menú Inicio) y escribe:

```powershell
git clone https://github.com/TU_USUARIO/TESINA.git
cd TESINA
```

Si no tienes Git, descarga el ZIP desde GitHub → botón verde "Code" → "Download ZIP", y extrae la carpeta donde quieras.

### Paso 5 — Crear el entorno virtual

En la misma ventana de PowerShell, **dentro de la carpeta TESINA**, escribe estos comandos uno por uno (presiona Enter después de cada uno):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install ipykernel numpy pandas matplotlib seaborn
```

Sabrás que el entorno está activo porque verás `(.venv)` al inicio de la línea en la terminal.

### Paso 6 — Crear el kernel `tesina_Yamileth`

Con el entorno activo (ves `(.venv)` en la terminal), escribe:

```powershell
python -m ipykernel install --user --name tesina_Yamileth --display-name "tesina_Yamileth"
```

Verás un mensaje como: `Installed kernelspec tesina_Yamileth in C:\Users\...`
¡Eso significa que funcionó!

### Paso 7 — Abrir el notebook en VS Code

1. En VS Code, abre la carpeta del proyecto: menú **File → Open Folder** y selecciona la carpeta `TESINA`.
2. En el explorador de archivos de la izquierda, haz doble clic en `casos_de_estudio.ipynb`.
3. En la **esquina superior derecha** del notebook verás un botón que dice el nombre del kernel (puede decir "Python 3" o algo similar). Haz clic ahí.
4. En el menú que aparece busca **"tesina_Yamileth"** y selecciónalo.
5. ¡Listo! Ahora puedes ejecutar las celdas haciendo clic en el botón ▶ de cada celda, o con `Shift + Enter`.

> **Tip:** Si no ves `tesina_Yamileth` en la lista, cierra VS Code, vuelve a abrirlo y repite el Paso 7.

---

## Cómo compilar el documento LaTeX (Windows)

1. Instala **MiKTeX** desde [https://miktex.org/download](https://miktex.org/download).
2. Abre una ventana de PowerShell dentro de la carpeta `tesis_escrita/`.
3. Haz doble clic en `build.bat` (o ejecútalo en PowerShell):

```powershell
cd tesis_escrita
.\build.bat
```

El archivo `main.pdf` se generará dentro de `tesis_escrita/`.

---

## ¿Por qué antes el espesor salía de 50 cm? — Diagnóstico del error

El proceso inicial devolvía `t_req ≈ 50.79 cm` (unos 508 mm), un valor completamente inviable en obra. Había **dos errores combinados**:

### Error 1 — Dato de entrada irreal: `M_u = 1 800 000 kg·cm` (18 ton·m)

El momento último ingresado era 18 ton·m para una columna con carga axial de apenas 12 ton. Eso produce una **excentricidad de 150 cm**, es decir, la resultante de la carga cae a **tres longitudes de placa fuera del borde**. En la práctica, un perfil IR 305 con esa carga axial no resistiría ni transferiría un momento de 18 ton·m en la base; la columna o la propia conexión fallarían mucho antes. El valor real para esta combinación es del orden de **6 ton·m** (`M_u = 600 000 kg·cm`).

### Error 2 — Bug de dimensiones en la fórmula de `M_u_placa`

La Ecuación 13.2.1 de las NTC-2023 trabaja con **momento por unidad de ancho** [kg·cm/cm]:

```
t_req = sqrt( 4 · M_u_placa / (F_R · F_y) )
```

El código original calculaba `M_u_placa` multiplicando por `B` (el ancho de la placa), obteniendo un **momento total** [kg·cm] en lugar de uno por unidad de ancho. Eso infla `M_u_placa` por un factor `B = 50`, y por tanto `t_req` por un factor `√50 ≈ 7×`.

**Ambos errores combinados** elevaron el espesor de un valor real de ~4.6 cm (46 mm) a los ~50.8 cm (508 mm) que se veían originalmente.
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Nota: coloque el logo de la Universidad en `figuras/logo_uv.png` si lo desea.
=======
>>>>>>> bbc217a (Actualizacion de README y descipcion de figuras en csv)
