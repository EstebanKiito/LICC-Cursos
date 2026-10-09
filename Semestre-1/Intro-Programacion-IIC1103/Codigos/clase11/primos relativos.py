def primosrelativos(x,y):
    for i in range(2,min(x,y)+1):
        if x%i==0 and y%i==0:
            return False
    return True


for i in range(2,20):
    for j in range(i+1,21):
        if primosrelativos(i,j):
            print(i,j,'son primos relativos')