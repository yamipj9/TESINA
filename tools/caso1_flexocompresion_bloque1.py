#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caso de Estudio 1: Flexocompresión Extrema - BLOQUE 1
Calcula la configuración de variables y la resistencia de aplastamiento
según NTC-2023 (Cap.13). Unidades: kg, cm.

Referencias (NTC-2023):
- Sección 13.3.1 (Ec. 13.3.1.b): cálculo de esfuerzo de aplastamiento f_pu
- Sección 13.1.1.4: voladizos críticos m, n y l

El script calcula:
- A1: área de la placa base (N x B)
- A2: área del dado de concreto
- f_pu: esfuerzo de aplastamiento no aumentado (0.85 f'c sqrt(A2/A1)) limitado a 1.7 f'c
- f_pd: esfuerzo de aplastamiento resistente de diseño = F_R * f_pu (F_R = 0.65)
- m, n, l: voladizos críticos (se usa la interpretación geométrica usual: m=(N-b_p)/2, n=(B-d)/2)

Detener después de este bloque y esperar confirmación para continuar.
"""

import math

# ---------------------------
# DATOS DE ENTRADA (kg, cm)
# ---------------------------
# Perfil IR 305x74.5
d = 30.5       # profundidad total del perfil, cm (d)
b_p = 16.5     # ancho de ala / huella en planta, cm (b_p)
F_y = 3515.0   # kg/cm^2 (Acero A992)

# Placa base
N = 50.0       # cm
B = 50.0       # cm

# Dado de concreto
dado_x = 60.0  # cm
dado_y = 60.0  # cm
f_c = 250.0    # kg/cm^2 (resistencia del concreto)

# Factor de seguridad para aplastamiento (según enunciado)
F_R_aplastamiento = 0.65

# ---------------------------
# CÁLCULOS BLOQUE 1
# ---------------------------

# 1) Áreas (Se usan en Ec. 13.3.1.b)
# A1: área de la placa base (N x B)
A1 = N * B
# A2: área del dado de concreto (dado_x x dado_y)
A2 = dado_x * dado_y

# 2) Esfuerzo de aplastamiento no aumentado f_pu (Ec. 13.3.1.b):
#    f_pu = 0.85 * f'c * sqrt(A2 / A1)
#    límite: f_pu <= 1.7 * f'c  (tal como indica la Sección 13.3.1)
f_pu_raw = 0.85 * f_c * math.sqrt(A2 / A1)
f_pu_limit = 1.7 * f_c
# Aplicar el límite especificado
f_pu = min(f_pu_raw, f_pu_limit)

# 3) Esfuerzo resistente de diseño por aplastamiento f_pd (Sección 13.3.1):
#    f_pd = F_R * f_pu
f_pd = F_R_aplastamiento * f_pu

# 4) Voladizos críticos m, n y l (Sección 13.1.1.4)
#    Interpretación geométrica usada aquí (huella del perfil sobre la placa):
#    m = (N - b_p) / 2   -> espacio libre en la dirección N (cada lado)
#    n = (B - d) / 2     -> espacio libre en la dirección B (cada lado)
#    l = max(m, n)
m = (N - b_p) / 2.0
n = (B - d) / 2.0
l = max(m, n)


def resumen_bloque1():
    """Imprime un resumen de los resultados del Bloque 1."""
    print("BLOQUE 1: Configuración y resistencia de aplastamiento (NTC Cap.13)")
    print("Unidades: kg, cm")
    print()
    print(f"Área placa A1 = N * B = {N:.2f} * {B:.2f} = {A1:.2f} cm^2")
    print(f"Área dado A2 = {dado_x:.2f} * {dado_y:.2f} = {A2:.2f} cm^2")
    print()
    print("Sección 13.3.1 (Ec. 13.3.1.b): f_pu = 0.85 * f'c * sqrt(A2/A1) (límite 1.7 f'c)")
    print(f"f_pu (raw) = {f_pu_raw:.6f} kg/cm^2")
    if f_pu_raw > f_pu_limit:
        print(f"Se aplicó límite: f_pu = min(f_pu_raw, 1.7*f'c) = {f_pu_limit:.6f} kg/cm^2")
    print(f"f_pu (usado) = {f_pu:.6f} kg/cm^2")
    print(f"f_pd = F_R * f_pu = {F_R_aplastamiento:.2f} * {f_pu:.6f} = {f_pd:.6f} kg/cm^2")
    print()
    print("Sección 13.1.1.4: Voladizos críticos (interpretación geométrica)")
    print(f"m = (N - b_p)/2 = ({N:.2f} - {b_p:.2f})/2 = {m:.4f} cm")
    print(f"n = (B - d)/2 = ({B:.2f} - {d:.2f})/2 = {n:.4f} cm")
    print(f"l = max(m, n) = {l:.4f} cm")


if __name__ == "__main__":
    resumen_bloque1()
