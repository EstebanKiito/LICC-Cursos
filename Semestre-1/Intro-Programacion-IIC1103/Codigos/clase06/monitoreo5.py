valor = int(input('Ingresar valor estacion: '))
if 0<=valor<=99:
    print('bueno')
elif 100<=valor<=199:
    print('regular')
elif 200<=valor<=299:
    print('alerta')
elif 300<=valor<=499:
    print('preemergencia')
elif valor>=500:
    print('emergencia')
else:
    print('fuera de rango')
print('fin')