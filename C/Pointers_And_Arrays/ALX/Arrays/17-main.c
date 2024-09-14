#include <stdio.h>

void f(int *a);

/**
 * main - Illustrating the array type decay
 *
 * Return: Always 0.
 */
int main(void)
{
	int *p; /* a pointer to an integer */
	int t[10]; /* An array */

	p = t; /* This works because of the auto implicit conversion to (int *) */
	/* Auto implicit conversion is also called automatic type conversion. */

	printf("t: %p\n", t);
	printf("&t[0]: %p\n", &t[0]);
	printf("p: %p\n", p);

	f(t);
	/* The line above is the same as: f(p); */

	return (0);
}

/**
 * f - prints the value of a pointer of type int
 * @a: address of an integer we need to print
 *
 * Return: Nothing.
 */
void f(int *a)
{
	printf("a: %p\n", a);

	return;
}
