#include <stdio.h>

/**
 * main - Dereferencing pointers, example with int and char tyes
 *
 * Return: Always 0.
 */
int main(void)
{
	/* Declaring variables */
	int n;
	int *p;
	char c;
	char *pp;

	/* Assigning values */
	c = 'H';
	pp = &c;
	n = 98;
	p = &n;

	/* Printing */
	printf("Value of 'c': %d ('%c')\n", c, c); /* The putchar() function came into play here */
	printf("Address of 'c': %p\n", &c);
	printf("Value of 'pp': %p\n", pp);
	printf("Value of 'n': %d\n", n);
	printf("Address of 'n': %p\n", &n);
	printf("Value of 'p': %p\n", p);

	/* Dereferencing begins ... */
	*p = 402;
	*pp = 'o';

	/* Printing */
	printf("Value of 'n': %d\n", n);
	printf("Value of '*pp': %d\n", *pp); /* The putchar() function came into play here */
	printf("Value of 'c': %d ('%c')\n", c, c);
	printf("Value of '*pp': %d ('%c')\n", *pp, *pp);

	return (0);
}
