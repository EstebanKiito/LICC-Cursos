#0-99 bueno, 100-199 regular, otro: fuera de rango
valor = int(input('Ingresar valor estacion: '))
if valor<0 or valor>199:
    print('fuera de rango')
else:
    if valor<=99:
        print('bueno')
    else:
        print('regular')
print('fin')


