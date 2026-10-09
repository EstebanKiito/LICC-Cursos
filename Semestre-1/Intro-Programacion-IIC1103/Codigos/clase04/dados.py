
import random
dado = random.randint(1,6)
print('Voy a tirar un dado')
usuario = int(input('Adivina cual numero me sale? '))
print(f'Me salio un {dado}')
print(f'Adivinaste: {dado==usuario}')