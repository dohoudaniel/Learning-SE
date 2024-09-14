#include <stdio.h>

/**
 * main - calls other functions
 *
 * Return: Always 0
 */
int main(void)
{
	int num = 5;

	printf("The number doubled is: %d\n", doubled(&num));

	return (0);
}
