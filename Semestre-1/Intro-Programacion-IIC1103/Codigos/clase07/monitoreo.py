# 200-299 alerta
# 300-499 preemergencia
# 500+ emergencia

e1 = int(input('Estacion 1: '))
e2 = int(input('Estacion 2: '))
e3 = int(input('Estacion 3: '))
if (e1>=500 and e2>=500) or (e2>=500 and e3>=500) or (e1>=500 and e3>=500):
    print('Emergencia')
elif (e1>=300 and e2>=300) or (e2>=300 and e3>=300) or (e1>=300 and e3>=300):
    print('Preemergencia')
elif (e1>=200 and e2>=200) or (e2>=200 and e3>=200) or (e1>=200 and e3>=200):
    print('Alerta')
else:
    print('No hay ninguna medida excepcional')
