def factorialp(n):
    producto = 1
    for i in range(1,n+1):
        producto*=i #producto = producto*i
    print(producto)

x = int(input('Cuantos factoriales quieres calcular? '))
for i in range(1,x+1):
    print(i,end=" = ")
    factorialp(i)