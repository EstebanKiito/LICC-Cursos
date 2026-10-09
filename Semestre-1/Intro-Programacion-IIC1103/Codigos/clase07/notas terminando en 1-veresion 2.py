print('Ingresa notas, cuando ingreses -1 se termina el programa')
suma = 0
n = 0
while True: #seguir == True
    nota = float(input('nota? '))
    if nota==-1:
        break
    else:
        suma+=nota #suma = suma+nota
        n+=1
if n==0:
    print('No hay suficientes notas')
else:
    print(suma/n)

