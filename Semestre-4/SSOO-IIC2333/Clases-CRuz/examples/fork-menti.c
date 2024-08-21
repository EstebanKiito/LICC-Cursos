/* 

   Compile with:
     gcc -o fork-menti fork-menti.c

   Run (in Unix/Linux/MacOSX) with:
     ./fork-menti

  This code prints "*" 6 times.

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

