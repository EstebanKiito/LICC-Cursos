import random
puntos1 = 0
puntos2 = 0
turno = 1
while puntos1<100 and puntos2<100:
    print(f'*** Turno jugador {turno}')
    #TURNO
    seguir = True
    puntos_este_turno = 0
    while seguir:
        opcion = int(input('Lanzar? (1) si, (2) no: '))
        if opcion == 2:
            seguir = False
            if turno == 1:
                puntos1+=puntos_este_turno
            else:
                puntos2+=puntos_este_turno
        else:
            dado = random.randint(1,6)
            print(f'Tienes un {dado}')
            if dado == 1:
                seguir = False
            else:
                puntos_este_turno+=dado
    print(f'Puntos jugador 1: {puntos1}, jugador 2: {puntos2}')
    if turno == 1:
        turno=2
    else:
        turno=1

if puntos1>=100:
    print('FELICITACIONES JUGADOR 1')
else:
    print('FELICITACIONES JUGADOR 2')