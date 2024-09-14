#include "main.h"

/**
 * print_diagonal - prints a diagonal line on the terminal
 * @n: The number of times the diagonal should be printed
 */
void print_diagonal(int n)
{
    int line;
    int space;

    if (n <= 0)
    {
        _putchar('\n');
    }

    else
    {
        for (line = 0; line < n; line++)
        {
            for (space = 0; space < line; space++)
            {
                _putchar(' ');
            }
            _putchar(92);
            _putchar('\n');
        }
    }
}
