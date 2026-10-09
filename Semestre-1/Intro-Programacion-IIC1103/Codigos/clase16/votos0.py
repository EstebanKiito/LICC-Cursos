voto1=0
voto2=0

seguir=True

while seguir:
    voto = int(input("Voto?"))
    if voto==-1:
        seguir = False
    elif voto==1:
        voto1+=1
    elif voto==2:
        voto2+=1
print("Votos emitidos="+str(voto1+voto2))
print("#1="+str(voto1))
print("#2="+str(voto2))
