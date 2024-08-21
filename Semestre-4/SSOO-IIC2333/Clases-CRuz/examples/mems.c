/*
  Compile with:

  gcc -o mems mems.c

*/

#include <stdio.h>
#include <stdlib.h>

int b = 3;

int main(int argc, char *argv[]) {
    int x=3;
    printf("Location of code   : %p\n", (void *)main);
    printf("Location of data   : %p\n", (void *)&b);
    printf("Location of heap   : %p\n", (void *)malloc(1));
    printf("Location of stack  : %p\n", (void *)&x);
    return x+b;
}

