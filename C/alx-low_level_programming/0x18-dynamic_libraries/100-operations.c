#include <stdio.h>
/* #include <stdlib.h> */
#include <math.h>

/**
 * add - A function that adds two numbers.
 * @a: First Integer.
 * @b: Second Integer.
 *
 * Return: Added numbers.
 */
int add(int a, int b)
{
	int addition = a + b;

	return (addition);
}

/**
 * sub - A function that subtracts between two numbers.
 * @a: First Integer.
 * @b: Second Integer.
 *
 * Return: Difference in two numbers.
 */
int sub(int a, int b)
{
	int difference = a - b;

	return (difference);
}

/**
 * mul - A function that multiplies two numbers
 * @a: First Integer.
 * @b: Second Integer.
 *
 * Return: Product of two numbers
 */
int mul(int a, int b)
{
	int product = (int) a * b; /* Typecasting */

	return (product);
}

/**
 * div - A function that divides a number by another.
 * @a: First Integer.
 * @b: Second Integer.
 *
 * Return: Quotient of numbers.
 */
int div(int a, int b)
{
	int quotient = (int) a / b; /* Typecasting */

	return (quotient);
}

/**
 * mod - A function that calculates the modulo of two integers.
 * @a: First Integer.
 * @b: Second Integer.
 *
 * Return: Modulo.
 */
int mod(int a, int b)
{
	int modulo = (int) a % b;

	return (modulo);
}
