/* Displaying an unsigned int in bits */
#include <stdio.h>

void displayBits(unsigned int value); /* Prototype */

/**
 * main - Displaying an unsigned int in bits
 *
 * Return: Nothing.
 */
int main(void)
{
	unsigned int x; /* Variable to hold user input */

	printf("%s", "Enter a non-negative integer: ");
	scanf("%u", &x);

	displayBits(x);
}

/* Display bits of unassigned int value */
void displayBits(unsigned int value)
{
	/* Define displayMark and left shift 31 bits.*/
	unsigned int displayMark = 1 << 31;

	printf("%10u = ", value);

	/* Loop through bits */
	for (unsigned int c = 1; c <= 32; ++c)
	{
		putchar(value & displayMark ? '1': '0'); /* A ternary operator */
		value <<= 1; /* Shift value left by 1 */

		if (c % 8 == 0)
		{
			/* Output space after 8 bits */
			putchar(' ');
		}
	}
	putchar('\n');
}
