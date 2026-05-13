#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caso de Estudio 1: Flexocompresión Extrema - BLOQUE 4
Momento en la placa y espesor mínimo según NTC-2023 (Cap.13).

Operaciones:
- Calcula M_{u,placa} según Ecs. 13.1.4.2.d y 13.1.4.2.e dependiendo de Y respecto a l.
- Determina el espesor mínimo requerido t_req usando Ec. 13.2.1 con F_R = 0.90:
    t_req = sqrt(4 * M_{u,placa} / (F_R * F_y))

Notas:
- El cálculo de Y y f_pd se repite aquí para mantener el script autocontenido.
- Comentarios hacen referencia a las secciones/ecuaciones solicitadas.

Detener tras este bloque y esperar confirmación para continuar.
"""

import math

# ---------------------------
# DATOS DE ENTRADA (kg, cm)
# ---------------------------
d = 30.5       # cm (perfil IR 305x74.5)
b_p = 16.5     # cm
F_y = 3515.0   # kg/cm^2 (Acero A992)

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
f = 20.0            # cm, distancia eje→centro de anclas en tensión

# Factores
F_R_aplastamiento = 0.65
F_R_flexion = 0.90   # según enunciado (Ec. 13.2.1)

# Número de anclas en tensión (ya usado en Bloque 3)
num_anclas_tension = 2

# ---------------------------
# CÁLCULOS PREVIOS (repetidos para autocontenido)
# ---------------------------
A1 = N * B
A2 = dado_x * dado_y
f_pu_raw = 0.85 * f_c * math.sqrt(A2 / A1)   # Ec. 13.3.1.b
f_pu_limit = 1.7 * f_c
f_pu = min(f_pu_raw, f_pu_limit)
f_pd = F_R_aplastamiento * f_pu               # Sección 13.3.1

# Voladizos críticos (Sección 13.1.1.4)
m = (N - b_p) / 2.0
n = (B - d) / 2.0
l = max(m, n)

# Excentricidad real
e = M_u / P_u

# Cálculo de Y (Ec. 13.1.4.2.f):
# Y = (f + N/2) - sqrt( (f + N/2)^2 - (2 P_u (e + f)) / (B f_pd) )
a = f + N / 2.0
discriminante = a ** 2 - (2.0 * P_u * (e + f)) / (B * f_pd)
if discriminante < 0 and discriminante > -1e-9:
    discriminante = 0.0
if discriminante < 0:
    raise ValueError(f"Discriminante negativo al calcular Y: {discriminante}")

Y = a - math.sqrt(discriminante)

# ---------------------------
# CÁLCULO DE M_{u,placa} (Ecs. 13.1.4.2.d y 13.1.4.2.e)
#
# Interpretación utilizada (consistente con la derivación de Y):
# - a = f + N/2 (distancia desde la cara comprimida hasta la resultante de anclas)
# - Cuando Y <= l (bloque de compresión contenido dentro de la zona central),
#   el momento actuante en la placa se obtiene de la resultante de compresión C
#   actuando a distancia (a - Y/2):
#     M_u_placa = C * (a - Y/2) = B * f_pd * Y * (a - Y/2)   (Ec. 13.1.4.2.d)
# - Cuando Y > l (bloque excede el voladizo crítico), se usa l en lugar de Y:
#     M_u_placa = B * f_pd * l * (a - l/2)                 (Ec. 13.1.4.2.e)

if Y <= l:
    M_u_placa = B * f_pd * Y * (a - Y / 2.0)
    caso = "Y <= l (usar Y)"
else:
    M_u_placa = B * f_pd * l * (a - l / 2.0)
    caso = "Y > l (usar l)"

# Como comprobación, por equilibrio de momentos P_u*(e+f) ≈ M_u_placa cuando Y<=l

# ---------------------------
# Espesor mínimo requerido (Ec. 13.2.1 con F_R = 0.90)
# t_req = sqrt(4 * M_{u,placa} / (F_R * F_y))
# (Se aplica tal como se solicitó; las unidades se mantienen en kg, cm.)
if F_R_flexion * F_y <= 0:
    raise ValueError("F_R_flexion * F_y no puede ser cero o negativo")

t_req = math.sqrt((4.0 * M_u_placa) / (F_R_flexion * F_y))


def resumen_bloque4():
    print("BLOQUE 4: Momento en placa y espesor mínimo (NTC 13.2)")
    print("Unidades: kg, cm")
    print()
    print("Datos y parámetros:")
    print(f"P_u = {P_u:.2f} kg, M_u = {M_u:.2f} kg-cm, e = {e:.4f} cm, f = {f:.2f} cm")
    print(f"A1 = {A1:.2f} cm^2, A2 = {A2:.2f} cm^2")
    print(f"f_pu (raw) = {f_pu_raw:.6f} kg/cm^2, f_pu (usado) = {f_pu:.6f} kg/cm^2")
    print(f"f_pd = {f_pd:.6f} kg/cm^2")
    print()
    print("Voladizos críticos:")
    print(f"m = {m:.4f} cm, n = {n:.4f} cm, l = max(m,n) = {l:.4f} cm")
    print()
    print("Cálculo de Y (Ec. 13.1.4.2.f):")
    print(f"a = f + N/2 = {a:.4f} cm")
    print(f"Discriminante = {discriminante:.6f}")
    print(f"Y = {Y:.6f} cm")
    print(f"Caso usado: {caso}")
    print()
    print("Cálculo de M_{u,placa} (Ecs. 13.1.4.2.d/e):")
    print(f"M_u_placa = {M_u_placa:.3f} kg-cm")
    print(f"(Comprobación: P_u*(e+f) = {P_u * (e + f):.3f} kg-cm)")
    print()
    print("Espesor mínimo (Ec. 13.2.1 con F_R=0.90):")
    print(f"t_req = sqrt(4 * M_u_placa / (F_R * F_y)) = {t_req:.4f} cm")
    print()
    if t_req > 50.0:
        print("ATENCIÓN: espesor requerido es muy grande — revisar hipótesis o considerar diseño alternativo.")


if __name__ == "__main__":
    resumen_bloque4()
