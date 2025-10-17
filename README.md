# Pensamiento-computacional
El presente proyecto consiste en el desarrollo de un Gestor de Gastos Personales en Python, diseñado para facilitar el registro, organización y análisis de los gastos cotidianos. Su funcionamiento se basa en un sistema de consola que almacena la información en archivos .csv, lo que asegura un manejo sencillo y compatible con herramientas externas como Excel.

El objetivo principal es proporcionar una herramienta práctica que permita a cualquier persona llevar un mejor control de sus finanzas, a la vez que se demuestra la aplicación de la programación en la solución de problemas reales y cotidianos.
# Gestor de gastos personales 
La administración de los recursos financieros personales es un desafío común en la vida diaria. Con frecuencia, las personas tienen dificultades para organizar sus ingresos y controlar sus gastos cotidianos relacionados con alimentación, transporte, vivienda, entretenimiento, servicios y otras necesidades. La ausencia de un registro claro y sistemático puede derivar en una mala distribución del presupuesto, desconocimiento del destino del dinero o incluso endeudamiento.

El Gestor de Gastos Personales en Python se presenta como una alternativa práctica y eficiente. Se trata de un programa de consola que ofrece funciones esenciales para el registro, organización y análisis de gastos, garantizando la persistencia de la información mediante archivos .csv. Este formato es ampliamente compatible con software como Microsoft Excel o Google Sheets, lo que permite al usuario analizar o ampliar los datos en otras plataformas de manera sencilla.

El proyecto tiene como objetivo promover mejores hábitos de control financiero en cualquier persona, independientemente de su perfil o contexto, mostrando cómo la programación puede aplicarse a la solución de problemas reales. Su diseño modular y escalable permite no solo registrar gastos y consultar reportes, sino también proyectar futuras mejoras, como la generación de gráficos con librerías de Python, la implementación de límites de gasto con alertas automáticas o la incorporación de interfaces gráficas que faciliten aún más la experiencia de uso.

Considero interesante el desarrollo de un Gestor de Gastos Personales en Python porque representa una forma práctica de aplicar la programación a una necesidad real y cotidiana: el control de las finanzas. Muchas veces los gastos diarios parecen pequeños e insignificantes, pero al sumarse pueden generar un impacto importante en el presupuesto. Con este proyecto es posible llevar un registro ordenado que permita analizar en qué se utiliza el dinero y tomar decisiones más conscientes.

# Algoritmo
Inicio

Mostrar el menú principal con opciones:

1 Registrar gasto

2 Ver historial de gastos

3 Ver reporte de gastos

4 Salir

Leer la opción elegida por el usuario.

Si la opción es 1 (Registrar gasto):

Pedir fecha del gasto (puede ser automática).

Pedir categoría (comida, transporte, ocio, etc.).

Pedir descripción (texto).

Pedir monto (número).

Guardar la información en un archivo .csv.

Regresar al menú principal.

Si la opción es 2 (Ver historial de gastos):

Leer el archivo .csv.

Mostrar todos los registros en forma de tabla.

Regresar al menú principal.

Si la opción es 3 (Ver reporte de gastos):

Leer el archivo .csv.

Calcular el gasto total.

Calcular el gasto acumulado por categoría.

Mostrar los resultados en pantalla.

Regresar al menú principal.

Si la opción es 4 (Salir):

Mostrar mensaje de cierre.

Terminar el programa.

Fin

# Referencias al API de Python

- "datetime" (https://docs.python.org/3/library/datetime.html): se usa para obtener la fecha actual de cada gasto.
- "csv" (https://docs.python.org/3/library/csv.html): se usa para guardar y leer los gastos en un archivo CSV.
- "os" (https://docs.python.org/3/library/os.html): se usa para verificar si el archivo CSV existe antes de cargar los datos almacenados.
