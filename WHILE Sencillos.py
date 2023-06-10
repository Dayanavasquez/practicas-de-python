import random

# Ejercicio 1
# Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es
# menor que 10. Si no lo está, debe volver a leer el número repitiendo la operación hasta que
# el usuario escriba un valor correcto. Finalmente, debe escribir por pantalla el valor leído
# cuando este sea correcto.

"""num=11

while num > 10:
    num= int(input("Introduzca un número menor de 10: "))

print("Su número es: ", num)"""

#OPCIÓN PROFE

"""numero= int(input("Introduzca un número mayor de 10: "))

while numero > 10
    print("Error ha introducido un número mayor de ")"""

# Ejercicio 2
# Modifique el algoritmo del problema anterior para que, en vez de comprobar que el número
# sea menor que 10, compruebe que se encuentre en el rango (0, 20).

"""num= 21

while num <0 or num >20:
    num= int(input("Introduzca un número menor entre 0 y 20: "))

print("Su número es: ", num)"""

#OPCIÖN PROFE

"""num= int(input("Introduzca un número menor entre 0 y 20: "))

while num <0 or num >20:
    num= int(input("Introduzca un número menor entre 0 y 20: "))
    print("Su número es: ", num)"""

# Ejercicio 3
# Modifique el algoritmo del problema anterior para que cuente las veces que ha leído un
# número de teclado y escriba el resultado de entre 0 y 20 por pantalla.

#OPCIÓN YO
"""num= 21
contador= 0

while num <0 or num >20:
    num= int(input("Introduzca un número menor entre 0 y 20: "))
    contador= contador + 1

print("Su número es: ", num)
print("Las veces que ha leído números es: ", contador)"""

#OPCION PROFE

"""contador= 1
num= int(input("Introduzca un número menor entre 0 y 20: "))

while num <0 or num >20:
    print("Error no ha introducido un numero entre 0 y 20)
    num= int(input("Introduzca un número menor entre 0 y 20: "))
    contador= contador + 1

print("Su número es: ", num)
print("Las veces que ha leído números es: ", contador)"""

# Ejercicio 4
# Modifique el algoritmo del problema anterior para que se realicen 5 lecturas por teclado como
# máximo.

"""num= 21
contador= 0

while num <0 or num >20:
    num= int(input("Introduzca un número menor entre 0 y 20: "))
    contador= contador + 1
    if contador == 5:
    print(" Ha excedido el número de intentos")
        break
if numero> 0 or <20:
    print("Su número es: ", num)
print("Las veces que ha leído números es: ", contador)"""

# Ejercicio 5
# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante)
# y la vuelva a solicitar hasta que las dos contraseñas coincidan.

"""contraseña = input("Introduzca su contraseña: ")
password = input("Introduzca su contraseña: ")

while contraseña != password:
    print("Las contraseñas no coinciden ")
    contraseña = input("Introduzca su contraseña: ")
    password = input("Introduzca su contraseña: ")


print("Contraseña correcta")"""

#OPCION B

"""contraseña = input("Introduzca su contraseña: ")
password = input("Introduzca su contraseña: ")

while contraseña != password:
    print("Las contraseñas no coinciden ")
    password = input("Introduzca de nuevo la contraseña anterior: ")


print("Contraseña correcta")"""

# Ejercicio 6
# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante)
# y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres
# peticiones.

# OPCIÓN YO

"""contraseña="1234"
contador= 1

password= input("Introduzca su contraseña: ")

while contraseña != password:
    print( "Contraseña incorrecta")
    contador= contador + 1
    password = input("Introduzca su contraseña: ")
    if contador== 3:
        print("Ha excedido el número de intentos ")
        break

print("Contraseña correcta")"""

#OPCION B

contador= 1
contraseña= input("Introduzca la contraseña: ")
verificación= input("Introduzca la verificación: ")

while contraseña != verificación:
    print("Las contraseñas no coinciden. Intentalo de nuevo.")
    verificación= input("Introduzca otra vez la contraseña: ")
    contador= contador+ 1
    if contador== 3:
        print("Se han acabado los intentos.")
        break

if contraseña == verificación:
    print("La verificación es correcta")
