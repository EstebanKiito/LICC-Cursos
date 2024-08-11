#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n; //agregamos el tipo de dato
    scanf("%d", &n);
    for (int i = 0; i < n; i++){ //agregamos i = 0
        for (int j = 0; j < i + 1; j++){ //agregamos j = 0
            printf("*");
        }
        printf("\n"); // incluimos el salto de linea
    }
    return 0;
}
