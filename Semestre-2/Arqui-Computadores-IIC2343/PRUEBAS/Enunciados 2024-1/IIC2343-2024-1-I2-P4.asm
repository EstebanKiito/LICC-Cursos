
.global _main

.data 

pelea: .word 0
pelea_text: .string "\n\nPelea "
turno: .word 0
turno_text: .string "\nTurno "

bulbasaur:
	.word	1	# ID
		0	# Tipo 		0: Planta	1: Fuego	2: Agua
		5	# Nivel
		0	# Exp
		0	# Estado
		21	# HP
		21	# HP Total
		11	# Ataque
		8	# Defensa
		13	# Ataque Especial
		13	# Defensa Especial
		11	# Velocidad
	
charmander:
	.word	4	# ID
		1	# Tipo
		5	# Nivel
		0	# Exp
		0	# Estado
		20	# HP
		20	# HP Total
		12	# Ataque
		7	# Defensa
		10	# Ataque Especial
		11	# Defensa Especial
		13	# Velocidad

squirtle:
	.word	7	# ID
		2	# Tipo
		5	# Nivel
		0	# Exp
		0	# Estado
		20	# HP
		20	# HP Total
		11	# Ataque
		10	# Defensa
		11	# Ataque Especial
		12	# Defensa Especial
		10	# Velocidad
	
evolutions: 
	.word	1, 2, 16	# (Bulbasaur, Ivysaur, nivel 16)
		2, 3, 32	# (Ivysaur, Venusaur, nivel 32)
		4, 5, 16	# (Charmander, Charmeleon, nivel 16)
		5, 6, 36 	# (Charmeleon, Charizard, nivel 36)
		7, 8, 16	# (Squirtle, Wartortle, nivel 16)
		8, 9, 36	# (Wartortle, Blastoise, nivel 36)
	
level_up_text: .string "Felicitaciones, ha subido de nivel!"
evolve_text: .string "Felicitaciones, ha evolucionadoooo!"
poisoning_text: .string "Oh no!! Ha sido envenenado"
poison_text: .string "Ha perdido vida por envenenamiento"
sleep_text: .string "Oh no!! Se ha quedado dormido"
wake_up_text: .string "Ha despertado!"
fainted_text: .string "No le queda energia para seguir peleando :("
critical_text: .string "Ha hecho un ATAQUE CRITICO!"
names: .string 			"\nBulbasaur:  "
				"\nIvysaur:    "
				"\nVenusaur:   "
				"\nCharmander: "
				"\nCharmeleon: "
				"\nCharizard:  "
				"\nSquirtle:   "
				"\nWartortle:  "
				"\nBlastoise:  "

.text

_main:
beq zero, zero, _start

_print_number:
	addi a7, zero, 1
	ecall
	jalr zero, 0(ra)

_print_string:
	addi a7, zero, 4
	ecall
	jalr zero, 0(ra)

_print_combat:
	addi sp, sp, -4
	sw ra, 0(sp)
	
	la a0, pelea_text
	jal ra, _print_string

	la t0, pelea
	lw a0, 0(t0)
	addi a0, a0, 1
	sw a0, 0(t0)

	jal ra, _print_number

	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)
	
_print_turn:
	addi sp, sp, -4
	sw ra, 0(sp)
	
	la a0, turno_text
	jal ra, _print_string

	la t0, turno
	lw a0, 0(t0)
	addi a0, a0, 1
	sw a0, 0(t0)

	jal ra, _print_number

	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)
	
_print_pokemon_name:
	lw t0, 0(a0)
	addi t1, zero, 14
	mul t0, t0, t1
	addi t0, t0, -14
	la a0, names
	add a0, t0, a0
	addi a7, zero, 4
	ecall
	jalr zero, 0(ra)

_print_poison_text:
	addi sp, sp, -4
	sw ra, 0(sp)
	jal ra, _print_pokemon_name
	la a0, poison_text
	jal ra, _print_string
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_print_wake_up_text:
	addi sp, sp, -4
	sw ra, 0(sp)
	jal ra, _print_pokemon_name
	la a0, wake_up_text
	jal ra, _print_string
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_print_evolve_text:
	addi sp, sp, -4
	sw ra, 0(sp)
	jal ra, _print_pokemon_name
	la a0, evolve_text
	jal ra, _print_string
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_print_critical_text:
	addi sp, sp, -4
	sw ra, 0(sp)
	jal ra, _print_pokemon_name
	la a0, critical_text
	jal ra, _print_string
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_rand_number:		# a0 rango del numero random. numero = [0, a0]
	addi a7, zero, 42
	add a1, zero, a0
	addi a0, zero, 0
	ecall
	jalr zero, 0(ra)

