#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "./Objects/struct.h"

/* Retorna true si ambos strings son iguales */
bool string_equals(char *string1, char *string2) {
	return !strcmp(string1, string2);
}

/* Revisa que los parametros del programa sean válidos */
bool check_arguments(int argc, char **argv) {
	if (argc != 3) {
		printf("Modo de uso: %s INPUT OUTPUT\n", argv[0]);
		printf("Donde:\n");
		printf("\tINPUT es la ruta del archivo de input\n");
		printf("\tOUTPUT es la ruta del archivo de output\n");
		return false;
	}

	return true;
}

int main(int argc, char **argv) {
	if (!check_arguments(argc, argv)) {
		/* Salimos del programa indicando que no terminó correctamente */
		return 1;
	}

	/* Abrimos el archivo de input */
	FILE *input_file = fopen(argv[1], "r");

	/* Abrimos el archivo de output */
	FILE *output_file = fopen(argv[2], "w");

	int N_EVENTS;
	fscanf(input_file, "%d", &N_EVENTS);

	/* String para guardar la instrucción actual*/
	char command[32];

	for (int event = 0; event < N_EVENTS; event++) {
		/* Leemos el evento */
		fscanf(input_file, "%s", command);

		/* [Por implementar] A continuación debes implementar cada evento */
		if (string_equals(command, "PRINT")) {
			char to_print[32];
			fscanf(input_file, "%s", to_print);
			printf("%s\n", to_print);
		}
		else if (string_equals(command, "WRITE")) {
			char to_write[32];
			fscanf(input_file, "%s", to_write);
			fprintf(output_file, "%s\n", to_write);

		} else if (string_equals(command, "POINT")){
			int x, y;
			fscanf(input_file, "%d %d", &x, &y);
			Point* point = createPoint(x, y);
			printPoint(point);
			freePoint(point);
		} else {
			continue;
		}
	}


	fclose(input_file);
	fclose(output_file);

	return 0;
}
