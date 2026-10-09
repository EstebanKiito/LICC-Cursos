def ordenar(x,y,z):
    if x.lower()<y.lower()<z.lower():
        print(x+","+y+","+z)
    elif x<z<y:
        print(x+","+z+","+y)
    elif y<x<z:
        print(y+","+x+","+z)
    elif y<z<x:
        print(y+","+z+","+x)
    elif x<y: #z debe ser la menor
        print(z+","+x+","+y)
    else:
        print(z+","+y+","+x)

a = input()
b = input()
c = input()
ordenar(a.lower(),b.lower(),c.lower())