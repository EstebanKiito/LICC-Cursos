from functools import reduce
import os

class DCCAplicacion:
    # rellenar
    pass
    

clase = DCCAplicacion() # rellenar
clase.leer_archivo()
clase.arreglar_archivo()
clase.nombres_gasto()
clase.promedio_gasto()
generador_menor = clase.recorrer_especifico("menor")
generador_mayor = clase.recorrer_especifico("mayor")
for elemento in generador_menor:
    print(elemento)
for elemento in generador_mayor:
    print(elemento)
