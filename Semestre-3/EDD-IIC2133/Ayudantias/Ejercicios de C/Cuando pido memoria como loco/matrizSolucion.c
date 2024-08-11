#include <stdio.h>
#include <stdlib.h>
// Solución

/*
Este código crea una matriz en donde cada celda contiene justamente
un struct llamado Celda, donde sus atributos son los enteros x, y. 
Luego, asigna valores a cada celda de la matriz y los imprime en la 
consola. Finalmente, libera la memoria asignada para la matriz y sus 
filas.  

Para compilar:
gcc matrizSolucion.c -o matrizSolucion

Para ejecutar:
./matrizSolucion

*/

// Definición del struct Celda, que contiene dos enteros, x e y.
typedef struct celda_t {
    int x;
    int y;
} Celda;

int main(int argc, char **argv) {

    // Se crea una matriz de punteros Celda con 3 filas.
    Celda** Matriz = calloc(3, sizeof(Celda*));

    // Se asigna memoria para cada fila de la matriz, cada una con 3 elementos de tipo Celda.
    for (int i = 0; i < 3; i++){
        Matriz[i] = calloc(3, sizeof(Celda));
    }

    // Se asigna a cada celda de la matriz los valores de x e y correspondientes.

    // Es importante notar que cuando llamamos a Matriz[i][j], con un i y j en particular,
    // este contiene el struct celda y no hay que crear otro como se estaba haciendo en un principio.
    // Ademas como Matriz[i][j] es directamente el struct, accedemos a sus parametros con un punto
    // y no con una flecha, ya que no es un puntero.


    for (int i = 0; i <3; i++){
        for (int j = 0; j < 3; j++){
            Matriz[i][j].x = i;
            Matriz[i][j].y = j;
        }
    }

    // Se imprime la matriz.
    for (int i = 0; i < 3; i++){
        printf("|");
        for (int j = 0; j < 3; j++){
            printf(" %d , %d |", Matriz[i][j].x, Matriz[i][j].y);
        }
        printf("\n");
    }    

    // Se libera la memoria asignada para cada fila de la matriz.
    for (int i = 0; i < 3; i++){
        free(Matriz[i]);
    }

    // Se libera la memoria asignada para la matriz
    free(Matriz);

    return 0; // Buena practica
}