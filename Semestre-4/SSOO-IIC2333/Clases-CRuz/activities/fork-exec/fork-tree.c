#include <stdio.h>     // printf
#include <stdlib.h>    // exit
#include <unistd.h>    // fork, exec
#include <sys/wait.h>  // wait

// $ man 2 fork
// ------------
// pid_t fork();

// $ man 3 exec
// ------------
// int execl(const char *path, const char *arg, ...
//                 /* (char  *) NULL */);
// int execlp(const char *file, const char *arg, ...
//                 /* (char  *) NULL */);
// int execle(const char *path, const char *arg, ...
//                 /*, (char *) NULL, char * const envp[] */);
// int execv(const char *path, char *const argv[]);
// int execvp(const char *file, char *const argv[]);
// int execvpe(const char *file, char *const argv[],
//                 char *const envp[]);

// $ man 3 exit
// ------------
// void exit(int status);



// Build this binary process tree of height 2:
//                         p0
//                       /    \
//                      /      \
//                    p1        p2
//                   /  \      /  \
//                 p11  p12  p21  p22
//
// Where
//    * each /p./  print '[PPID:PID]: child CPID\n' on each fork
//    * each /p../ print '[PPID:PID]: terminating\n'
//    * /p0/  waits for all descendants and then execs 'date -u --rfc-3339=seconds'
int main() {

	return 0;
}
