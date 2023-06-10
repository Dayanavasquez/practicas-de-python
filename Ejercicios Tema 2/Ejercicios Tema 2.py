#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")

#Ejercicio 2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y
#luego muestre por pantalla el contenido de la variable.

variable= "¡Hola Mundo!"
print(variable)

# Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después
#de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
#donde <nombre> es el nombre que el usuario haya introducido.

#Ejercicio 4
#Escribir un programa que muestre por pantalla el resultado de la siguiente
#operación aritmética:

#a= int(input("Introduzca el valor de a: "))
#b= int(input("Introduzca el valor de b: "))
#c= int(input("Introduzca el valor de c: "))

#cuenta= ((a+b)/(b*c))**b


"""cuenta= ((3+2)/(2*5))**2
print("El resultado es igual a", cuenta)

horas_trabajadas= float(input("Introduzca en horas decimal las horas trabajadas"))
coste_hora= float(input("¿Cuál es el coste por hora?"))
print("La paga que corresponde es:",  horas_trabajadas * coste_hora)

#Ejercicio 6
#Escribir un programa que lea un entero positivo, n, introducido por el usuario y
#después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma
#de los n primeros enteros positivos puede ser calculada de la siguiente forma: ***

dato_usuario= print("Introduzca un dato entero positivo")

n= int(input("Introduzca el valor de n, entero positivo: "))

suma= (n*(n+1))/2
print("El resultado es: ", suma)

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por
#pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de
#masa corporal calculado redondeado con dos decimales.
#Fórmula: peso (kg) / [estatura (m)]2

peso= float(input("Introduzca su peso en kg"))
estatura= float(input("Introduzca su estatura en metros"))

imc= peso/estatura**2
imc= round(imc,2)

print( "Tu índice de masa corporal es ", imc )

#Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por
#pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los
#números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la
#división entera respectivamente.

n= int(input( "Introduce un numero entero: "))
m= int(input( "Introduce otro numero entero: "))

division= n/m
resto= n%m

print("La division de ",n, "entre", m, " da un cociente de ", division, " y un resto de ", resto)"""

"""Ejercicio 1
Escribir un programa que solicite al usuario ingresar un número con decimales y almacenarlo
en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número
entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de
la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla
el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado
de la operación."""

"""numero_decimal= float(input("Introduzca un número decimal: "))
numero_entero= int(input("Introduzca un número entero: "))

suma= numero_decimal + numero_entero

print( "El resultado de la suma es ", suma)"""

"""Ejercicio 2
Escribir un programa que solicite al usuario dos números y los almacene en dos variables. En
otra variable almacena el resultado de la suma de esos dos números y luego muestra ese
resultado en pantalla.
A continuación, el programa debes solicitar al usuario que ingrese un tercer número, el cual
se debe almacenar en una nueva variable. Por último, mostrar en pantalla el resultado de la
multiplicación de este nuevo número por el resultado de la suma anterior."""

#opcion 1

"""a,b= [float(s) for s in input("Ingresa dos valores: ").split()]

a= print("Primer valor")
b= print("Segundo valor")

suma= a + b

print("El resultado de la suma es: ", suma)

c= float(input("Ingresa otro número: "))

print("Este es el resultado de la multiplicación de la suma con el número nuevo", suma * c)"""

#Opcion 2
"""a= float(input("Ingresa un número: "))
b= float(input( "Ingresa otro número: "))
suma= a+b
print("Esta es la suma de los dos números", suma)
c= float(input("Ingresa otro número: "))
print("Este es el resultado de la multiplicación de la suma con el número nuevo", suma * c)"""

"""Ejercicio 3
Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por
una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido.
Mostrar el consumo de combustible por kilómetro."""

"""kilometros_recorridos= float(input("Introduzca la cantidad de kilómetros recorridos: "))
litros_combustible= float(input("Introduzca los litros de combustible gastados: "))
combustible_kilometro = kilometros_recorridos/ litros_combustible

print("El consumo de combustible por kilometro: ", combustible_kilometro)"""

"""Ejercicio 4
Escribí un programa que solicite al usuario el ingreso de una temperatura en escala
Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La
fórmula de conversión que se usa para este cálculo es: Celsius = (5/9) * (Fahrenheit-32)"""

"""fahrenheit= float(input("Ingrese temperatura en Farenheit: "))
celsius= 5/9

equivalente= (celsius * (fahrenheit -32))
equivalente_redondeado= round(equivalente,2)

print("El equivalente de Fahrenheit en grados Celcius es: ", equivalente_redondeado)"""

"""Ejercicio 5
Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el
promedio de los tres."""

"""a, b, c = [float(s) for s in input("Ingresa tres valores: ").split()]
print("Valor 1: ", a)
print("Valor 2: ", b)
print("Valor 3: ", c)

promedio= (a+b+c)/ 3

print("El promedio es: ", round(promedio,2)"""

#Ejercicio 6
"""Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo
en una única variable. A continuación, mostrar el resultado final en pantalla."""

"""numero_usuario= float(input("Introduzca un valor: "))
resultado= numero_usuario - (15/100*numero_usuario)


print("El resultado es: ", resultado)"""


#Ejercicio 7
"""Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se
guardarán en dos variables distintas. A continuación, almacena en una variable la
concatenación de la primera palabra, más un espacio, más la segunda palabra. Muestra este
resultado en pantalla."""

"""palabra_1= input("Introduzca una palabra: ")
palabra_2= input("Introduzca otra palabra: ")

concatenada=  palabra_1 + " " + palabra_2

print("Estas son las palabras concatenadas", concatenada)"""

#Ejercicio 8
"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

"""peso_payaso= 112
peso_muneca= 75

payasos_vendidos= int(input("Ingrese el número de payasos a enviar: "))
munecas_vendidas= int(input("Ingrese el número de muñecas a enviar: "))

peso_total= (payasos_vendidos * peso_payaso) + (munecas_vendidas * peso_muneca)

print("El peso total del paquete es de: ", peso_total, "gramos")"""

#Ejercicio 9
"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al
año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la
cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después
el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
segundo y tercer años. Redondear cada cantidad a dos decimales.
balance = inversión * (1 + interés)"""

"""inversion= float(input("Ingrese la cantidad de dinero a depositar "))
interes= 0.04
balance_ano_1= inversion*(1 + interes)
balance_ano_2= balance_ano_1*(1 + interes)
balance_ano_3= balance_ano_2*(1 + interes)
print("Este es el balance del primer año: ", round(balance_ano_1,2))
print("Este es el balance del segundo año: ", round(balance_ano_2,2))
print("Este es el balance del tercer año: ", round(balance_ano_3,2))"""


#Ejercicio 10
"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un
descuento del 60%. Escribir un programa que comience leyendo el número de barras
vendidas que no son del día. Después el programa debe mostrar el precio habitual de una
barra de pan, el descuento que se le hace por no ser fresca y el coste final total."""

"""pan: 3.49
descuento: 0.06
pan_duro: int(input("Introduzca la cantidad de panes de otro día vendidos: "))

print("EL precio habitual de una barra de pan es: ", pan, "euros")
print(" El descuento que se aplica a las barras de pan no fresca es:", descuento * 100, "%")

coste_total: (pan * pan_duro) * (1 - descuento)"""














