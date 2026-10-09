import random
def palabra():
    archivo = open('diccionario.txt',encoding='latin-1')
    lista = archivo.readlines()
    pos = random.randint(0,len(lista)-1)
    archivo.close()
    return lista[pos].strip()

for i in range(10):
    print(palabra())