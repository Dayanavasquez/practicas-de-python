#Ejercicio 1 (III)
"""Calcular el perímetro y área de un rectángulo dada su base y su altura."""

"""base= float(input("Introduzca la base del rectangulo: "))
altura= float(input("Introduzca la altura del rectangulo: "))

perimetro: print("El perimetro del rectángulo es: ", 2*(base+altura))
area:print("El area del rectángulo es: ", base*altura)"""

#Ejercicio 2
"""Calcular el perímetro y área de un círculo dado su radio."""

"""radio= float(input("Introduce el radio del circulo: "))
pi= 3.1416

perimetro= 2 * pi * radio

print("El perimetro del circulo es: ", perimetro) 

area= pi * (radio ** 2)

print("El area del circulo es: ", area)"""

#Ejercicio 3
"""Mostrar el precio del IVA de un producto con un valor introducido por el usuario y su precio
final."""

"""iva= 21/100
valor_usu= float(input("Introduzca el precio: "))
iva_producto= valor_usu * iva
print("El iva del producto es: ", iva_producto)
precio_final= print("El precio final del producto es: ", valor_usu + iva_producto)"""


#Ejercicio 4
"""Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y
unidades son. Se recuerda que una gruesa son doce docenas."""

"""unidades= int(input("Introduzca una cantidad: "))
docena= 12
docenas= (unidades / docena)
gruesas= (docenas / docena)
gruesas2= (unidades/ 144)

print("La cantidad dada son: ", docenas, "docenas,", gruesas, "gruesas,", unidades,"unidades.", gruesas2)"""

#opcion B, con resto

"""unidades= int(input("Introduzca las unidades: "))
gruesas= unidades // 144
docenas= unidades % 144 // 12
resto_unidades= unidades % 12"""

#Ejercicio 5
"""Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas,
minutos y segundos son."""

"""segundo= 60
segundos = int(input("Introduce los segundos: "))
minutos= segundos/segundo
horas= minutos/ segundo
print("El valor introducido son: ", horas, "horas", segundos, "segundos", minutos,"minutos.")"""

#Opción B, con resto

segundos = int(input("Introduce los segundos: "))

horas= segundos//3600
minutos= segundos % 3600//60
seg= segundos % 60

print("El resultados es: ", horas, "horas", minutos, "minutos", seg, "segundos")



#Ejercicio 4
"""En un plano cartesiano encontramos dos puntos A y B que serán solicitados por teclado como
número decimales. Queremos realizar un programa que calcule la distancia entre los puntos.
El calculo de esta distancia se realiza bajo esa fórmula:"""

"""ax= float(input("Introduzca un número decimal para cordenada ax: "))
ay= float(input("Introduzca un otro número decimal para cordenada ay: "))
bx= float(input("Introduzca un número decimal para cordenada bx: "))
by= float(input("Introduzca otro número decimal para cordenada by: "))
distancia: ((ax-bx)**2 + (ay - b_y)**2)**0.5
print("La distancia total es de: ", round(distancia,2))"""

# Ejercicio 7
# Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y
# empatados, por ABC club en el torneo apertura, se debe de mostrar su puntaje total,
# teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado 1 punto y
# perdido 0 puntos.

"""ganados= int(input("Introduce el número de partidos ganados: "))
empatados= int(input("Introduce el número de partidos empatados: "))
perdidos= int(input("Introduce el número de partidos perdidos: "))


puntos_gan= 3
puntos_emp= 1
puntos_perdidos= 0

print("EL puntaje total del equipo es: ", (ganados * puntos_gan) + (empatados * puntos_emp) + (perdidos* puntos_perdidos)"""

# Ejercicio 8
# Elaborar un algoritmo que permita calcular el número de micro discos 3.5 necesarios para
# hacer una copia de seguridad, de la información almacenada en un disco cuya capacidad se
# conoce.
#
# Hay que considerar que el disco duro está lleno de información, además expresado
# en gigabyte. Un micro disco tiene 1.44 megabyte y un gigabyte es igual a 1,024 megabyte.
# El proceso de cálculo para determinar el número de Megabytes (MG) dado la cantidad
# de Gigabytes (GB) es MG = 1024 x GB, esto se puede determinar también si se aplica
# la regla de tres simple. Para calcular el número de Micro discos de 3.5 se procede a
# dividir el número de Megabytes (MD) calculados entre 1.44 que es la capacidad de un
# solo Micro disco, así: MD = MG / 1.44

#gigabyte es igual a 1,024 megabyte

"""microdisco= 1.44 #megabyte
cap_disco_gb= float(input("Introduce el número de Gigabytes: "))

mg_requeridos = 1024 * cap_disco_gb
resultado= (mg_requeridos/microdisco)

print("La cantidad de microdiscos que se necesitan es: ", round(resultado,2))"""

