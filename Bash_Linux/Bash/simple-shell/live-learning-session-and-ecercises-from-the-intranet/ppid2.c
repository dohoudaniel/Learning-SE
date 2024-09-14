#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(void)
{
	pid_t my_ppid;

	my_ppid = getpid();
	printf("%u\n", my_ppid);
	return (0);
}