_critical_damage: # 10% de dano critico
	addi sp, sp, -8
	sw ra, 0(sp)
	sw a0, 4(sp)
	addi a0, zero, 10
	jal ra, _rand_number
	addi t0, zero, 1
	beq a0, t0, _critical_damage_print
	add a0, zero, zero
	beq zero, zero, retornar_critico
	_critical_damage_print:
	lw a0, 4(sp)
	jal ra, _print_critical_text
	addi a0, zero, 1
	retornar_critico:
	lw ra, 0(sp)
	addi sp, sp, 8
	jalr zero, 0(ra)

_type_boost:
	lw t0, 4(a0)	# tipo 1
	lw t1, 4(a1)	# tipo 2
	addi t2, t0, 1	# t2 = tipo 1 + 1
	addi t3, zero, 3	# t3 = 3
	rem t2, t2, t3	# t2 =  (tipo 1 + 1) mod 3		
	beq t2, t1, ataque_no_favorable
	addi t2, t0, 2	# t2 = tipo 1 + 2
	rem t2, t2, t3	# t2 =  (tipo 1 + 1) mod 3		
	beq t2, t1, ataque_favorable
	ataque_neutro:
		add a0, zero, zero
		jalr zero, 0(ra)
	ataque_favorable:
		addi a0, zero, 3
		jalr zero, 0(ra)
	ataque_no_favorable:
		addi a0, zero, -3
		jalr zero, 0(ra)

_faint:
	addi sp, sp, -4
	sw ra, 0(sp)
	addi t0, zero, 3
	sw t0, 16(a0)
	jal ra, _print_pokemon_name
	la a0, fainted_text
	jal ra, _print_string
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_heal:
	lw t0, 24(a0)
	sw t0, 20(a0)
	sw zero, 16(a0)
	jalr zero, 0(ra)

_heal_all:
	addi sp, sp, -4
	sw ra, 0(sp)
	la a0, bulbasaur
	jal ra, _heal
	la a0, charmander
	jal ra, _heal
	la a0, squirtle
	jal ra, _heal
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_poison_pokemon:
	addi t0, zero, 1
	sw t0, 16(a0)
	addi sp, sp, -4
	sw ra, 0(sp)
	jal ra, _print_pokemon_name
	la a0, poisoning_text
	jal ra, _print_string
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_sleep_pokemon:
	addi t0, zero, 2
	sw t0, 16(a0)
	addi sp, sp, -4
	sw ra, 0(sp)
	jal ra, _print_pokemon_name
	la a0, sleep_text
	jal ra, _print_string
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, 0(ra)

_turn:
	addi sp, sp, -16
	sw ra, 0(sp)
	sw a0, 4(sp)
	sw a1, 8(sp)
	sw s0, 12(sp)
	jal ra, _print_turn
	lw a0, 4(sp)

	# Se comienza el turno de ataque
	jal ra, turn_attack

	# Se verifica si algun pokemon se ha desmayado
	lw a0, 4(sp)
	lw a1, 8(sp)
	lw t0, 20(a1)
	beq t0, zero, sumar_experiencia
	lw a0, 8(sp)
	lw a1, 4(sp)
	lw t0, 20(a1)
	beq t0, zero, sumar_experiencia
	beq zero, zero, seguir_turno

	sumar_experiencia:
	jal ra, experience
	beq zero, zero, retornar_turno

	seguir_turno:
	# Se resta HP a los pokemones envenenados
	lw a0, 4(sp)
	jal ra, poison_damage
	lw a0, 8(sp)
	jal ra, poison_damage

	# Se verifica si algun pokemon se ha desmayado despues del envenenamiento
	lw a0, 4(sp)
	lw a1, 8(sp)
	lw t0, 20(a1)
	beq t0, zero, sumar_experiencia
	lw a0, 8(sp)
	lw a1, 4(sp)
	lw t0, 20(a1)
	beq t0, zero, sumar_experiencia

	# Se verifica si se despierta un pokemon
	lw a0, 4(sp)
	jal ra, wake_up
	lw a0, 8(sp)
	jal ra, wake_up

	# Se elige si se envenena o duerme algun pokemon
	lw a0, 4(sp)
	lw t0, 16(a0)
	bne t0, zero, comprobar_estado_siguiente

	addi a0, zero, 10
	jal ra, _rand_number
	add s0, zero, a0

	lw a0, 4(sp)
	addi t1, zero, 1
	bne s0, t1, _seguir_dormir_pokemon1
	jal ra, _poison_pokemon
	beq zero, zero, comprobar_estado_siguiente
	
	_seguir_dormir_pokemon1:
	addi t1, zero, 2
	bne s0, t1, comprobar_estado_siguiente
	jal ra, _sleep_pokemon

	comprobar_estado_siguiente:
	lw a0, 8(sp)
	lw t0, 16(a0)
	bne t0, zero, retornar_turno

	addi a0, zero, 10
	jal ra, _rand_number
	add s0, zero, a0

	lw a0, 8(sp)
	addi t1, zero, 1
	bne s0, t1, _seguir_dormir_pokemon2
	jal ra, _poison_pokemon
	beq zero, zero, retornar_turno
	
	_seguir_dormir_pokemon2:
	addi t1, zero, 2
	bne s0, t1, retornar_turno
	jal ra, _sleep_pokemon

	retornar_turno:
	lw a0, 4(sp)
	lw a1, 8(sp)
	lw s0, 12(sp)
	lw ra, 0(sp)
	addi sp, sp, 16
	jalr zero, 0(ra)

