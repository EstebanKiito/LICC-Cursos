cuantos = int(input('Cuantos candidatos? '))
votos =  [0]*cuantos

seguir=True

while seguir:
    voto = int(input("Voto?"))
    if voto==-1:
        seguir = False
    votos[voto-1]+=1
    print(votos)
print("#votos emitidos=",sum(votos))
for i in range(len(votos)):
    print(f"Candidato {i+1} = {votos[i]}")