def factorial(n):
    producto = 1
    for i in range(1,n+1):
        producto*=i #producto = producto*i
    return producto

x = int(input('Cuantos factoriales quieres calcular? '))
for i in range(1,x+1):
    valor = factorial(i)
    print(f'factorial({i}) = {valor}')