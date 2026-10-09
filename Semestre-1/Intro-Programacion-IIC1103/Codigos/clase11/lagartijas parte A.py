from lagartijas import *

def numero_lagartijas():
    # Rellenar
    i = 0
    seguir = True
    while seguir:
        if existe_lagartija(i) == False: #if not existe_lagartija(i)
            print(i)
            return
        i+=1

