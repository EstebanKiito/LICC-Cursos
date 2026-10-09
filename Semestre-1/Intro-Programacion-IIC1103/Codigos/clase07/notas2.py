
cuantas = int(input('cuantas notas vas a ingresar? '))
suma = 0
for n in range(cuantas):
    nota = float(input('nota? '))
    suma+=nota #suma = suma+nota
print(suma/cuantas)

