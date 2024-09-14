#include <stdio.h>

/**
 * main - prints the size of an array and the address of an array
 * @b: The array
 * @&b: The address of an aray.
 * Return: Always 0.
 */
int main(void)
{
	char b[98];

	/* Printing the adress of the array 'b' */
	printf("b: %p\n", b);
	printf("&b: %p\n", &b);

	/* Printing the size of'b' and '&b' */
	printf("sizeof(b): %lu\n", sizeof(b));
	printf("sizeof(&b): %lu\n", sizeof(&b));

	return (0);
}
