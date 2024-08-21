/* 

   Compile with:
     gcc -o fork-menti2 fork-menti2.c

   Run (in Unix/Linux/MacOSX) with:
     ./fork-menti2

   This code prints "*" twice.
   The parent prints "*" once, and the child prints "*",
   then, the child "becomes" the command "ls" (execlp)
   so the rest of the child's code is never executed.

*/

#include <unistd.h>     /* Symbolic Constants */
#include <sys/types.h>  /* Primitive System Data Types */ 
#include <errno.h>      /* Errors */
#include <stdio.h>      /* Input/Output */
#include <sys/wait.h>   /* Wait for Process Termination */
#include <stdlib.h>     /* General Utilities */
#include <string.h>     /* String utilities */

int main() {

    pid_t childpid; 
    int retval;     
    int status;     
        
    /* now create new process */
    childpid = fork();
    
    if (childpid == 0) { 
        printf("[%d] *\n", getpid());
        // 'ls' es un comando que lista el directorio
        execlp("/bin/ls","ls",NULL);
        childpid = fork();
        if (childpid == 0) {
            printf("[%d] *\n", getpid());
        }
        else { 
	        printf("[%d] *\n", getpid());
        }
        printf("[%d] *\n", getpid());
    }
    else {
        printf("[%d] *\n", getpid());
    }
    return 0;
}

