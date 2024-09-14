#include <stdio.h>

/**
 * main - An array printed with and without the unary operator.
 *
 * Return: Always 0.
 */
int main(void)
{
	int Daniel;

	printf("Daniel (printed without unary operator): %p\n", Daniel);
	printf("Daniel (printed with unary operator): %p\n", &Daniel);

	return (0);
}
