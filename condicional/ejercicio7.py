# Ejercicio: Juego de Piedra, Papel o Tijeras.

jugador1 = input("Jugador 1, elige: piedra papel o tijera: ")
jugador2 = input("Jugador 2, elige: piedra papel o tijera: ")

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == 'papel' and jugador2 == 'piedra') or (jugador1 == 'tijera' and jugador2 == 'papel') or (jugador1 == 'tijera' and jugador2 == 'piedra'):
    print(f'jugador1, gana con {jugador1} :v jugador 2, pierde con {jugador2}')
else:
    print(f'jugador2, gana con {jugador2} :v jugador 1, pierde con {jugador1}')


