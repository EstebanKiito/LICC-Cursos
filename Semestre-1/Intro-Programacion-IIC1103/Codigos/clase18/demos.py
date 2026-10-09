def agregar(lista, x):
    for i in range(len(lista)):
        if lista[i]>x:
            lista.insert(i,x)
            return lista
    lista.append(x)
    return lista

lista = [5,10,25,70]
print(lista)
lista = agregar(lista,100)
print(lista)