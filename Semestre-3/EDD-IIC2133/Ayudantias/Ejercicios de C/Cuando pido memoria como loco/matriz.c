#include <stdio.h>
#include <stdlib.h>

/*
Este código crea una matriz en donde cada celda contiene justamente
un struct llamado Celda, donde sus atributos son los enteros x, y. 
Luego, asigna valores a cada celda de la matriz y los imprime en la 
consola. Finalmente, libera la memoria asignada para la matriz y sus 
filas. Lamentablemente el código tiene problemas en dos partes indicadas,
los que deberas arreglar para que el programa funcione. 

Para compilar:
gcc matriz.c -o matriz

Para ejecutar:
./matriz

*/

// Definición del struct Celda, que contiene dos enteros, x e y.
// NO CAMBIAR
typedef struct celda_t {
    int x;
    int y;
} Celda;

int main(int argc, char **argv) {
    //    Se crea una matriz de punteros Celda con 3 filas.
    //    NO CAMBIAR        
    Celda** Matriz = calloc(3, sizeof(Celda*));

    //    Se asigna memoria para cada fila de la matriz, cada una con 3 elementos de tipo Celda.
    //    NO CAMBIAR
    for (int i = 0; i < 3; i++){
        Matriz[i] = calloc(3, sizeof(Celda));
    }

    //    Se asigna a cada celda de la matriz los valores de x e y correspondientes.
    //    AQUI ESTA MALO, DEBES HACER CAMBIOS
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            Celda* nueva_celda = calloc(1, sizeof(Celda));
            nueva_celda -> x = i;
            nueva_celda -> y = j;

            Matriz[i][j] = nueva_celda;
        }
    }

    //    AQUI DEBES COMPLETAR EL printf() PARA IMPRIMIR LA MATRIZ DE LA SIGUIENTE FORMA:
    //     0 , 0 | 0 , 1 | 0 , 2 |
    //     1 , 0 | 1 , 1 | 1 , 2 |
    //     2 , 0 | 2 , 1 | 2 , 2 |

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            printf("");
        }
        printf("\n");
    }    

    //    Se libera la memoria asignada para cada fila de la matriz.
    //    NO CAMBIAR
    for (int i = 0; i < 3; i++){
        free(Matriz[i]);
    }  

    //    Se libera la memoria asignada para la matriz
    //    NO CAMBIAR
    free(Matriz);

    return 0; // Buena practica
}


