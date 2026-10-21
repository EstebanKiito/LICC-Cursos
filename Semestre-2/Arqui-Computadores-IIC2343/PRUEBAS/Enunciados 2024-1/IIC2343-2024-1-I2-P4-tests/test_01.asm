##########################################
#### TEST 1: Attack
##########################################
_start:
	la a0, bulbasaur
	la a1, charmander
	jal ra, attack

	la a0, bulbasaur
    jal ra, _print_pokemon
	la a0, charmander
    jal ra, _print_pokemon

_end:


###################################
## Resultados Esperados
########################
## Si Bulbasaur no tiene ataque critico.
#############
#    Bulbasaur:  
#    ID: 1
#    Tipo: 0
#    Nivel: 5
#    EXP: 0
#    Estado: 0
#    HP: 21
#    HP Total: 21
#    Ataque: 11
#    Defensa: 8
#    Ataque Especial: 13
#    Defensa Especial: 13
#    Velocidad: 11
#
#    Charmander: 
#    ID: 4
#    Tipo: 1
#    Nivel: 5
#    EXP: 0
#    Estado: 0
#    HP: 19
#    HP Total: 20
#    Ataque: 12
#    Defensa: 7
#    Ataque Especial: 10
#    Defensa Especial: 11
#    Velocidad: 13
########################
########################
########################
########################
## Si Bulbasaur tiene un ataque critico.
#############
#    Bulbasaur:  Ha hecho un ATAQUE CRITICO!
#
#    Bulbasaur:  
#    ID: 1
#    Tipo: 0
#    Nivel: 5
#    EXP: 0
#    Estado: 0
#    HP: 21
#    HP Total: 21
#    Ataque: 11
#    Defensa: 8
#    Ataque Especial: 13
#    Defensa Especial: 13
#    Velocidad: 11
#
#    Charmander: 
#    ID: 4
#    Tipo: 1
#    Nivel: 5
#    EXP: 0
#    Estado: 0
#    HP: 15
#    HP Total: 20
#    Ataque: 12
#    Defensa: 7
#    Ataque Especial: 10
#    Defensa Especial: 11
#    Velocidad: 13
###################################



