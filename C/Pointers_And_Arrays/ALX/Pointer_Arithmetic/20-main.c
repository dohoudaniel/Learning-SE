#include <stdio.h>

/**
 * main - Pointers arithmetic.
 *
 * Return: Always 0.
 */
int main(void)
{
	int *p;
	int a[2];
	int n;

	p = &n;
	printf("p = &n;\np: %p\n\n", p);
	printf("p + 1: %p\n\n", p + 1);
	printf("p + 2: %p\n\n", p + 2);
	printf("p + 10: %p\n\n", p + 10);

	/* possible since a is evaluated */
	/* as an int * in this context */
	p = a;
	printf("p = a;\np: %p\np + 1: %p\n\n", p, p + 1);

	/* This is the pointers arithmetic. */
	/* The computer knows that a points to an integer. */
	/* The computer also knows that the size of an integer in memory */
	/* is sizeof(int) bytes - in this case 4 bytes - and */
	/* concludes that the next element of this type */
	/* will be stored 4 bytes later in memory. */

	return (10);
}
