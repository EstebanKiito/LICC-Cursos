def vuelos_sin_vuelta(t):
    resultados = []
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j]==1 and t[j][i]==0:
                resultados.append([i,j])
    return resultados

def vuelos_con_una_escala(t):
    resultado = []
    for i in range(len(t)):
        resultado.append([0]*len(t))
    for i in range(len(t)):
        for j in range(len(t)):
            if i!=j:
                if t[i][j]==1:
                    resultado[i][j]=1
                else:
                    for k in range(len(t)):
                        if t[i][k]==1 and t[k][j]==1:
                            resultado[i][j]=1
    return resultado

def vuelos_con_escala(t):
    t2 = vuelos_con_una_escala(t)
    if t2 == t:
        return t2
    return vuelos_con_escala(vuelos_con_una_escala(t))

t = [[0,1,0,0],[1,0,0,0],[1,0,0,0],[0,0,1,0]]
r = vuelos_sin_vuelta(t)
print(r)

r2 = vuelos_con_una_escala(t)
print(r2)

r3 = vuelos_con_escala(t)
print(r3)