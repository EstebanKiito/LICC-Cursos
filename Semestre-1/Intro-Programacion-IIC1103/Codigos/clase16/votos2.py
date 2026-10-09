votos = []
seguir = True
while seguir:
    voto = int(input('Voto? '))
    if voto == -1:
        seguir = False
    else:
        votos.append(voto)

print(f'Votos emitidos {len(votos)}')
for i in range(1,10):
    print(f'#{i} = {votos.count(i)}')
