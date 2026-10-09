#0-99 bueno, 100-199 regular, otro: fuera de rango
valor = int(input('Ingresar valor estacion: '))
if 0<=valor<=99:
    print('bueno')
else:
    if 199>=valor>=100:
        print('regular')
    else:
        print('fuera de rango')
print('fin')