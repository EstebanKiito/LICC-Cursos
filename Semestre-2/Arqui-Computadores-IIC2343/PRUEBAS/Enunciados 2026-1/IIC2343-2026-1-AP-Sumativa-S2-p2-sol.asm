.data
arr: .word 1, 1, 1, 2, 2, 5
len: .word 6
res: .word -1
.text
init:
    lw s0, len                   # s0 = Largo arr
    la s1, res                   # s1 = Dir. memoria res
    la t0, arr                   # t0 = Dir. memoria arr[i]
    addi t1, zero, 0             # t1 = i = 0
    lw t3, arr                   # t3 = valor bloque actual
    addi t4, zero, 0             # t4 = peso bloque actual
    lw t5, res                   # t5 = peso máximo actual

loop:    
    lw t2, 0(t0)                 # t2 = arr[i], bloque actual
    beq t2, t3, inc_weight       # if t2 == t3 -> mismo bloque, aumenta peso
    ble t4, t5, next_block       # if t4 <= t5 -> bloque actual no pesa más, sigue al siguiente
    add t5, zero, t4             # t5 = nuevo peso máximo

    next_block:
        add t3, zero, t2         # t3 = nuevo valor bloque actual
        add t4, zero, t3         # t4 = peso inicial nuevo bloque
        jal zero, next_iter      # Siguiente iteración

    inc_weight:
        add t4, t4, t3           # t4 += peso bloque actual

    next_iter:
        addi t1, t1, 1           # t1 += 1 -> i += 1
        bge t1, s0, end_loop     # if i > len, salta a end_loop
        addi t0, t0, 4           # t0 += 4 -> dir. sgte. elemento
        jal zero, loop           # Reinicia loop
    
    end_loop:
        ble t4, t5, end_program  # if t4 <= t5 -> bloque actual no pesa más, termina el programa
        add t5, zero, t4         # t5 = nuevo peso máximo y termina
    
end_program:
    sw t5, 0(s1)                 # res = peso máximo encontrado
    addi a7, zero, 10
    ecall
