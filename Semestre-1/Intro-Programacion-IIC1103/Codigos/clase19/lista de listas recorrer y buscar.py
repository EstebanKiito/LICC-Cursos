L = [[2,5,7],[1,4,6],[8,0,3],[9,5,10]]
for lista in L:
    t=''
    for elem in lista:
        t+=str(elem)+' '
    print(t.strip())

for i in range(len(L)):
    for j in range(len(L[0])):
        print(L[i][j],end=' ')
    print()

#Encontrar 5

for i in range(len(L)):
    for j in range(len(L[0])):
        if L[i][j]==5:
            print(i,j)
print(L.count([9,5,10]))