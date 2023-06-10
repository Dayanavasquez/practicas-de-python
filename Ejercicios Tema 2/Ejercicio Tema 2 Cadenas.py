

#Cantidad de letras (len)

"""cantidad= len(nombre)

# Reemplaza cadena: .replace

cadena_a_reemplazada= nombre.replace("nombre", "apellido")

#CORTAR CADENAS (SUBSTRING) VARIABLE CON CORCHETES [] ***************

dni= "123456789-G"
numero_dni= dni[:8]
print(numero_dni)
letra= dni[9:]
print(letra)

print(dni[2:-5])
print(dni[::-1]) #inversión de la cadena
print(dni[::-4])


#BUSCAR ELEMENTOS .find

posición= dni.find("G")

#.find() nos devuelve la posicion del primer elemento que encuentre
#refind() nos devuelve el último elemento que encuentre."""

# Ejercicio 1
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después
# muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras
# minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre
# y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando
# mayúsculas y minúsculas como quiera.

"""nombre= input( "Introduzca su nombre completo: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.capitalize())
print(nombre.title())"""

# Ejercicio 2
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el
# usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE>
# es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

"""nombre= input( "Introduzca su nombre: ")
n= lend(nombre)

print(nombre.upper(), "tiene", len(n), "letras.")"""

# Ejercicio 3
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el
# prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-
# 56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre
# por pantalla el número de teléfono sin el prefijo y la extensión.

"""numero= input("Introduzca su número de teléfono, con el siguiente formato +34-913724710-56: ")
extracto= numero[4:13]
print(extracto)"""

# Ejercicio 4
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre
# por pantalla la frase invertida.

"""frase= input("Introduzca una frase: ")
frase_invertida[::-1]
print(frase_invertida)"""

# Ejercicio 5 #.replace
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
# y después muestre por pantalla la misma frase, pero con la vocal introducida en mayúscula.

#OPCION A

"""frase= input("Introduzca una frase: ")
vocal= input("Intriduzca una vocal: ")
frase_may= frase.replace(vocal, vocal.upper())
print(frase_may)"""

#OPCION B SOLO LA ÚLTIMA VOCAL
"""frase= input("Introduzca una frase y una vocal: ")
print(frase[:-1] + frase.upper()[-1])"""

# Ejercicio 6
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para
# que también funcione cuando el día o el mes se introduzcan con un solo carácter.

#OPCION A # HACERLO

fecha= input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

dia= fecha[:fecha.find("/")]
mes= fecha[fecha.find("/") +1:fecha.rfind("/")]
año= fecha[fecha.rfind("/")+1:]

print(dia)
print(mes)
print(año)


#OPCION B .split
"""fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

# Dividir la cadena de entrada en día, mes y año
dia, mes, año = fecha_nacimiento.split('/')

# Comprobar si el día o el mes tienen un solo carácter y agregar un cero a la izquierda si es necesario
if len(dia) == 1:
    dia = '0' + dia
if len(mes) == 1:
    mes = '0' + mes

print("Día:" + dia, "" + mes, "" + año)"""

# Ejercicio 7
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

# OPCIÓN A
"""def mostrar_productos():
    productos = input("Ingrese los productos de la cesta de la compra, separados por comas: ")
    lista_productos = productos.split(",")

    for producto in lista_productos:
        print(producto.strip())  # Eliminamos los espacios en blanco al inicio y al final de cada producto"""

# OPCIÓN B
productos = input("Ingrese los productos de la cesta de la compra, separados por comas: ")
print(productos.replace(",","\n"))

a= "Alejanadro"
b= "Fernandez"

print(a,b, sep= "\n")


# Ejercicio 8
# Escribir un programa que pregunte el nombre de un producto, su precio y un número de
# unidades y muestre por pantalla una cadena con el siguiente formato:
# <producto>: <unidades> unidades x <precio>€ = <total>€
# donde <unidades> es el número de unidades con cinco dígitos, <precio> es el precio unitario
# con 6 dígitos enteros y 2 decimales y <total> es el coste total con 8 dígitos enteros y 2
# decimales.

producto= input("Introduzca el nombre del producto")
precio= float(input("Introduzca el precio")) # 6 digitos y 2 decimales))
unidades= int(input("Introduzca el precio")) # 6 digitos y 2 decimales)) #5 digitos

total= unidades *precio # 8 digitos enteros y 2 decimales"""

print(producto, ":", unidades, "unidades x", precio, "€ =", total, "€")




