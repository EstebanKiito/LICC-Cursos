# DEFINIR FUNCION

def segundos(hora):
    s = hora % 100
    m = (hora // 100) % 100
    h = hora // 10000
    return s+m*60+h*60*60

# CODIGO PRINCIPAL
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

totales_mayor = segundos(mayor_tiempo)

totales_menor = segundos(menor_tiempo)

print(f'Diferencia: {totales_mayor-totales_menor}')
