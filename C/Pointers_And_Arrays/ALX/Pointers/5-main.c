#include <stdio.h>

/**
 * main - Dereferencing pointers.
 *
 * '*' - The dereference operator
 * Return: Always 0.
 */
int main(void)
{
	int n;
	int *p;

	n = 100;
	p = &n;

	printf("Value of 'n': %d\n", n);
	printf("Address of 'n': %p\n", &n);
	printf("Value of 'p': %p\n", p);

	/* This updates the value of n.*/
	*p = 402;
	printf("Value of 'n': %d\n", n);

	return (0);
}
