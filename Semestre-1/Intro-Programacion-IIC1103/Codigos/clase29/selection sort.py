def ordenar1(lista):
    for ip in range(0,len(lista)):
        valor = min(lista[ip:])
        m = lista[ip:].index(valor)+ip
        lista[ip],lista[m] = lista[m],lista[ip]
def ordenar(lista):
    for ip in range(0,len(lista)):
        m = ip
        for i in range(ip+1,len(lista)):
            if lista[i] < lista[m]:
                m = i
        lista[ip],lista[m] = lista[m],lista[ip]

lista = [45, 12, 10, 45, 33, 45, 12, 9]
print(lista)
ordenar1(lista)
print(lista)