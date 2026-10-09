def criterio(item):
    return item[1]
archivo = open('catalan.txt','r')
lista_palabras = archivo.readlines()
contar = []
for palabra in lista_palabras:
    c = lista_palabras.count(palabra)
    if c>1 and [palabra.strip(),c] not in contar:
        contar.append([palabra.strip(),c])

contar.sort(key=criterio, reverse=True)
for elem in contar:
    print(elem[0],elem[1])