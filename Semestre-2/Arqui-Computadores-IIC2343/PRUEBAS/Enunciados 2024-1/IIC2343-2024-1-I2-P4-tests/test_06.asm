##########################################
#### TEST 6: Turn_Attack
##########################################
_start:
	la a0, bulbasaur
	la a1, charmander

	addi t0, zero, 1
	sw t0, 20(a0)
	sw t0, 20(a1)

	jal ra, turn_attack

    la a0, bulbasaur
    jal ra, _print_pokemon
	la a0, charmander
    jal ra, _print_pokemon

_end:

###################################
## Resultados Esperados
########################
## Si Charmander no tiene ataque critico.
#############
# 	 Bulbasaur:  No le queda energia para seguir peleando :(
#
#    Bulbasaur:  
#    ID: 1
#    Tipo: 0
#    Nivel: 5
#    EXP: 0
#    Estado: 3
#    HP: 0
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
#    HP: 1
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
## Si Charmander tiene un ataque critico.
#############
#    Charmander:  Ha hecho un ATAQUE CRITICO!
# 	 Bulbasaur:  No le queda energia para seguir peleando :(
#
#    Bulbasaur:  
#    ID: 1
#    Tipo: 0
#    Nivel: 5
#    EXP: 0
#    Estado: 3
#    HP: 0
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
#    HP: 1
#    HP Total: 20
#    Ataque: 12
#    Defensa: 7
#    Ataque Especial: 10
#    Defensa Especial: 11
#    Velocidad: 13
###################################



