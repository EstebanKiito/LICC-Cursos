n = int(input('n? '))
primos = []
criba = list(range(2,n+1))

while criba!=[]: #len(criba)>0
    m = min(criba)
    for i in range(m,n+1,m):
        if i in criba:
            criba.remove(i)
    primos.append(m)

print(f'primos = {primos}')



