##########################################
#### TEST 4: Attack
##########################################
_start:
	la a0, bulbasaur
	addi t0, zero, 2
	sw t0, 16(a0)
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
#    Bulbasaur:  
#    ID: 1
#    Tipo: 0
#    Nivel: 5
#    EXP: 0
#    Estado: 2
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
#    HP: 20
#    HP Total: 20
#    Ataque: 12
#    Defensa: 7
#    Ataque Especial: 10
#    Defensa Especial: 11
#    Velocidad: 13
###################################



