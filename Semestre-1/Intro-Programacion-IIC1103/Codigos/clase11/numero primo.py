def primo(num):
    for i in range(2,num//2+2):
        if num%i==0:
            return False
    return True

for i in range(3,100):
    if primo(i):
        print(i)
