entera = 53 #Variable de tipo numérica entera
decimal = 4.2 # Variable de tipo numérica decimal
cadena = "Vivo en Madrid!" #Variable de tipo alfanumérica (cadena)
booleana = True #Variable de tipo booleana
booleana2 = False #Variable de tipo booleana

#Enviar mensajes al usuario
print("Valor de tipo cadena")
print(decimal)
print("Tengo",entera,"años")

#Recoger datos del usuario
años = input("¿Cuántos años tienes? (en número entero) ") #Siempre lo almacena como cadena
print("El usuario tiene", años, "años")

#Conversión de tipos de variables
#int() convertimos en número entero
#float() convertimos en número decimal
#str() convertimos en cadena

años = int(input("Introduce de nuevo tu edad: "))
suma = entera + años
print("La suma es", suma)

numero = 45
numero_cadena = str(numero) #"45"

numero_cadena = "55"
numero = int(numero_cadena) #55

#Operadores
numero_a = 45
numero_b = 9
numero_c = 5

suma = numero_a + numero_b
resta = numero_a - numero_b
multiplicacion = numero_a * numero_b
division = numero_a/numero_b
potencia = numero_c ** 2
resto = 13%2

#Redondear
cuenta = 32543/243
cuenta = round(cuenta,2)
print(cuenta)


