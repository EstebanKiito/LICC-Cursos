#include "struct.h"
#include <stdlib.h>



void write_file(FILE *output_file, char *to_write) {
    fprintf(output_file, "%s\n", to_write);
}

Point* createPoint(int x, int y) {
    Point* point = calloc(sizeof(Point), 1);
    point->x = x;
    point->y = y;
    return point;
}

void printPoint(Point* point) {
    printf("(%d, %d)\n", point->x, point->y);
}

void freePoint(Point* point) {
    free(point);
}

int one(){
    return 1;
}