.data
arr: .word 3, 2, 1, 2, 4, 3
len: .word 6
res: .word -1
.text
init:
    lw s0, len                   # s0 = Largo arr
    addi s1, s0, -1              # s1 = Largo arr - 1
    la s2, res                   # s2 = Dir. memoria res
    la s3, arr                   # s3 = Dir. memoria arr[i]
    addi t0, zero, 0             # t0 = i = 0
    addi t1, zero, 1             # t1 = j = 1
    beq s1, zero, end_program    # if s1 == 0 -> len = 1, termina programa con máxima dist. = 0
    

loop:
    add t3, zero, t0             # t3 = i
    slli t3, t3, 2               # t3 = 4*i (2 shift lefts)
    add t3, t3, s3               # t3 = dir(arr) + 4*i = dir(arr[i])
    lw t3, 0(t3)                 # t3 = arr[i]

    continue_loop:
        add t4, zero, t1         # t4 = j
        slli t4, t4, 2           # t4 = 4*j (2 shift lefts)
        add t4, t4, s3           # t4 = dir(arr) + 4*j = dir(arr[j])
        lw t4, 0(t4)             # t4 = arr[j]
        bne t3, t4, next_j       # if t3 != t4 -> no gemelos, avanza j
        sub t5, t1, t0           # t5 = j - i -> distancia entre gemelos
        ble t5, t2, next_j       # if t5 <= t2 -> distancia <= a la máxima actual, avanza j
        add t2, zero, t5         # t2 = t5 -> nueva distancia máxima
    
    next_j:
        addi t1, t1, 1           # j += 1
        bge t1, s0, next_i       # if t1 >= s0 -> j >= len, avanza i y restituye j
        jal zero, continue_loop  # Reinicia loop manteniendo arr[i], ya que no cambia
    
    next_i:
        addi t0, t0, 1           # i += 1
        bge t0, s1, end_program  # if t0 >= s1 -> i >= len - 1, termina programa (último elemento)
        addi t1, t0, 1           # j = i + 1, solo vemos las combinaciones hacia adelante
        jal zero, loop           # Reinicia loop desde el comienzo
    
end_program:
    sw t2, 0(s2)                 # res = distancia máxima encontrada, o cero
    addi a7, zero, 10
    ecall
