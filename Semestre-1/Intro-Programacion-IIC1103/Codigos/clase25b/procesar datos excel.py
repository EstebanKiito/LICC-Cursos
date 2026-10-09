archivo = open('datos.csv')
salida = open('puntajes_sobre75.csv','w')
lista = archivo.readlines()
lista.pop(0) #lista = lista[1:]
for elem in lista:#elem: '1;1;1;1;1;1;0,06;0;0\n'
    datos_estudiante = elem.strip().split(';')
    puntos_totales = 0
    for puntaje in datos_estudiante[1:]: #datos_estudiante[1:]: ['1', '1', '1', '1', '1', '0,06', '0', '0']
        puntos_float = float(puntaje)
        puntos_totales+=puntos_float
    if puntos_totales>=7.5:
        print(f'{datos_estudiante[0]};{round(puntos_totales,2)}',file=salida)

salida.close()