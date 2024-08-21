/* 
   Compile with:
     gcc -o fork3 fork3.c

   Run (in Unix/Linux/MacOSX) with:
     ./fork3

*/


#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main(int argc, char *arg[]) {
  int pid;
  int i=0;
  for(i=0; i<4; i++) {
    fork();
    printf("[%4d] %d\n", getpid(), i);
  }
  return 0;
}


