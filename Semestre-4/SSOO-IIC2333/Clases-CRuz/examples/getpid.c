/* 
   Compile with:
     gcc -o getpid getpid.c

   Run (in Unix/Linux/MacOSX) with:
     ./getpid

*/


#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main(int argc, char *arg[]) {
  int pid;
  pid = getpid();
  printf("[%4d]\n", pid);
  return 0;
}


