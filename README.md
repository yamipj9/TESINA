Plantilla LaTeX para tesina (Universidad Veracruzana)

Estructura principal y comandos para compilar (Windows PowerShell):

1. Abrir PowerShell en el directorio del proyecto (donde está `main.tex`).

2. Ejecutar:

```powershell
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Nota: coloque el logo de la Universidad en `figuras/logo_uv.png` si lo desea.
