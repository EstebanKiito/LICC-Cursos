#define _GNU_SOURCE
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <signal.h>

int main(int argc, char *argv[]) {
   pid_t tid;
   tid = syscall(SYS_gettid);
   tid = syscall(SYS_tgkill, getpid(), tid, SIGHUP);
}


