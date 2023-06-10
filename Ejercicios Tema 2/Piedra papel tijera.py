import random

# ELECCION JUGADOR
opcion_jugador= int(input("Introduzca una opción piedra= 1, papel= 2, tijera= 3: "))

if opcion_jugador == 1:
    print("Piedra")
elif opcion_jugador== 2:
    print("Papel")
elif opcion_jugador==3:
    print("Tijera")
else:
    print("Incorrecto. Introduce 1, 2 o 3")


#ELECCION PC
opcion_pc = random.randrange(1, 4)  

if opcion_pc == 1:
     print("Piedra")
elif opcion_pc == 2:
    print("Papel")
else:
    print("Tijera")

# GANADOR
if opcion_pc == opcion_jugador:
    print("Empate")
elif (opcion_pc == "Piedra" and opcion_jugador == "Tijera") or (opcion_pc == "Tijera" and opcion_jugador == "Papel")\
        or (opcion_pc == "Papel" and opcion_jugador == "Piedra"):
    print("El ganador es: PC")
else:
    print("El ganador es: Jugador 1")


#OPCION B

# ELECCION JUGADOR
opcion_jugador= int(input("Introduzca una opción piedra= 1, papel= 2, tijera= 3: "))

if opcion_jugador == 1:
    eleccion_jugador="Piedra"
elif opcion_jugador== 2:
    eleccion_jugador="Papel"
elif opcion_jugador==3:
    eleccion_jugador="Tijera"
else:
    print("Incorrecto")


#ELECCION PC
opcion_pc = random.randrange(1, 4)

if opcion_pc == 1:
    eleccion_pc = "Piedra"
elif opcion_pc == 2:
    eleccion_jugador="Papel"
else:
    print("Tijera")

# GANADOR
if opcion_pc == opcion_jugador:
    print("Empate")
elif (opcion_pc == "Piedra" and opcion_jugador == "Tijera") or (opcion_pc == "Tijera" and opcion_jugador == "Papel")\
        or (opcion_pc == "Papel" and opcion_jugador == "Piedra"):
    print("El ganador es: PC")
else:
    print("El ganador es: Jugador 1")


