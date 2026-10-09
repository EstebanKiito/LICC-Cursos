archivo1 = open('catalan.txt')
archivo2 = open('diccionario.txt')

catalan = archivo1.readlines()
diccionario = archivo2.readlines()

salida = open('castellano.txt','w')
for palabra in catalan: #palabra: 'cel\n'
    palabra2 = palabra.strip()
    for definicion in diccionario: #definicion: 'cel-cielo\n'
        lista = definicion.strip().split('-')
        pal_catalan = lista[0]
        pal_castellano = lista[1]

        if pal_catalan == palabra2:
            print(pal_castellano,file=salida)
salida.close()
archivo1.close()
archivo2.close()