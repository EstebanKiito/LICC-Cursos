##########################################
#### TEST 10: Evolve
##########################################
_start:
	la a0, bulbasaur
    addi t0, zero, 17
    sw t0, 8(a0)
	jal ra, evolve

    la a0, bulbasaur
    jal ra, _print_pokemon

_end:


###################################
## Resultados Esperados
########################
#    Ivysaur:    Felicitaciones, ha evolucionadoooo!
#
#    Ivysaur:  
#    ID: 2
#    Tipo: 0
#    Nivel: 17
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



