archivo = open('traducciones.txt','a')
seguir = True
while seguir:
    palabra = input('palabra? ')
    if palabra == 'fin':
        seguir = False
    else:
        traduccion = input('traduccion? ')
        #nos interesa guardar palabra&traduccion
        print(palabra+'&'+traduccion,file=archivo)

archivo.close()