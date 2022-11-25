from random import choice, sample, shuffle 
import random
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

print("")
print(f"Las cartas y sus puntos son: {cartas}.\n" )         #Se enseñan las cartas y su puntuación.


lista_cartas = list(cartas)                             
carta = choice(lista_cartas)                            #Se elige aleatoriamente las dos cartas del jugador
carta2 = choice(lista_cartas)
puntos = cartas[carta]                                  #Determinamos las puntuaciones de las dos cartas por separado del jugador
puntos2 = cartas[carta2]
puntosjugador = puntos + puntos2

print(f"Tus cartas son {carta} con valor {puntos} y {carta2} con valor {puntos2}. Tus cartas suman {puntos + puntos2}.\n")

cartan1mesa = choice(lista_cartas)
cartan2mesa = choice(lista_cartas)
print("Carta numero 1: ", cartan1mesa)
print("Carta numero 2: ", cartan2mesa)
cartas_mesa = [cartan1mesa, cartan2mesa]
print("Cartas de la mesa: ", cartas_mesa)
valor_cartas_mesa = cartas[cartan1mesa] + cartas[cartan2mesa]
print("Valor de las cartas de la mesa: ", valor_cartas_mesa)
if puntosjugador>valor_cartas_mesa<21:
    print("Has ganado")
elif puntosjugador<valor_cartas_mesa<21:
    print("Has perdido")
elif puntosjugador==valor_cartas_mesa:
    print("Empate") 