##########################################
#### TEST 12: Poison Damage
##########################################
_start:
	la a0, bulbasaur
	jal ra, poison_damage

    la a0, bulbasaur
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
#    Estado: 0
#    HP: 21
#    HP Total: 21
#    Ataque: 11
#    Defensa: 8
#    Ataque Especial: 13
#    Defensa Especial: 13
#    Velocidad: 11
###################################



