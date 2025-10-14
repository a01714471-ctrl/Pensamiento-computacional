"""
Proyecto Final - GESTOR DE GASTOS
Descripción:
Este programa permite registrar, consultar y analizar gastos guardados en un archivo CSV.
Cada gasto incluye fecha, categoría, descripción, monto y clasificación.
Calcula total, promedio, mayor, menor y porcentaje de cada gasto.
Incluye funciones, condicionales, listas anidadas, ciclos while y for, 
y un menú interactivo.
"""

import csv  # Para guardar y leer gastos en CSV
import os   # Para verificar existencia del archivo CSV
from datetime import datetime  # Para obtener la fecha actual


def sumar(total, gasto):
    return total + gasto


def contar(cantidad):
    return cantidad + 1


def promedio(total, cantidad):
    return total / cantidad


def mayor(actual, gasto):
    if gasto > actual:
        return gasto
    return actual


def menor(actual, gasto):
    if gasto < actual:
        return gasto
    return actual


def porcentaje_gasto(gasto, total):
    return (gasto / total) * 100


def clasificar_gasto(gasto):
    if gasto < 150:
        return "Bajo"
    elif gasto <= 500:
        return "Medio"
    else:
        return "Alto"


def validar_gasto():
    """Solicita un gasto positivo."""
    gasto = -1
    while gasto <= 0:
        gasto = float(input("Ingrese un gasto positivo: "))
        if gasto <= 0:
            print("El gasto debe ser mayor que cero.")
    return gasto


def guardar_gasto_csv(gasto):
    """Guarda un gasto nuevo en el archivo CSV."""
    with open("gastos.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(gasto)


def cargar_gastos():
    """Carga los gastos desde el archivo CSV si existe."""
    gastos = []
    if os.path.exists("gastos.csv"):
        with open("gastos.csv", "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                if len(row) == 5:
                    fecha, categoria, descripcion, monto, clasificacion = row
                    monto = float(monto)
                    gastos.append([fecha, categoria, descripcion, monto, clasificacion])
    return gastos


def registrar_gasto(gastos, total, cantidad, mayor_gasto, menor_gasto):
    """Registra un gasto y actualiza totales."""
    fecha = datetime.now().strftime("%d/%m/%Y")  # Formato día/mes/año

    categoria = input(
        "Ingrese la categoría (comida, transporte, ocio, etc.): "
    ).capitalize()

    descripcion = input("Ingrese una descripción del gasto: ")
    monto = validar_gasto()
    clasificacion = clasificar_gasto(monto)

    total = sumar(total, monto)
    cantidad = contar(cantidad)

    if cantidad == 1:
        mayor_gasto = monto
        menor_gasto = monto
    else:
        mayor_gasto = mayor(mayor_gasto, monto)
        menor_gasto = menor(menor_gasto, monto)

    gasto = [fecha, categoria, descripcion, monto, clasificacion]
    gastos.append(gasto)
    guardar_gasto_csv(gasto)

    print("Clasificación del gasto:", clasificacion)
    print("Gasto registrado correctamente.\n")

    return gastos, total, cantidad, mayor_gasto, menor_gasto


def mostrar_historial(gastos):
    """Muestra todos los gastos registrados."""
    if len(gastos) == 0:
        print("No hay gastos registrados.\n")
        return

    print("HISTORIAL DE GASTOS")

    for i in range(len(gastos)):
        print("Gasto", i + 1)
        print("Fecha:", gastos[i][0])
        print("Categoría:", gastos[i][1])
        print("Descripción:", gastos[i][2])
        print("Monto: %.2f" % gastos[i][3])
        print("Clasificación:", gastos[i][4])

    print("\n")


def mostrar_reporte(gastos):
    """Calcula y muestra total, promedio, mayor, menor y porcentaje por gasto."""
    if len(gastos) == 0:
        print("No hay gastos registrados.\n")
        return

    total = 0
    for g in gastos:
        total += g[3]

    mayor_gasto = gastos[0][3]
    menor_gasto = gastos[0][3]

    for i in range(1, len(gastos)):
        mayor_gasto = mayor(mayor_gasto, gastos[i][3])
        menor_gasto = menor(menor_gasto, gastos[i][3])

    print("\nREPORTE DE GASTOS")
    print("Total de gastos: %.2f" % total)
    print("Promedio de gastos: %.2f" % promedio(total, len(gastos)))
    print("Mayor gasto: %.2f" % mayor_gasto)
    print("Menor gasto: %.2f" % menor_gasto)
    print("\nDetalle de cada gasto:")

    for i in range(len(gastos)):
        pct = porcentaje_gasto(gastos[i][3], total)
        print(
            "Gasto", i + 1, ": %.2f (%.2f%%) - Clasificación: %s"
            % (gastos[i][3], pct, gastos[i][4])
        )

    print()


def mostrar_menu():
    """Muestra el menú principal."""
    print("MENU PRINCIPAL")
    print("1. Registrar gasto")
    print("2. Ver historial de gastos")
    print("3. Ver reporte de gastos")
    print("4. Salir")


# Programa principal
gastos = cargar_gastos()
total = 0
cantidad = len(gastos)
mayor_gasto = 0
menor_gasto = 0
opcion = ""

while opcion != "4":
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        gastos, total, cantidad, mayor_gasto, menor_gasto = registrar_gasto(
            gastos, total, cantidad, mayor_gasto, menor_gasto
        )

    elif opcion == "2":
        mostrar_historial(gastos)

    elif opcion == "3":
        mostrar_reporte(gastos)

    elif opcion == "4":
        print("Gracias por usar el gestor de gastos. ¡Hasta luego!")

    else:
        print("Opción no válida. Intente de nuevo.\n")


