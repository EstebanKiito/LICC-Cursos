
def eliminar_duplicados(lista):
    a_borrar = []
    for elem in lista:
        if lista.count(elem)>1 and elem not in a_borrar:
            a_borrar.append(elem)
    for elem in a_borrar:
        while elem in lista:
            lista.remove(elem)


lista = [1, 8, 1, 3, 8, 2, 4, 1, 3, 4, 5, 6, 3, 2, 4, 7, 4, 4, 4, 2, 3]
print(lista)
eliminar_duplicados(lista)
print(lista)