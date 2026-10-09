lista = [ ['Inigo','inigo@gmail.com','03/10'], ['Lucy','lucy@gmail.com','10/06'], ['Ada','ada@gmail.com','18/09']]
#Cuantos amigos cumplen años entre el mes 7 y el mes 12?
for elem in lista: #ej: elem = ['Inigo','inigo@gmail.com','03/10']
    cumple = elem[2]
    mes = int(cumple[3:])
    #mes = elem[2][3:]
    if mes>=7:
        print(elem[0])