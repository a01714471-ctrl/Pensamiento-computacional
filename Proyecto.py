"""
Avance 4
Algoritmo: Reporte de Gastos con operadores aritméticos
Descripción:
Este algoritmo permite al usuario ingresar tres montos de gastos realizados.
Calcula información relevante usando únicamente operadores aritméticos y estructuras condicionales.
Incluye cálculo de total, promedio, mayor, menor y clasificación individual de cada gasto.
"""

def total_gastos(g1, g2, g3):
    return g1 + g2 + g3

def promedio_gastos(total):
    return total / 3

def mayor_gasto(g1, g2, g3):
    mayor = g1
    if g2 > mayor:
        mayor = g2
    if g3 > mayor:
        mayor = g3
    return mayor

def menor_gasto(g1, g2, g3):
    menor = g1
    if g2 < menor:
        menor = g2
    if g3 < menor:
        menor = g3
    return menor

def porcentaje_gasto(gasto, total):
    return (gasto / total) * 100

def clasificar_gasto(gasto):
    if gasto < 150:
        return "Bajo"
    elif gasto <= 500:
        return "Medio"
    else:
        return "Alto"

gasto1 = float(input("Ingrese el primer gasto: "))
gasto2 = float(input("Ingrese el segundo gasto: "))
gasto3 = float(input("Ingrese el tercer gasto: "))
total = total_gastos(gasto1, gasto2, gasto3)
promedio = promedio_gastos(total)
mayor = mayor_gasto(gasto1, gasto2, gasto3)
menor = menor_gasto(gasto1, gasto2, gasto3)
print("Total de gastos:", total)
print("Promedio de gastos: %.2f" %promedio)
print("Mayor gasto:", mayor)
print("Menor gasto:", menor)
print("Porcentaje gasto 1: %.2f" %(porcentaje_gasto(gasto1, total)), "% Clasificación:", clasificar_gasto(gasto1))
print("Porcentaje gasto 2: %.2f" %(porcentaje_gasto(gasto2, total)), "% Clasificación:", clasificar_gasto(gasto2))
print("Porcentaje gasto 3: %.2f" %(porcentaje_gasto(gasto3, total)), "% Clasificación:", clasificar_gasto(gasto3))
