/**
 * This program prints all the arguments, without using ac
 */

#include <stdio.h>
#include <stdlib.h>

int main(__attribute__((unused))int argc, char **argv)
{
	int idx = 0;
	while (argv[idx])
	{
		printf("argv[%d]: %s\n", idx, argv[idx]);
		idx++;
	}
	return (0);
}
