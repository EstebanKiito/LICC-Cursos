##########################################
#### TEST 13: Poison Damage
##########################################
_start:
	la a0, bulbasaur
    addi t0, zero, 1
    sw t0, 16(a0)
	jal ra, poison_damage

    la a0, bulbasaur
    jal ra, _print_pokemon

_end:

###################################
## Resultados Esperados
########################
#    Bulbasaur:  Ha perdido vida por envenenamiento
#
#    Bulbasaur:  
#    ID: 1
#    Tipo: 0
#    Nivel: 5
#    EXP: 0
#    Estado: 1
#    HP: 19
#    HP Total: 21
#    Ataque: 11
#    Defensa: 8
#    Ataque Especial: 13
#    Defensa Especial: 13
#    Velocidad: 11
###################################



