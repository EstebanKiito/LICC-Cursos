def fibonacci(mes):
    if mes==1 or mes==2:
        return 1
    return fibonacci(mes-1)+fibonacci(mes-2)

for i in range(1,48):
    print(f'mes {i} => {fibonacci(i)}')