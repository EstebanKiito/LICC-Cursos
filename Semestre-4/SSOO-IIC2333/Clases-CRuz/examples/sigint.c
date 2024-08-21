#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

void sigint_handler(int dummy) {
	printf("%d %s\n", dummy, "CTRL + C");
	printf("%s\n", "Continuando...");
    exit(0);
}

int main(int argc, char *argv[]){
	printf("Arguments %d\n", argc);

	int i;
	for(i = 0; i < argc; i++){
		printf("Argument %d: %s\n", i + 1, argv[i]);
	}

	signal(SIGINT, sigint_handler);

	while(1){};
}
