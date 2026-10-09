rut = int(input('RUT (sin puntos ni DV): '))
mult = 2
suma = 0
while not rut==0:
    ultimo = rut%10
    suma+= ultimo*mult
    #borrar ultimo digito
    rut = rut//10
    mult+=1
    if mult==8:
        mult=2

calculo = suma%11
dv = 11-calculo
if dv == 10:
    print('K')
elif dv == 11:
    print('0')
else:
    print(dv)