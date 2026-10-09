
import random
print('Juguemos cachipun!')
computador = random.randint(1,3)
usuario = int(input('Elige: (1) Piedra, (2) Papel, (3) Tijeras: '))

resultado = (usuario==1 and computador==3) or (usuario == 2 and computador == 1) or (usuario==3 and computador==2)
print(f'Yo juego: {computador}')
print(f'Ganaste: {resultado}')
