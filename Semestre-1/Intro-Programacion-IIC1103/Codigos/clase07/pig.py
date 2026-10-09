import random
puntos1 = 0
puntos2 = 0
turno = 1
while puntos1<100 and puntos2<100:
    print(f'*** Turno jugador {turno}')
    #TURNO
    seguir = True
    while seguir:
        opcion = int(input('Lanzar? (1) si, (2) no'))
        if opcion == 2:
            seguir = False
        else:
            dado = random.randint(1,6)
            print(f'Tienes un {dado}')
            if dado == 1:
                seguir = False



    if turno == 1:
        turno=2
    else:
        turno=1