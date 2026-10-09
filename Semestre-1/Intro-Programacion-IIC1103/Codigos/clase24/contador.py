
s = input('Ingresa archivo a leer: ')
archivo = open(s)
lista = archivo.readlines()
print(len(lista))