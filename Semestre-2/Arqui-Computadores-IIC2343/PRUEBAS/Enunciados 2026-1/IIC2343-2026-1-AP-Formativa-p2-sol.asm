.data
  arr:        .word 1, 3, 5, 7, -5
  len:        .word 5
  pair_sum:   .word 10
  x_pair_sum: .word -1
  y_pair_sum: .word -1
.text
  la s0, arr                        # Dirección inicial del arreglo.
  addi s1, zero, 4                  # Constante para multiplicar índices por 4 para obtener direcciones.
  lw s2, len		            # Largo del arreglo.
  addi s3, s2, -1                   # len - 1 para terminar antes el loop de i.
  lw s4, pair_sum                   # Suma a buscar.
  la s5, x_pair_sum                 # Dirección para almacenar el índice del primer número del par.
  la s6, y_pair_sum                 # Dirección para almacenar el índice del segundo número del par.
  addi t0, zero, 0                  # Índice i
  find_pair_sum:
    i_loop:                         # Iteración respecto al índice i
      addi t1, t0, 1                # j = i + 1, no vemos los elementos hacia atrás, ya se revisaron.
      j_loop:
        mul t2, t0, s1              # t2 = 4 * i
        mul t3, t1, s1              # t3 = 4 * j
        add t2, s0, t2              # t2 = dir(arr) + 4 * i
        add t3, s0, t3              # t3 = dir(arr) + 4 * j
        lw t2, 0(t2)                # t2 = arr[i]
        lw t3, 0(t3)                # t3 = arr[j]
        add t4, t2, t3              # t4 = arr[i] + arr[j]
        beq t4, s4, pair_sum_found  # arr[i] + arr[j] == pair_sum
      j_loop_continue:
        addi t1, t1, 1
        blt t1, s2, j_loop          # if j >= n, end j_loop
    i_loop_continue:
      addi t0, t0, 1
      bge t0, s3, end               # if i >= n - 1, end i_loop
      jal zero, i_loop
    pair_sum_found:
      sw t0, 0(s5)                  # x_pair_sum = i
      sw t1, 0(s6)                  # y_pair_sum = j
  end:
    addi a7, zero, 10
    ecall
