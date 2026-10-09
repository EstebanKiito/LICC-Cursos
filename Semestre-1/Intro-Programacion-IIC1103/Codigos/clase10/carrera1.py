seguir = True
numero = 1
menor_tiempo = 240000
ganador = 0
while seguir:
    llegada = int(input(f'Hora de llegada #{numero}?'))
    if llegada == -1:
        seguir = False
    else:
        if llegada < menor_tiempo:
            menor_tiempo = llegada
            ganador = numero
        numero+=1
    print(llegada, menor_tiempo, ganador)

print(f'#{ganador}- tiempo:{menor_tiempo}')