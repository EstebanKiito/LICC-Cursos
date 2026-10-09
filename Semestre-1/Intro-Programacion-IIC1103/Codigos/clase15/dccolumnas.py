# Escribe tu código aquí

turno = 1
j1par = 0
j1impar = 0
j2par = 0
j2impar = 0

while j1par < 6 and j1impar < 6 and j2par < 6 and j2impar < 6:
    print(f'TURNO DEL JUGADOR {turno}')
    if turno == 1:
        print(f'FICHA PAR: {j1par} , FICHA IMPAR: {j1impar}')
    else:
        print(f'FICHA PAR: {j2par} , FICHA IMPAR: {j2impar}')
    dado = int(input())
    print(f'EL JUGADOR {turno} HA LANZADO {dado}')
    cicloturno = True
    avance = 0
    while cicloturno:
        opcion = input()  # SEGUIR o PLANTARSE
        if opcion == 'PLANTARSE':
            print(f'EL JUGADOR {turno} DECIDE PLANTARSE')
            cicloturno = False
        else:
            print(f'EL JUGADOR {turno} DECIDE SEGUIR')
            dadoturno = int(input())
            print(f'EL JUGADOR {turno} HA LANZADO {dadoturno}')
            if dadoturno % 2 != dado % 2:
                cicloturno = False
                avance = 0
            else:
                avance += 1
                if turno == 1:
                    if (dado % 2 == 0 and j1par + avance == 6) or (dado % 2 != 0 and j1impar + avance == 6):
                        cicloturno = False
                else:
                    if (dado % 2 == 0 and j2par + avance == 6) or (dado % 2 != 0 and j2impar + avance == 6):
                        cicloturno = False

    if turno == 1:
        if dado % 2 == 0:
            j1par += avance
        else:
            j1impar += avance
    else:
        if dado % 2 == 0:
            j2par += avance
        else:
            j2impar += avance

    if turno == 1:
        turno = 2
    else:
        turno = 1

if j1par == 6 or j1impar == 6:
    print('HA GANADO EL JUGADOR 1')
else:
    print('HA GANADO EL JUGADOR 2')