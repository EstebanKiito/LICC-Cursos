# Escribe tu código aquí

nombre = input()
archivo = open('registro.txt','r')
lista = archivo.readlines()
for linea in lista: #linea: 'kaatt 455'
    datos = linea.strip().split()
    #datos[0]: nombre, datos[1]: puntaje
    if datos[0]==nombre:
        print(datos[1])

