#include <stdio.h>

/**
 * modify_my_param - set the integer to 402
 * @m: a pointer to the integer we want to set to 402
 *
 * Return: Nothing.
 */
void modify_my_param(int *m)
{
	printf("Value of 'm': %p\n", m);
	printf("Address of 'm': %p\n", &m);
	*m = 402;
	/* We used this function to modify a number */
}

/**
 * main - how to change the value of a variable from outside the function
 * it is declared in, using a pointer.
 *
 * Return: Always 0.
 */
int main(void)
{
	/* Declare variables */
	int n;
	int *p;

	/* Assign values */
	p = &n;
	n = 98;

	/* Printing */
	printf("Value of 'n' before the call: %d\n", n);
	printf("Address of 'n': %p\n", &n);
	printf("Value of 'p': %p\n", p);
	printf("Address of 'p': %p\n", &p);

	/* Function call */
	modify_my_param(p);
	printf("Value of 'n' after the call: %d\n", n);

	return (0);
	/* When we leave the function modif_my_param , the variable m is destroyed,*/
       /* but n’s value is still 402 */
}
