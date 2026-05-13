#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caso de Estudio 1: Flexocompresión Extrema - BLOQUE 3
Equilibrio de fuerzas y tensión en anclas según NTC-2023 Sección 13.1.4.2.

Operaciones realizadas:
- Calcula la longitud del bloque de compresiones Y (Ec. 13.1.4.2.f)
- Calcula la tensión total requerida en anclas T_ua (Ec. 13.1.4.2.h)
- Calcula la demanda por ancla asumiendo 2 anclas en tensión

Unidades: kg, cm

Detener tras este bloque y esperar confirmación para continuar.
"""

import math

# ---------------------------
# DATOS DE ENTRADA (kg, cm) — consistentes con Bloques previos
# ---------------------------
d = 30.5       # cm (perfil)
b_p = 16.5     # cm (perfil)
F_y = 3515.0   # kg/cm^2

# Placa base
N = 50.0       # cm
B = 50.0       # cm

# Dado de concreto
dado_x = 60.0  # cm
dado_y = 60.0  # cm
f_c = 250.0    # kg/cm^2

# Anclas y cargas
P_u = 12000.0       # kg (compresión)
M_u = 1800000.0     # kg-cm
V_u = 4000.0        # kg (no usado aquí)
f = 20.0            # cm, distancia eje→centro de anclas en tensión

# Factor f_R para aplastamiento (Bloque 1)
F_R_aplastamiento = 0.65

# Número de anclas en tensión (según enunciado asumir 2)
num_anclas_tension = 2

# ---------------------------
# CÁLCULOS PREVIOS
# ---------------------------
A1 = N * B
A2 = dado_x * dado_y
f_pu_raw = 0.85 * f_c * math.sqrt(A2 / A1)   # Ec. 13.3.1.b
f_pu_limit = 1.7 * f_c
f_pu = min(f_pu_raw, f_pu_limit)
f_pd = F_R_aplastamiento * f_pu

# Excentricidad real
e = M_u / P_u

# ---------------------------
# Ec. 13.1.4.2.f: cálculo de Y (longitud del bloque de compresión)
# Y = (f + N/2) - sqrt( (f + N/2)^2 - (2 P_u (e + f)) / (B f_pd) )
# Nota: se verifica el discriminante para evitar valores imaginarios.
term_inside_sqrt = (f + N / 2.0) ** 2 - (2.0 * P_u * (e + f)) / (B * f_pd)

if term_inside_sqrt < 0:
    # Si hay pequeña desviación numérica, permitir 0 como tolerancia
    if term_inside_sqrt > -1e-9:
        term_inside_sqrt = 0.0
    else:
        raise ValueError(f"Discriminante negativo en cálculo de Y: {term_inside_sqrt}")

Y = (f + N / 2.0) - math.sqrt(term_inside_sqrt)

# ---------------------------
# Ec. 13.1.4.2.h: tensión total requerida en anclas en tracción
# T_ua = B * f_pd * Y - P_u
T_ua = B * f_pd * Y - P_u

# Demanda por ancla (asumiendo num_anclas_tension anclas en tensión)
if num_anclas_tension <= 0:
    raise ValueError("Número de anclas en tensión debe ser >= 1")

T_por_ancla = T_ua / num_anclas_tension


def resumen_bloque3():
    print("BLOQUE 3: Equilibrio de fuerzas y tensión en anclas (NTC 13.1.4.2)")
    print("Unidades: kg, cm")
    print()
    print("Datos relevantes:")
    print(f"P_u = {P_u:.2f} kg, M_u = {M_u:.2f} kg-cm, f = {f:.2f} cm")
    print(f"A1 = {A1:.2f} cm^2, A2 = {A2:.2f} cm^2")
    print(f"f_pu (raw) = {f_pu_raw:.6f} kg/cm^2, f_pu (usado) = {f_pu:.6f} kg/cm^2")
    print(f"f_pd = F_R * f_pu = {F_R_aplastamiento:.2f} * {f_pu:.6f} = {f_pd:.6f} kg/cm^2")
    print()
    print("Ec. 13.1.4.2.f: Y = (f + N/2) - sqrt((f + N/2)^2 - (2 P_u (e + f)) / (B f_pd))")
    print(f"e = M_u / P_u = {e:.6f} cm")
    print(f"Discriminante = {term_inside_sqrt:.6f}")
    print(f"Y = {Y:.6f} cm")
    print()
    print("Ec. 13.1.4.2.h: T_ua = B * f_pd * Y - P_u")
    print(f"T_ua (total) = {T_ua:.3f} kg")
    print(f"Asumiendo {num_anclas_tension} anclas en tensión → T_por_ancla = {T_por_ancla:.3f} kg por ancla")
    if T_ua <= 0:
        print("ATENCIÓN: T_ua <= 0 → no se requieren anclas en tensión (o hay sobredimensionamiento).")


if __name__ == "__main__":
    resumen_bloque3()
