mayor = ''
seguir = True
while seguir:
    palabra = input('palabra? ')
    if palabra == 'fin' or palabra == 'FIN':
        seguir = False
    elif len(palabra) > len(mayor):
        mayor = palabra
print('palabra mas larga',mayor)
