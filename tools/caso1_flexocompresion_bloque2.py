#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caso de Estudio 1: Flexocompresión Extrema - BLOQUE 2
Análisis de excentricidad según NTC-2023 Sección 13.1.4.1.

Entradas: Unidades kg, cm.
Referencias normativas en comentarios para cada ecuación.

Detener después de este bloque y esperar confirmación para continuar.
"""

import math

# ---------------------------
# DATOS DE ENTRADA (kg, cm)
# ---------------------------
# Perfil IR 305x74.5 (redefinidos aquí para consistencia entre bloques)
d = 30.5       # cm
b_p = 16.5     # cm
F_y = 3515.0   # kg/cm^2

# Placa base
N = 50.0       # cm
B = 50.0       # cm

# Dado de concreto
dado_x = 60.0  # cm
dado_y = 60.0  # cm
f_c = 250.0    # kg/cm^2

# Anclas y cargas de diseño (según enunciado)
P_u = 12000.0       # kg (compresión)
M_u = 1800000.0     # kg-cm
V_u = 4000.0        # kg (no usado en este bloque)

# Distancia del eje al centro de anclas en tensión (f)
f = 20.0            # cm

# Factor de diseño para aplastamiento (igual que Bloque 1)
F_R_aplastamiento = 0.65

# ---------------------------
# CÁLCULOS PREVIOS (repetidos del Bloque 1 para autocontenido)
# ---------------------------
A1 = N * B
A2 = dado_x * dado_y
f_pu_raw = 0.85 * f_c * math.sqrt(A2 / A1)   # Ec. 13.3.1.b
f_pu_limit = 1.7 * f_c                         # límite (Sección 13.3.1)
f_pu = min(f_pu_raw, f_pu_limit)
f_pd = F_R_aplastamiento * f_pu               # Sección 13.3.1

# ---------------------------
# BLOQUE 2: Análisis de Excentricidad (NTC 13.1.4.1)
# ---------------------------

# 1) Excentricidad real: e = M_u / P_u  (NTC 13.1.4.1)
e = M_u / P_u  # cm

# 2) Excentricidad crítica (NTC 13.1.4.1):
#    e_crit = N/2 - P_u / (2 * B * f_pd)
#    (interpreta la reducción de la zona comprimida por la resistencia f_pd)
den = 2.0 * B * f_pd
if den == 0:
    raise ZeroDivisionError("Denominador en e_crit es cero (ver f_pd, B)")
e_crit = N / 2.0 - P_u / den


def resumen_bloque2():
    """Imprime resultados del análisis de excentricidad.

    Referencias:
    - NTC Sección 13.1.4.1: definición de excentricidad real y crítica.
    - Ec. usada para f_pd tomada de Sección 13.3.1 (Ec. 13.3.1.b).
    """
    print("BLOQUE 2: Análisis de Excentricidad (NTC 13.1.4.1)")
    print("Unidades: kg, cm")
    print()
    print(f"Cargas: P_u = {P_u:.2f} kg, M_u = {M_u:.2f} kg-cm")
    print()
    print("Cálculo de f_pd (Sección 13.3.1):")
    print(f"A1 = {A1:.2f} cm^2, A2 = {A2:.2f} cm^2")
    print(f"f_pu (raw) = {f_pu_raw:.6f} kg/cm^2, límite 1.7*f'c = {f_pu_limit:.6f} kg/cm^2")
    print(f"f_pu (usado) = {f_pu:.6f} kg/cm^2")
    print(f"f_pd = F_R * f_pu = {F_R_aplastamiento:.2f} * {f_pu:.6f} = {f_pd:.6f} kg/cm^2")
    print()
    print("Sección 13.1.4.1:")
    print(f"Excentricidad real e = M_u / P_u = {M_u:.2f} / {P_u:.2f} = {e:.4f} cm")
    print(f"Excentricidad crítica e_crit = N/2 - P_u/(2*B*f_pd) = {e_crit:.4f} cm")
    print()
    if e <= e_crit:
        print("RESULTADO: e <= e_crit → NO corresponde al Caso 1 (se requiere gran excentricidad).")
        print("Acción: revisar cargas o detenimiento — el procedimiento para Caso 1 no aplica.")
    else:
        print("RESULTADO: e > e_crit → procede el análisis para gran excentricidad (Caso 1).")


if __name__ == "__main__":
    resumen_bloque2()
