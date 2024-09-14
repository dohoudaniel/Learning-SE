#include <stdio.h>

/**
 * main - storing the address of variable into a pointer
 *
 * Return: Always 0.
 */
int main(void)
{
	int n;
	int *p;

	n = 100;
	p = &n;

	printf("Address of n: %p\n", &n);
	printf("Value of 'p': %p\n", p);

	if (p == &n)
	{
		printf("'p' stores the address of the variable 'n'\n");
	}

	return (0);
}
