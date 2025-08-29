"""
Avance 2
Algoritmo: Reporte de Gastos con operadores aritméticos
Descripción:
Este algoritmo permite al usuario ingresar tres montos de gastos realizados.
A partir de estos datos, calcula información relevante utilizando únicamente operadores
aritméticos básicos y comparaciones, sin estructuras complejas ni archivos externos.
"""

gasto_1=float(input("Introduce el monto del primer gasto realizado\n"))
gasto_2=float(input("Introduce el monto del segundo gasto realizado\n"))
gasto_3=float(input("Introduce el monto del tercer gasto realizado\n"))
total=gasto_1+gasto_2+gasto_3
promedio=total/3
mayor=gasto_1
if gasto_2>mayor:
	mayor=gasto_2
if gasto_3>mayor:
	mayor=gasto_3
menor=gasto_1
if gasto_2<menor:
	menor=gasto_2
if gasto_3<menor:
	menor=gasto_3
print("Reporte de los gastos:\n")
print("Total gastado: ",total,"\n")
print("Promedio de gastos: %.2f"%(promedio),"\n")
print("Mayor gasto: ",mayor,"\n")
print("Menor gasto: ",menor)