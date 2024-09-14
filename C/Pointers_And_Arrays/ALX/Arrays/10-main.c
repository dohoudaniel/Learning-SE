#include <stdio.h>

/**
 * main - You can not modify a
 *
 * Return: Always 0.
 */
/* NB: This program is meant to return an error during compilation. */
int main(void)
{
	int a[5]; /* An array */
	int b;
	int c[5]; /* An array */

	a = 0; /* nope */
	a = &b; /* nope */
	a = c; /* nope */

	return (0);
}
