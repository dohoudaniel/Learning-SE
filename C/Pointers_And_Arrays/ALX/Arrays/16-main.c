#include <stdio.h>

/**
 * main - An array is not a pointer, but...
 *
 * Return: Always 0.
 */
int main(void)
{
	int a[98]; /* array */

	printf("a: %p\n", a); /* Printing the address of a */
	printf("&a[0]: %p\n", &a[0]); /* Printing the address of the first index of a */

	/* The address of a = t]The address of a[0] */
	/* The value of an array is the address of the first element of the same array. */

	return (0);
}
