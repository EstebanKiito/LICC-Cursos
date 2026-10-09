def buscar(x,y):
    for i in range(len(x)):
        print(x[i:i+len(y)])
        if y == x[i:i+len(y)]:
            return i
    return -1

print(buscar('abracadabra','caba'))
