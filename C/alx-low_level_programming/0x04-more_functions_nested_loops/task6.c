#include "main.h"

/**
 * print_line - a function that draws a straight line
 * @n: The number of times the line character should be drawn
 * Return: Nothing.
*/
void print_line(int n)
{
    int d;
    
    if (n < 0 || n == 0)
    {
        _putchar('\n');
    }

    else
    {
        for (d = 1; d <= n; d++)
        {
            _putchar('_');
        }
        _putchar('\n');
    }
}
