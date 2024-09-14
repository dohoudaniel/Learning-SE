#include "main.h"

/**
 * print_number - Prints a number
 * @n: The number to be printed
 * Return: Nothing.
 */
void print_number(int n)
{
    unsigned int d = n;

    /* Checking if n is negative */
    if (n < 0)
    {
        _putchar('-');
        d = -d;
    }

    /* Prints the first digits */
    if ((d / 10) > 0)
    {
        print_number(d / 10);
    }

    /* Prints the last digit */
    _putchar((d % 10) + 48);
}
