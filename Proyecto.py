"""
Avance 3
Algoritmo: Reporte de Gastos con operadores aritméticos
Descripción:
Este algoritmo permite al usuario ingresar tres montos de gastos realizados.
A partir de estos datos, calcula información relevante utilizando únicamente operadores
aritméticos básicos y comparaciones, sin estructuras complejas ni archivos externos.
"""

def total(g1,g2,g3):
	suma=g1+g2+g3
	return suma

def promedio(total):
	promedio=total/3
	return promedio

def mayor(g1,g2,g3):
	mayor=g1
	if g2>mayor:
		mayor=g2
	if g3>mayor:
		mayor=g3
	return mayor

def menor(g1,g2,g3):
	menor=g1
	if g2<menor:
		menor=g2
	if g3<menor:
		menor=g3
	return menor

def porcentaje_gasto(gasto,total):
	porcentaje=(gasto/total)*100
	return porcentaje

gasto1=float(input("Ingrese el primer gasto: "))
gasto2=float(input("Ingrese el segundo gasto: "))
gasto3=float(input("Ingrese el tercer gasto: "))
total=total(gasto1, gasto2, gasto3)
promedio=promedio(total)
mayor=mayor(gasto1, gasto2, gasto3)
menor=menor(gasto1, gasto2, gasto3)
print("Total de gastos: ",total)
print("Promedio de gastos: %.2f"%(promedio))
print("Mayor gasto: ",mayor)
print("Menor gasto: ",menor)
print("Porcentaje gasto 1: %.2f"%(porcentaje_gasto(gasto1,total)))
print("Porcentaje gasto 2: %.2f"%(porcentaje_gasto(gasto2,total)))
print("Porcentaje gasto 3: %.2f"%(porcentaje_gasto(gasto3,total)))
