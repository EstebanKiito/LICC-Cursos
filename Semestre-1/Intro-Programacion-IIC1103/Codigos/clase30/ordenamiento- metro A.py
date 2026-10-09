
def criterio(item):
    return item[0]

def estaciones_comunes(metro):
    resultados = []
    nombres_estaciones_comunes = []
    for i in range(len(metro)): #linea: ['nombre_linea',['e1','e2',...]]
        linea = metro[i]
        for estacion in linea[1]: #estacion: 'Vespucio Norte'
            lista_lineas = [linea[0]]
            for j in range(i+1,len(metro)):
                lineaj = metro[j]  #lineaj: ['nombre_linea',['e1','e2',...]]
                if estacion in lineaj[1]:
                    lista_lineas.append(lineaj[0])
            if estacion not in nombres_estaciones_comunes and len(lista_lineas)>1:
                resultados.append([estacion,lista_lineas])
                nombres_estaciones_comunes.append(estacion)

    resultados.sort(key=criterio)
    return resultados