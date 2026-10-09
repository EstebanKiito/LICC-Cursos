# Escribe tu código aquí

import amigos

nombre = input()
print('Amigos de mi amigo:')
i = 1
seguir = True

while seguir:
    amigo = amigos.obtener_amigo(nombre,i)
    if amigo == '':
        seguir = False
    else:
        if amigos.estudia(amigo) == amigos.estudia(nombre):
            print(amigo)
    i+=1
