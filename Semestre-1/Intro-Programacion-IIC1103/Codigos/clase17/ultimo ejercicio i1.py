# Escribe tu código aquí

def contar(s,x): #CON Traslapes
    contador = 0
    for i in range(len(s)):
        if s[i:i+len(x)]==x:
            contador+=1
    return contador

def suenos_repetidos(loop):
    maslargo = ''
    for i in range(len(loop)):
        for k in range(2,len(loop)):
            trozo = loop[i:i+k]
            c = contar(loop,trozo)
            if c>=2 and len(trozo)>len(maslargo):
                maslargo = trozo
    return maslargo
