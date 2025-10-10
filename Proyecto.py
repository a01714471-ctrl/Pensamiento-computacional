"""
Avance 7 - GESTOR DE GASTOS
Descripción:
Este programa permite registrar, consultar y analizar gastos en memoria.
Cada gasto se guarda junto con su categoría, descripción, monto y clasificación
en una lista anidada (matriz). 
Se calculan el total, promedio, mayor y menor gasto, así como el 
porcentaje que representa cada gasto respecto al total.
Incluye funciones, operadores aritméticos, condicionales, listas anidadas,
ciclos while y for, y un menú interactivo.
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

def validar_gasto():
    """Solicita un gasto positivo."""
    gasto=-1
    while gasto<=0:
        gasto=float(input("Ingrese un gasto positivo: "))
        if gasto<=0:
            print("El gasto debe ser mayor que cero.")
    return gasto

def registrar_gasto(gastos,total,cantidad,mayor_gasto,menor_gasto):
    """Registra un gasto y actualiza totales y valores extremos."""
    categoria=input("Ingrese la categoría (comida, transporte, ocio, etc.): ").capitalize()
    descripcion=input("Ingrese una descripción del gasto: ")
    monto=validar_gasto()
    clasificacion=clasificar_gasto(monto)
    total=sumar(total,monto)
    cantidad=contar(cantidad)
    if cantidad==1:
        mayor_gasto=monto
        menor_gasto=monto
    else:
        mayor_gasto=mayor(mayor_gasto,monto)
        menor_gasto=menor(menor_gasto,monto)
    gastos.append([categoria,descripcion,monto,clasificacion])
    print("Clasificación del gasto:",clasificacion)
    return gastos,total,cantidad,mayor_gasto,menor_gasto

def mostrar_historial(gastos):
    """Muestra todos los gastos registrados (simplificado, sin enumerate)."""
    if len(gastos)==0:
        print("No hay gastos registrados.")
    else:
        print("\nHistorial de gastos")
        for i in range(len(gastos)):
            print("Gasto",i+1)
            print("Categoría:",gastos[i][0])
            print("Descripción:",gastos[i][1])
            print("Monto: %.2f"%gastos[i][2])
            print("Clasificación:",gastos[i][3])

def mostrar_reporte(gastos):
    """Calcula y muestra total, promedio, mayor, menor y porcentaje por gasto sin enumerate."""
    if len(gastos)==0:
        print("No hay gastos registrados.\n")
        return
    total=0
    for g in gastos:
        total+=g[2]

    mayor_gasto=gastos[0][2]
    menor_gasto=gastos[0][2]

    for i in range(1,len(gastos)):
        mayor_gasto=mayor(mayor_gasto,gastos[i][2])
        menor_gasto=menor(menor_gasto,gastos[i][2])

    print("\nREPORTE DE GASTOS")
    print("Total de gastos: %.2f"%total)
    print("Promedio de gastos: %.2f"%promedio(total,len(gastos)))
    print("Mayor gasto: %.2f"%mayor_gasto)
    print("Menor gasto: %.2f"%menor_gasto)
    print("\nDetalle de cada gasto:")
    
    for i in range(len(gastos)):
        pct=porcentaje_gasto(gastos[i][2],total)
        print("Gasto",i+1,": %.2f (%.2f%%)-Clasificación: %s"%(gastos[i][2], pct, gastos[i][3]))

def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1. Registrar gasto")
    print("2. Ver historial de gastos")
    print("3. Ver reporte de gastos")
    print("4. Salir")

gastos=[]
total=0
cantidad=0
mayor_gasto=0
menor_gasto=0
opcion=""
while opcion!="4":
    mostrar_menu()
    opcion=input("Seleccione una opción: ")
    if opcion=="1":
        gastos,total,cantidad,mayor_gasto,menor_gasto=registrar_gasto(gastos,total,cantidad,mayor_gasto,menor_gasto)
    elif opcion=="2":
        mostrar_historial(gastos)
    elif opcion=="3":
        mostrar_reporte(gastos)
    elif opcion=="4":
        print("Gracias por usar el gestor de gastos. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente de nuevo.\n")