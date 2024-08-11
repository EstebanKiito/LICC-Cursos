#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int a, b;
    scanf("%d %d", &a, &b); //agregamos & a las variables
    int i = 1;
    int maximo = 1;
    while (i <= a && i <= b){ //cambiamos and por &&
        if (a%i==0 && b%i==0){ //cambiamos and por &&
            maximo = i;
        }
        i++;
    }
    printf("%d", maximo);
    return 0;
}
