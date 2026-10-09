cuantas = int(input('cuantas notas vas a ingresar? '))
suma = 0
n = 0 #contador de notas
while n<cuantas:
    nota = float(input('nota? '))
    suma+=nota #suma = suma+nota
    n+=1
print(suma/cuantas)
