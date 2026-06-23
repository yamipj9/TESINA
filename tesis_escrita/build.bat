@echo off
REM Compila main.tex con XeLaTeX + BibTeX en Windows
xelatex -interaction=nonstopmode main.tex
if ERRORLEVEL 1 goto :end
bibtex main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
:end
echo Compilación finalizada.
pause
