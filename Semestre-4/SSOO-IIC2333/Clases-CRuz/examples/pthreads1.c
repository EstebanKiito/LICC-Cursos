/*
  Compile with:

  gcc -o pthreads1 pthreads1.c -lpthread

*/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_THREADS 10

void* print_hello_world(void* tid) {
	/* This function prints the thread’s identifier and then exits. */
	printf("Hello World. Greetings from thread %ld\n", (long)tid );
	pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
	/* The main program creates 10 threads and then exits. */
	pthread_t threads[NUMBER_OF_THREADS];
	int status;
	long i;
	for(i=0; i < NUMBER_OF_THREADS; i++) {
		printf("[main] Creating thread %ld\n", i);
		status = pthread_create(&threads[i], NULL, print_hello_world, (void *)i);
		if (status != 0) {
			printf("[main] Oops. pthread_create returned error code %d\n", status);
			exit(-1);
        }
    }
	exit(0);
}
