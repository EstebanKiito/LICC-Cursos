valor = int(input('Ingresar valor estacion: '))
if 0<=valor<=99:
    print('bueno')
else:
    if 100<=valor<=199:
        print('regular')
    else:
        if 200<=valor<=299:
            print('alerta')
        else:
            if 300<=valor<=499:
                print('preemergencia')
            else:
                if valor>=500:
                    print('emergencia')
                else:
                    print('fuera de rango')
