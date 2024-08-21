#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/time.h>

#define DEPTH 3
#define BRANCHING 2
#define true 1
#define false 0
typedef short bool;

int main(int argc, char ** argv) {

  for(int i = 0; i < DEPTH; i++){
    bool parent = true;

    for(int j = 0; j < BRANCHING && parent; j++){
      if(!fork()){
        printf("PARENT %d - CHILD %d\n", getppid(), getpid());
        parent = false;
      }
    }

    for(int j = 0; j < BRANCHING; j++){
      int status;
      wait(&status);
    }

    if(parent) return 0;
      sleep(5);
  }

  return 0;
}