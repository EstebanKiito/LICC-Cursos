valor = int(input('Ingresar valor estacion: '))
if valor>=500:
    print('emergencia')
elif valor>=300:
    print('preemergencia')
elif valor>=200:
    print('alerta')
elif valor>=100:
    print('regular')
elif valor>=0:
    print('bueno')
else:
    print('fuera de rango')