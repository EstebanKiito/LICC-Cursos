##########################################
#### TEST 11: Evolve
##########################################
_start:
	la a0, bulbasaur
    addi t0, zero, 3
    sw t0, 0(a0)
    addi t0, zero, 60
    sw t0, 8(a0)
	jal ra, evolve

    la a0, bulbasaur
    jal ra, _print_pokemon

_end:


###################################
## Resultados Esperados
########################
#    Venusaur:  
#    ID: 3
#    Tipo: 0
#    Nivel: 60
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