_combat:
	addi sp, sp, -12
	sw ra, 0(sp)
	sw a0, 4(sp)
	sw a1, 8(sp)
	jal ra, _print_combat
	la t0, turno
	sw zero, 0(t0)
	lw a0, 4(sp)
	loop_combat:
	jal ra, _turn
	lw a0, 4(sp)
	lw a1, 8(sp)
	lw t0, 20(a0)
	beq t0, zero, teminar_combate
	lw t0, 20(a1)
	beq t0, zero, teminar_combate
	beq zero, zero, loop_combat

	teminar_combate:
	lw a0, 4(sp)
	lw a1, 8(sp)
	lw ra, 0(sp)
	addi sp, sp, 12
	jalr zero, 0(ra)

_level_up:
	addi sp, sp, -8
	sw ra, 0(sp)
	sw a0, 4(sp)

	lw t0, 8(a0)	# Nivel del pokemon a0
	addi t0, t0, 1
	sw t0, 8(a0)	# Nivel del pokemon a0
	lw t0, 20(a0)	# HP del pokemon a0
	addi t0, t0, 3
	sw t0, 20(a0)	# Hp del pokemon a0
	lw t0, 24(a0)	# HP total del pokemon a0
	addi t0, t0, 3
	sw t0, 24(a0)	# Hp total del pokemon a0
	lw t0, 28(a0)	# Ataque del pokemon a0
	addi t0, t0, 1
	sw t0, 28(a0)	# Ataque del pokemon a0
	lw t0, 32(a0)	# Defensa del pokemon a0
	addi t0, t0, 1
	sw t0, 32(a0)	# Defensa del pokemon a0
	lw t0, 36(a0)	# Ataque Especial del pokemon a0
	addi t0, t0, 1
	sw t0, 36(a0)	# Ataque Especial del pokemon a0
	lw t0, 40(a0)	# Defensa Especial del pokemon a0
	addi t0, t0, 1
	sw t0, 40(a0)	# Defensa Especial del pokemon a0
	lw t0, 44(a0)	# Velocidad del pokemon a0
	addi t0, t0, 1
	sw t0, 44(a0)	# Velocidad del pokemon a0

	jal ra, _print_pokemon_name
	la a0, level_up_text
	jal ra, _print_string

	lw a0, 4(sp)
	jal ra, evolve

	lw ra, 0(sp)
	addi sp, sp, 8
	jalr zero, 0(ra)

attack: # a0 tiene la direccion del primer pokemon, a1 el segundo
	jalr zero, 0(ra)

turn_attack:
	jalr zero, 0(ra)

experience:
	jalr zero, 0(ra)

evolve:
	jalr zero, 0(ra)

poison_damage:
	jalr zero, 0(ra)

wake_up:
	jalr zero, 0(ra)


_start:
	la a0, bulbasaur
	la a1, charmander
	jal ra, _combat
	jal ra, _heal_all

	la a0, bulbasaur
	la a1, squirtle
	jal ra, _combat
	jal ra, _heal_all

	la a0, charmander
	la a1, squirtle
	jal ra, _combat
	jal ra, _heal_all
	
	#####################################################
	## Terminamos si algun pokemon llega a nivel 40
	#####################################################
	addi t1, zero, 40
	la a0, bulbasaur
	lw t0, 8(a0)
	bge t0, t1, _end

	la a0, charmander
	lw t0, 8(a0)
	bge t0, t1, _end

	la a0, squirtle
	lw t0, 8(a0)
	bge t0, t1, _end

	beq zero, zero, _start

_end:

