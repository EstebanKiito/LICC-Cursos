
cuantas = int(input('cuantas notas vas a ingresar? '))
suma = 0
n = 1 #contador de notas
while n<=cuantas:
    nota = float(input('nota? '))
    if nota>=1 and nota<=7: #1<=nota<=7
        suma+=nota #suma = suma+nota
        n+=1
    else:
        print('Ingresa una nota entre 1 y 7')
print(suma/cuantas)

