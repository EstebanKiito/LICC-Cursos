/* Source: http://www.amparo.net/ce155/fork-ex.html 

   Compile with:
     gcc -o fork-menti3 fork-menti3.c

   Run (in Unix/Linux/MacOSX) with:
     ./fork-menti3

   This code prints "*" 5 times.
   The parent never prints "*" because it "transform" into the command "ls".
   The children, however, continue their normal execution.

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
        // 'ls' es un comando que lista el directorio
        execlp("/bin/ls","ls",NULL);
        printf("[%d] *\n", getpid());
    }
    return 0;
}

