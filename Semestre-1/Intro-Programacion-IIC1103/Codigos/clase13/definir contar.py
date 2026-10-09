def contar(x,y): #cuenta cuantas veces está y en x
    contador = 0
    for letra in x:
        if letra == y:
            contador+=1
    return contador
def contar2(x,y): #cuenta cuantas veces está y en x
    contador = 0
    for i in range(len(x)):
        if x[i] == y:
            contador+=1
    return contador

n1 = contar('abracadabra','a')
print('a = ',n1)

n2 = contar('abracadabra','e')
print('e = ',n2)

n3 = contar('abracadabra','c')
print('c = ',n3)