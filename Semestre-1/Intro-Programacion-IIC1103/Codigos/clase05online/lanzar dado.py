import random

print('Voy a tirar un dado! ')
dado = random.randint(1,6)
usuario = int(input('Adivina cual numero me sale: '))
print(f'Salio un {dado}')
if dado == usuario: #si es que dado es igual a usuario
    print('Bien! Ganaste!!')
    print(':-)')
else: #si no
    print('Lo siento, perdiste')
print('FIN')
