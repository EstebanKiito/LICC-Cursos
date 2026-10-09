def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

#COD PPAL
n = int(input('n? '))
print(factorial(n))