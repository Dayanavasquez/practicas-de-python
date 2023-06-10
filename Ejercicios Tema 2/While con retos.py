# Ejercicio 1
# Escriba un programa que simule una hucha. El programa solicitará primero una
# cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el
# programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el
# total ahorrado iguale o supere al objetivo. El programa comprobará que las
# cantidades sean positivas.
# Ejemplo de Ejecución:
# HUCHA
# ¿Cuántos euros quieres ahorrar?: -10
# Por favor, escribe una cantidad positiva.
# ¿Cuántos euros quieres ahorrar?: 20.5
# ¿Cuántos euros quieres meter en la hucha?: 20.6
# ¡Objetivo conseguido! Has ahorrado 20.6 euros.


"""cantidad_ahorrada = 0
objetivo = float(input("Ingrese la cantidad de dinero que desea ahorrar: "))

while objetivo <= 0:
        print("La cantidad ingresada debe ser positiva.")
    objetivo = float(input("Ingrese la cantidad de dinero que desea ahorrar: "))


while cantidad_ahorrada < objetivo:
    cantidad = float(input("Ingrese una cantidad para ahorrar (0 o negativo para salir): "))

    while cantidad <= 0:
        print("La cantidad ingresada debe ser positiva.")
    cantidad = float(input("Ingrese la cantidad de dinero que desea ahorrar: "))

    cantidad_ahorrada= cantidad_ahorrada + cantidad

print("Total ahorrado:", cantidad_ahorrada)

print("¡Objetivo conseguido! Has ahorrado", total_ahorrado)"""

# Ejercicio 2
# Crear un programa que solicite al usuario las notas que ha ido sacando en la carrera
# (de forma numérica y del 1 al 10, si es mayor de 10 habrá que mostrar un mensaje de
# error). Cuando el usuario pulse -1 se parará de pedir las notas y se mostrará cuántas
# notas ha introducido, cuantas han sido aprobadas (mayor o igual a 5) y cuales han
# sido suspensas.
# OJO! No deberá contar en el total la nota -1 que utilizaremos para salir.
# Ejemplo Ejecución:
# Introduce la nota: 4
# Introduce la nota: 10
# Introduce la nota: 2
# Introduce la nota: 3
# Introduce la nota: 11
# ERROR: La nota es incorrecta, tiene que ser entre 0 y 10.
# Introduce la nota: 0
# Introduce la nota: -1
# La cantidad de notas son: 5  CANTIDAD ES UN CONTADOR
# La cantidad de notas aprobadas son: 1
# La cantidad de notas suspensas son: 4

#YO
"""notas_usuario= 0
cantidad= 1

while notas_usuario != -1:

    notas_usuario = int(input("Introduzca las notas que ha ido sacando en la carrera (de forma numérica y del 1 al 10: "))
    if notas_usuario > 10:
        print("Error, la nota debe ser del 1 al 10")
    else:
        notas_usuario= int(input("Introduzca las notas que ha ido sacando en la carrera (de forma numérica y del 1 al 10: "))
    cantidad= cantidad + 1

print("La cantidad de notas son: ", cantidad)
print("La cantidad de notas aprobadas son: ")
print("La cantidad de notas suspensas son: ")"""

#CLASE

"""while notas_usuario != -1:
    notas_usuario = int(input("Introduzca las notas que ha ido sacando en la carrera (de forma numérica y del 1 al 10: "))
    contador= contador + 1"""

# Ejercicio 3
# Hacer un programa que simule los procesos de extracción de un cajero automático,
# permitiendo que el usuario tenga tres intentos de ingreso, en caso de error se
# deberá bloquear la tarjeta y saldremos de la aplicación. Si ingresa al sistema, el
# cajero deberá seleccionar entre la cuenta de ahorro, crédito o corriente.
# Una vez que haya seleccionado la cuenta, tendrá que elegir la cantidad a retirar (se
# deberá comprobar que tenga saldo suficiente, sino se le volverá a pedir la cantidad),
# se le descontará del saldo de la cuenta, se mostrará su saldo restante y nos volverá a
# preguntar el menú de selección de las cuentas. Con la opción 4 sale de la
# aplicación.

# OPCION A
contador= 1
contraseña= 1234
password= ""

while password != contraseña:
    password = input("Introduzca su contraseña: ")
    if password != contraseña:
        print("LA contraseña es incorrecta")
        contador= contador+1

print("Fin")