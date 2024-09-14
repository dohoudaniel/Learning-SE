#include <stdio.h>

/**
 * main - prints the address of an array
 *
 * Return: Always 0.
 */
int main(void)
{
	char b[98]; /* An array of characters. */

	printf("b: %p\n", b);
	printf("&b: %p\n", &b); /* Prints the address of b, same as &b[0] */

	return (0);
}
