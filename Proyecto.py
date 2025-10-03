"""
Avance 6
Descripción:
Este programa permite al usuario registrar la cantidad de gastos que desee.
Cada gasto se analiza para calcular el total, el promedio, el mayor y el menor,
además del porcentaje y la clasificación de cada gasto.
Se usan funciones, operadores aritméticos, condicionales, listas, ciclos while sin break y ciclos for.
"""

def sumar(total,gasto):
    return total+gasto

def contar(cantidad):
    return cantidad+1

def promedio(total,cantidad):
    return total/cantidad

def mayor(actual,gasto):
    if gasto>actual:
        return gasto
    return actual

def menor(actual,gasto):
    if gasto<actual:
        return gasto
    return actual

def porcentaje_gasto(gasto,total):
    return (gasto/total)*100

def clasificar_gasto(gasto):
    if gasto<150:
        return "Bajo"
    elif gasto<=500:
        return "Medio"
    else:
        return "Alto"

def mostrar_reporte(total,cantidad,mayor_gasto,menor_gasto,gastos):
    print("Total de gastos:",total)
    print("Cantidad de gastos:",cantidad)
    print("Promedio de gastos: %.2f"%promedio(total,cantidad))
    print("Mayor gasto:",mayor_gasto)
    print("Menor gasto:",menor_gasto)
    for i in range(cantidad):
        pct = porcentaje_gasto(gastos[i], total)
        print("Gasto",i+1,": %.2f (%.2f%%) - Clasificación:"%(gastos[i],pct),clasificar_gasto(gastos[i]))

total=0
cantidad=0
gastos=[]
gasto=float(input("Ingrese un gasto: "))
total=sumar(total,gasto)
cantidad=contar(cantidad)
mayor_gasto=gasto
menor_gasto=gasto
gastos.append(gasto)
print("Clasificación del gasto:",clasificar_gasto(gasto))
continuar=input("¿Desea introducir otro gasto? (si/no): ").lower()
while continuar=="si":
    gasto=float(input("Ingrese un gasto: "))
    total=sumar(total,gasto)
    cantidad=contar(cantidad)
    mayor_gasto=mayor(mayor_gasto,gasto)
    menor_gasto=menor(menor_gasto,gasto)
    gastos.append(gasto)
    print("Clasificación del gasto:", clasificar_gasto(gasto))
    continuar=input("¿Desea introducir otro gasto? (si/no): ").lower()
mostrar_reporte(total,cantidad,mayor_gasto,menor_gasto,gastos)
