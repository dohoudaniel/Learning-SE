#include "main.h"
/**
 * print_sign - main function
 *  @n: The argument
 * Return: 1 if positive, 0 if zero, -1 if negative
 */
int print_sign(int n)
{
    if (n > 0)
    {
        _putchar('+');
        return (1);
        // Prints '+' and returns 1 if n > o
    }
    else if (n == 0)
    {
        _putchar('0');
        return (0);
        // Prints '0' and returns 0 if n == 0
    }
    else
    {
        _putchar('-');
        return (-1);
        // Prints '-' and returns -1 if n < 1
    }
}
