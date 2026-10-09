def criterio1(item):#item:str
    return item.lower()
def criterio2(item):#item:lista de dos elementos
    return sum(item)
def criterio3(item): #lista de strings
    return item[1]

lista = ["casa", "arbol", "ELEFANTE", "feria", "automovil", "libro", "DelFiN", "dinoSAURIO"]
print(lista)
lista.sort(key=criterio1)
print(lista)

lista = [[4,4],[0,1],[1,2],[1,6],[0,3],[9,0],[3,4],[2,5]]
print(lista)
lista.sort(key=criterio2)
print(lista)

lista= [["cat","gato","gatto","Katze","neko","chat"],
        ["house","casa","casa","Haus","taku","maison"],
        ["roof","tejado","tetto","Dach","yane","toit"],
        ["tree","arbol","albero","Baum","ki","arbre"],
        ["umbrella","paraguas","ombrello","Schirm","kasa","parapluie"]]
print(lista)
lista.sort(key=criterio3)
for e in lista:
    print(e)