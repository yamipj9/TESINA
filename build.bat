@echo off
REM Compila main.tex con pdflatex + bibtex en Windows
pdflatex -interaction=nonstopmode main.tex
if ERRORLEVEL 1 goto :end
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
:end
echo Compilación finalizada.
pause
