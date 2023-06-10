# Ejercicio 1
# Escribir un programa que pida al usuario dos números y devuelva su división. Si el
# divisor es cero deberá mostrar un mensaje de Error.

"""numero1= float(input("Introduzca un numero: "))
numero2= float(input("Introduzca un numero: "))
division= numero1 /numero2
if  division == 0:
    print("Error")"""

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
# impar.

"""numero = int(input("Introduzca un número entero: "))

if numero == 0:
    print("ERROR")
if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")"""

# Ejercicio 3
# Los tramos impositivos para la declaración de la renta en un determinado país son los
# siguientes:

# Renta Tipo impositivo
# Menos de 10000€ 5%
# Entre 10000€ y 20000€ 15%
# Entre 20000€ y 35000€ 20%
# Entre 35000€ y 60000€ 30%
# Más de 60000€ 45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
# el tipo impositivo que le corresponde.

"""renta_anual = int(input("Ingrese su renta anual: "))

if renta_anual < 10000:
    tipo_impositivo = 5
elif renta_anual <= 20000:
    tipo_impositivo = 15
elif renta_anual <= 35000:
    tipo_impositivo = 20
elif renta_anual <= 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

print("Su tipo impositivo es:", tipo_impositivo, "%")"""


# Ejercicio 4
# Escribir un programa para una empresa que tiene salas de juegos recreativos para todas las
# edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por
# entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la
# entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe
# pagar 5€ y si es mayor de 18 años, 10€.

"""edad= int(input("Introduzca su edad: "))

if edad < 4:
    precio = "gratis"

elif edad <= 18:
    precio= "5€"

else:
    precio= "10€"

print(" El precio de la entrada es ", precio)"""

# Ejercicio 5
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los
# puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
# pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A
# continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La
# cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del
# nivel.
# Nivel Puntuación

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así
# como la cantidad de dinero que recibirá el usuario.

"""puntuacion = float(input("Introduzca la puntuación del empleado: "))
bonificacion= 2400
inaceptable= 0.0
aceptable= 0.4
meritorio= 0.6
if puntuacion == inaceptable:
    nivel = "Inaceptable"
    pago = bonificacion * puntuacion
elif puntuacion == aceptable:
    nivel = "Aceptable"
    pago = bonificacion * puntuacion
elif puntuacion >= meritorio:
    nivel = "Meritorio"
    dinero = bonificacion * puntuacion
else:
    nivel = "Incorrecto"
    dinero = 0.0 

if nivel != "Puntuación inválida":
    print("Nivel de rendimiento:", nivel)
    print("Cantidad de dinero a recibir:", dinero, "€")
else:
    print("La puntuación ingresada no es válida.")"""

# Ejercicio 6
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
# ingredientes para cada tipo de pizza aparecen a continuación.
# ● Ingredientes vegetarianos: Pimiento y tofu.
# ● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
# función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas
# las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y
# todos los ingredientes que lleva.

# Pregunta al usuario si desea una pizza vegetariana o no
"""print("Bienvenido/a a la Pizzería Bella Napoli") 

opcion = input("¿Desea una pizza vegetariana? (s/n): ")

if opcion.lower() == "s":
    print("Ingredientes disponibles para la pizza vegetariana:")
    print("1. Pimiento")
    print("2. Tofu")
    seleccion = input("Seleccione un ingrediente (1-2): ")
    if seleccion == "1":
        ingredientes = "Mozzarella, tomate, pimiento"
    elif seleccion == "2":
        ingredientes = "Mozzarella, tomate, tofu"
    else:
        print("Opción inválida")
        ingredientes = ""
    if ingredientes:
        print("La pizza elegida es vegetariana.")
        print("Ingredientes: " + ingredientes)
else:
    print("Ingredientes disponibles para la pizza no vegetariana:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    seleccion = input("Seleccione un ingrediente (1-3): ")
    if seleccion == "1":
        ingredientes = "Mozzarella, tomate, peperoni"
    elif seleccion == "2":
        ingredientes = "Mozzarella, tomate, jamón"
    elif seleccion == "3":
        ingredientes = "Mozzarella, tomate, salmón"
    else:
        print("Opción inválida")
        ingredientes = ""
    if ingredientes:
        print("La pizza elegida no es vegetariana.")
        print("Ingredientes: " + ingredientes)"""



# Reto 1
#  Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
# nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
# hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
# programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le
# corresponde.

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ")

if sexo== "M" and nombre.lower() < "m" or sexo=="H" and nombre.lower() > "n":
    grupo= "A"
else:
    grupo= "B"

print("El grupo es: ", grupo)

# Reto 2
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
# por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @)
# pero con dominio immune.institute

# Pedir al usuario que ingrese su correo electrónico
correo_usuario = input("Introduzca su correo electrónico: ")

# Separar la parte antes y después de la arroba
nombre = correo_usuario[: correo_usuario.find("@")]

# Generar el nuevo correo con el dominio "immune.institute"
nuevo_correo_usuario = nombre,"@immune.institute"

# Mostrar el nuevo correo por pantalla
print("Tu nuevo correo es:", nuevo_correo_usuario)

#opción 2
email = input("Introduzca su correo electrónico: ")
arroba= email.find("@")
if arroba== -1:
    print("El email introduido es incorrecto")
else:
    dominio=email[arroba+1:]
    dominio_nuevo= dominio.replace(dominio,"@ibm.com")
    nombre= email[:arroba]
