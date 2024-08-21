#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int main ()
{
  pid_t child_pid;
 
   /* Create child*/
  child_pid = fork ();
  if (child_pid > 0) {
 
    /* Parent process */
    sleep (30);
  }
  else {
 
    /*Child process. Exit immediately. */
    exit (0);
  }
  return 0;
}
