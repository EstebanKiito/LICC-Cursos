seguir = True
numero = 1
menor_tiempo = 240000
ganador = 0
mayor_tiempo = 0
while seguir:
    llegada = int(input(f'Hora de llegada #{numero}?'))
    if llegada == -1:
        seguir = False
    else:
        if llegada < menor_tiempo:
            menor_tiempo = llegada
            ganador = numero
        if llegada > mayor_tiempo:
            mayor_tiempo = llegada

        numero+=1
    print(llegada, menor_tiempo, mayor_tiempo, ganador)

print(f'#{ganador}- tiempo:{menor_tiempo} - mayor tiempo:{mayor_tiempo}')

segundos_mayor = mayor_tiempo%100
minutos_mayor = (mayor_tiempo//100)%100
horas_mayor = mayor_tiempo//10000
totales_mayor = segundos_mayor+minutos_mayor*60+horas_mayor*60*60

segundos_menor = menor_tiempo%100
minutos_menor = (menor_tiempo//100)%100
horas_menor = menor_tiempo//10000
totales_menor = segundos_menor+minutos_menor*60+horas_menor*60*60

print(f'Diferencia: {totales_mayor-totales_menor}')
