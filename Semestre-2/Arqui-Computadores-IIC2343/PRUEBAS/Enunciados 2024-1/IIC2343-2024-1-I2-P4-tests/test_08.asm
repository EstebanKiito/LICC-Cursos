##########################################
#### TEST 8: Experience
##########################################
_start:
	la a0, bulbasaur
    addi t0, zero, 99
	sw t0, 12(a0)
    addi t0, zero, 10
	sw t0, 20(a0)

	jal ra, experience

    la a0, bulbasaur
    jal ra, _print_pokemon

_end:


###################################
## Resultados Esperados
########################
#    Bulbasaur:  Felicitaciones, ha subido de nivel!
#
#    Bulbasaur:  
#    ID: 1
#    Tipo: 0
#    Nivel: 6
#    EXP: 28
#    Estado: 0
#    HP: 13
#    HP Total: 24
#    Ataque: 12
#    Defensa: 9
#    Ataque Especial: 14
#    Defensa Especial: 14
#    Velocidad: 12
###################################



