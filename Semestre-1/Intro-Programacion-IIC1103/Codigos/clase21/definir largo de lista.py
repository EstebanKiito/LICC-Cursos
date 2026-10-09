def largo(lista):
    if lista == []:
        return 0
    return largo(lista[1:])+1

print(largo([1,2,3,4,6,7]))