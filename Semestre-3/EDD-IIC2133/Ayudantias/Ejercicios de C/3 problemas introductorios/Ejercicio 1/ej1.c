#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Este código tiene 4 errores */
    n;
    scanf("%d", &n);
    for (int i; i < n; i++){
        for (int j; j < i + 1; j++){
            printf("*");
        }
    }
    return 0;
}
