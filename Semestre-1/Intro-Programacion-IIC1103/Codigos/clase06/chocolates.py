chocolates = int(input('Cuantos chocolates hay? '))
personas = int(input('Cuantas personas hay? '))
if chocolates<personas:
    print('ADVERTENCIA: no hay suficientes chocolates')

print(f'Repartir {chocolates//personas}, sobran {chocolates%personas}')
