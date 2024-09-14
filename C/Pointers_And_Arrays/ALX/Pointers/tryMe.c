#include <stdio.h>

/**
 * modify_my_char_var - Solve me.
 * @cc: A pointer to ccc.
 * @ccc: A character.
 * Return: Nothing.
 */
void modify_my_char_var(char *cc, char ccc)
{
	*cc = 'o';
	ccc = 'l';
}

/**
 * main - Solve me.
 *
 * Return: Always 0.
 */
int main(void)
{
	char c;
	char *p;

	/* Modifying the values of our variables */
	p = &c;
	c = 'H';

	/* print statements */
	printf("Address of 'c': %p\n", &c);
	printf("Value of 'c': %c\n", c);
	printf("Value of 'p': %p\n", p);
	printf("Address of 'p': %p\n", &p);

	/* Function call */
	modify_my_char_var(p, c);
	printf("\nAfter function call....\n");
	printf("Value of 'c': %c\n", c);
	printf("Address of 'c': %p\n", &c);
	printf("Value of 'p': %p\n", p);
	printf("Address of 'p': %p\n", &p);

	return (0);
}
