#include <stdio.h>

/**
 * main - Printing the size, in bytes, of a pointer
 *
 * Return: Always 0.
 */
int main(void)
{
	int *p;

	printf("Size of pointer 'p': %lu\n", sizeof(p));
	/* Prints: Size of pointer 'p': 8 */

	return (0);
}
