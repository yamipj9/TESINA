#!/usr/bin/env python3
# Ejecuta secuencialmente las celdas de código de un notebook Jupyter (.ipynb)
# y muestra las salidas en consola. Diseñado para este repo: casos_de_estudio.ipynb

import json
import sys
import os
import traceback

nb_path = os.path.join(os.getcwd(), 'casos_de_estudio.ipynb')
if not os.path.exists(nb_path):
    print('ERROR: no se encuentra', nb_path)
    sys.exit(2)

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

globals_exec = {}

cells = nb.get('cells', [])
for idx, cell in enumerate(cells, start=1):
    if cell.get('cell_type') != 'code':
        continue
    src = ''.join(cell.get('source', []))
    print(f'--- Ejecutando celda de código #{idx} ---')
    try:
        exec(src, globals_exec)
    except Exception:
        print(f'ERROR al ejecutar la celda #{idx}:')
        traceback.print_exc()
        sys.exit(1)

print('=== EJECUCIÓN DEL NOTEBOOK COMPLETADA ===')
