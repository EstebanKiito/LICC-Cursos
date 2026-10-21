##########################################
#### TEST 16: Wake Up!
#################
## Con esta tener ojo, el generador de numeros
## aleatorios no es muuuuy bueno por lo que se puede 
## demorar en que se cumpla la condicion.
##########################################
_start:
	la a0, bulbasaur
    addi t0, zero, 2
    sw t0, 16(a0)
	jal ra, wake_up

    la a0, bulbasaur
    jal ra, _print_pokemon

_end:

###################################
## Resultados Esperados
########################
## Si Bulbasaur despierta.
#############
#    Bulbasaur:  Ha despertado!
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
########################
########################
########################
########################
## Si Bulbasaur no despierta.
#############
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
###################################



