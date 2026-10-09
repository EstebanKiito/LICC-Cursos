arbol = [
    ["Abraham",[1,2]], #0
    ["Herb",[]], #1
    ["Homero",[3,4,5]], #2
    ["Bart",[]], #3
    ["Maggie",[]], #4
    ["Lisa",[]], #5
    ["Marge",[3,4,5]], #6
    ["Mona",[1,2]], #7
    ["Clancy",[6,10,11]], #8
    ["Jackie",[6,10,11]], #9
    ["Selma",[12]], #10
    ["Patty",[]], #11
    ["Ling",[]] #12
    ]

print(hijos(arbol,"Marge"))
print(hijos(arbol,"Abraham"))
print(hijos(arbol,"Herb"))

print(padres(arbol,"Maggie"))
print(padres(arbol,"Homero"))
print(padres(arbol,"Abraham"))
print(padres(arbol,"Ling"))