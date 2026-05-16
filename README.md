# Tesina — Diseño de Placas Base según NTC-2023

**Autora:** Yamileth Pérez Jaramillo  
**Institución:** Universidad Veracruzana — Facultad de Ingeniería Civil  
**Directora:** Prof. Francisco Cisneros  

---

## Descripción del proyecto

Esta tesina analiza el **diseño estructural de placas base de columnas de acero** sometidas a flexocompresión, utilizando las **Normas Técnicas Complementarias 2023 (NTC-2023)** del Reglamento de Construcciones para el Distrito Federal (Ciudad de México).

El trabajo combina dos componentes:

1. **Documento académico escrito** (redactado en LaTeX): marco teórico, metodología, casos de estudio, conclusiones y referencias bibliográficas.
2. **Herramienta de cálculo interactiva** (Jupyter Notebook en Python): implementación numérica del procedimiento normativo que permite verificar y reproducir todos los resultados del documento escrito.

---

## Hipótesis

> Una placa base de acero A992 diseñada conforme a la Sección 13 de las NTC-2023, ante una combinación de carga axial de compresión y momento flector de gran excentricidad, **requerirá anclas en tensión** y un **espesor de placa mayor** al correspondiente al caso de compresión centrada. El procedimiento normativo permite determinar de forma analítica y verificable la longitud del bloque de compresiones, la tensión en anclas y el espesor mínimo requerido.

---

## Alcances

- Análisis del **Caso 1 (gran excentricidad)**: excentricidad real `e > e_crit`, con levantamiento parcial de la placa y anclas en tensión.
- Perfil estudiado: **IR 305×74.5** (acero A992, `F_y = 3 515 kg/cm²`).
- Placa base: **50 × 50 cm**, pedestal de concreto `f'c = 250 kg/cm²`.
- Cargas de diseño: `P_u = 12 000 kg`, `M_u = 600 000 kg·cm` (6 ton·m), `V_u = 4 000 kg`.
- Ecuaciones aplicadas: 13.1.4.1, 13.1.4.2 (f y h), 13.2.1 y 13.3.1 de las NTC-2023.
- No se cubre el diseño de las anclas individuales ni el diseño del pedestal de concreto.

---

## Estructura del repositorio

```
TESINA/
├── casos_de_estudio.ipynb      ← Notebook principal de cálculo (ejecutar aquí)
├── README.md                   ← Este archivo
├── tools/                      ← Scripts Python auxiliares (cálculos por bloques)
│   ├── caso1_flexocompresion_bloque1.py
│   ├── caso1_flexocompresion_bloque2.py
│   ├── caso1_flexocompresion_bloque3.py
│   ├── caso1_flexocompresion_bloque4.py
│   └── extract_pdf_pages.py
└── tesis_escrita/              ← Todo el documento LaTeX
    ├── main.tex                ← Archivo raíz de LaTeX (compilar desde aquí)
    ├── build.bat               ← Script de compilación para Windows
    ├── capitulos/
    │   ├── capitulo1.tex … capitulo5.tex
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
    ├── figuras/                ← Imágenes usadas en el documento
    └── normas/                 ← PDFs de referencia normativa
```

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
pip install ipykernel
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
