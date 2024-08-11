#include <stdio.h>
#include <stdlib.h>

typedef struct Point {
    int x;
    int y;
} Point;


void printPoint(Point* p);
void write_file(FILE *output_file, char *to_write);
Point* createPoint(int x, int y);
void freePoint(Point *p);
int one();
