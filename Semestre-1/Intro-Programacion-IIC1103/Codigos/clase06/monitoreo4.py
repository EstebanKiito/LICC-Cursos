valor = int(input('Ingresar valor estacion: '))
if 0<=valor<=99:
    print('bueno')

if 100<=valor<=199:
    print('regular')

if 200<=valor<=299:
    print('alerta')

if 300<=valor<=499:
    print('preemergencia')

if valor>=500:
    print('emergencia')

if valor<0:
    print('fuera de rango')
