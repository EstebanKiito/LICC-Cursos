#include "stdio.h"

int main() {
  printf("         void: %d\n", sizeof(         void));  /* This should not compile */
  printf("         char: %d\n", sizeof(         char));
  printf("    short int: %d\n", sizeof(    short int));
  printf("          int: %d\n", sizeof(          int));
  printf("     long int: %d\n", sizeof(     long int));
  printf("long long int: %d\n", sizeof(long long int));
  printf("        float: %d\n", sizeof(        float));
  printf("       double: %d\n", sizeof(       double));
}
