# Prompt de inicio de proyecto — Tesina: Diseño de Placas Base (NTC-2023)

> **Instrucciones para Yamileth:** Copia todo el texto que está dentro del bloque gris de abajo y pégalo tal cual en el chat de GitHub Copilot (panel de chat, modo **Agent**). Asegúrate de tener abierta la carpeta del proyecto en VS Code antes de enviarlo.

---

````
Eres mi agente de código en este proyecto de tesina de ingeniería civil. Antes de hacer cualquier cosa, necesito que te llenes de contexto completo del repositorio y que luego prepares mi entorno de trabajo en Windows para poder ejecutar el notebook principal.

---

## PASO 1 — Lee y analiza el repositorio completo

Por favor realiza las siguientes lecturas en paralelo para entender el proyecto:

1. Lee el archivo `README.md` en la raíz del proyecto. Contiene la descripción del proyecto, hipótesis, alcances, estructura de carpetas y guía de instalación.
2. Lee el notebook `casos_de_estudio.ipynb`. Contiene 11 celdas con el procedimiento completo de diseño de placas base según NTC-2023 (Capítulo 13). Solo usa `import math`, no tiene dependencias externas.
3. Lee los archivos en `tools/`: `caso1_flexocompresion_bloque1.py`, `caso1_flexocompresion_bloque2.py`, `caso1_flexocompresion_bloque3.py`, `caso1_flexocompresion_bloque4.py` y `extract_pdf_pages.py`. Son scripts auxiliares autocontenidos que replican cada bloque de cálculo del notebook.
4. Lee `tesis_escrita/main.tex` para entender la estructura del documento LaTeX.

Cuando termines de leer, dame un resumen breve de lo que hace el proyecto antes de continuar con el Paso 2.

---

## PASO 2 — Diagnóstico completo del entorno Windows

Ejecuta los siguientes comandos en la terminal integrada de VS Code (PowerShell o CMD) para saber exactamente qué tengo instalado. No supongas nada: ejecuta cada comando y muéstrame la salida real.

### 2.1 Versión de Python y ubicación
```powershell
python --version
python -c "import sys; print(sys.executable)"
```

### 2.2 Verificar si pip está disponible
```powershell
pip --version
```

### 2.3 Verificar si ipykernel está instalado
```powershell
pip show ipykernel
```

### 2.4 Verificar si jupyter está instalado
```powershell
pip show jupyter
pip show notebook
pip show jupyterlab
```

### 2.5 Listar kernels de Jupyter ya registrados
```powershell
jupyter kernelspec list
```
> Si `jupyter` no está en el PATH, prueba con:
> ```powershell
> python -m jupyter kernelspec list
> ```

### 2.6 Verificar si existe algún entorno virtual en el proyecto
```powershell
Test-Path .venv
Test-Path venv
Test-Path env
```

### 2.7 Verificar si conda está disponible (aunque se espera que no lo esté)
```powershell
conda --version
```

Con base en los resultados, dime:
- ¿Qué versión de Python tengo?
- ¿Tengo `ipykernel` instalado?
- ¿Tengo Jupyter instalado (cualquier variante)?
- ¿Existe ya el kernel `tesina_Yamileth` registrado?
- ¿Hay algún entorno virtual en el proyecto?

---

## PASO 3 — Crear el kernel `tesina_Yamileth`

Con base en el diagnóstico del Paso 2, elige **una sola ruta** de instalación según lo que encontraste:

### Ruta A — No existe entorno virtual (caso más común)

Si no hay `.venv` ni `venv` en el proyecto, crea uno y registra el kernel:

```powershell
# Crear entorno virtual dentro del proyecto
python -m venv .venv

# Activarlo
.\.venv\Scripts\Activate.ps1

# Si PowerShell bloquea la ejecución de scripts, primero ejecuta:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Instalar ipykernel dentro del entorno
pip install ipykernel

# Registrar el kernel con el nombre correcto
python -m ipykernel install --user --name tesina_Yamileth --display-name "tesina_Yamileth"
```

### Ruta B — Ya existe un entorno virtual

Si encontraste `.venv` o `venv`, actívalo y solo instala ipykernel si falta:

```powershell
# Activar el entorno existente
.\.venv\Scripts\Activate.ps1

# Instalar ipykernel si no está
pip install ipykernel

# Registrar el kernel
python -m ipykernel install --user --name tesina_Yamileth --display-name "tesina_Yamileth"
```

### Ruta C — ipykernel ya está en Python global y no quiero entorno virtual

```powershell
# Instalar ipykernel globalmente si falta
pip install ipykernel

# Registrar el kernel
python -m ipykernel install --user --name tesina_Yamileth --display-name "tesina_Yamileth"
```

Después de ejecutar la ruta correspondiente, verifica que el kernel quedó registrado:

```powershell
python -m jupyter kernelspec list
```

Debes ver una línea que diga algo como:
```
tesina_yamileth   C:\Users\...\jupyter\kernels\tesina_yamileth
```

---

## PASO 4 — Seleccionar el kernel en VS Code y ejecutar el notebook

1. Asegúrate de tener el archivo `casos_de_estudio.ipynb` abierto en VS Code.
2. En la esquina superior derecha del notebook verás un botón con el nombre del kernel actual (puede decir "Python 3", "Select Kernel" o similar).
3. Haz clic en ese botón → se abrirá un menú desplegable.
4. Selecciona **"tesina_Yamileth"** de la lista.
   - Si no aparece en la lista inmediatamente, elige "Select Another Kernel…" → "Jupyter Kernel…" y búscalo ahí.
   - Si sigue sin aparecer, recarga VS Code con `Ctrl + Shift + P` → "Developer: Reload Window" y repite.
5. Una vez seleccionado el kernel, ejecuta todas las celdas en orden con:
   - `Ctrl + F9` (ejecutar todo), o
   - Haz clic en cada celda y presiona `Shift + Enter`

---

## PASO 5 — Verificación final

Cuando ejecutes la última celda (la celda 11, el resumen de resultados), deberías ver en la salida:

```
=================================================================
CASO DE ESTUDIO 1 — FLEXOCOMPRESIÓN EXTREMA (NTC-2023, Cap. 13)
=================================================================
...
  t_req = √(4·M_u_placa / (F_R·F_y))  = 4.6089 cm  (46.1 mm)
=================================================================
```

Si el espesor `t_req` es aproximadamente **4.6 cm (46 mm)**, el entorno está correctamente configurado y todos los cálculos son correctos.

Si aparece algún error o un espesor absurdamente grande (> 50 cm), muéstrame el mensaje de error completo para que lo diagnostiquemos.

---

## Contexto adicional para el agente

- El notebook usa **únicamente** `import math` (biblioteca estándar de Python). No requiere numpy, pandas ni ningún paquete externo.
- El proyecto es una tesina de la **Universidad Veracruzana, Facultad de Ingeniería Civil**.
- Los cálculos implementan el **Capítulo 13 de las NTC-2023** (Normas Técnicas Complementarias del RCDF).
- El sistema de unidades es **kg y cm** a lo largo de todo el notebook.
- El kernel debe llamarse exactamente `tesina_Yamileth` (con esa capitalización) para ser consistente con el proyecto.
````
