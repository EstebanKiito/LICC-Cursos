#include <stdio.h>
#include <string.h>
#include <ctype.h>

void encontrarPalabraMasLarga(const char *texto) {
    
    int init = 0;
    int fin = -1;
    int init_maslarga = 0;
    int fin_maslarga = 0;
    for (int i = 0; i < strlen(texto); i++){
        if (texto[i] != ' '){ 
            fin += 1;
        } else {
            if (fin - init > fin_maslarga - init_maslarga){
                init_maslarga = init;
                fin_maslarga = fin; // cambiamos el lugar de la llave
            }
            init = i + 1;
            fin = init - 1;
        }
    }
    if (fin - init > fin_maslarga - init_maslarga){
        init_maslarga = init;
        fin_maslarga = fin;
    }
    for (int i = init_maslarga; i < fin_maslarga + 1; i++){ // agregamos el for
        printf("%c", texto[i]); // colocamos el tipo correcto para imprimir
    }
    printf("\n");
    printf("%d",fin_maslarga - init_maslarga + 1);
}

int main() {
  	
  	//NO TOCAR
    char texto[1000];
    fgets(texto, sizeof(texto), stdin);
    encontrarPalabraMasLarga(texto);

    return 0;
}
