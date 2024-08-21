/* Source: http://www.amparo.net/ce155/fork-ex.html 

   Compile with:
     gcc -o fork5 fork5.c

   Run (in Unix/Linux/MacOSX) with:
     ./fork5

*/

#include <unistd.h>     /* Symbolic Constants */
#include <sys/types.h>  /* Primitive System Data Types */ 
#include <stdio.h>      /* Input/Output */
#include <sys/wait.h>   /* Wait for Process Termination */
#include <stdlib.h>     /* General Utilities */

int main() {
  pid_t pid;

  /* fork a child process */
  pid = fork();

  if (pid < 0) { 
    /* error occurred */
    fprintf(stderr, "Fork Failed"); 
    return 1;
  }
  else if (pid == 0) { 
    /* child process */
    printf("Child about to do exec\n"); 
    execlp("/bin/ls","ls",NULL);
    printf("Child done with exec\n");
  }
  else {
    /* parent process */
    /* parent will wait for the child to complete */
    wait(NULL);
    printf("Child Complete\n");
  }
  return 0;
}

