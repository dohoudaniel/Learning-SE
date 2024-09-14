#include "main.h"

/**
 * print_square - prints a square followed by a new line
 * @size: The size of the square.
 * Return: Nothing.
*/
void print_square(int size)
{
    int a, b;

    if (size <= 0)
    {
        _putchar('\n');
    }
    else
    {
        for (a = 0; a < size; a++)
        {
            for (b = 0; b < size; b++)
            {
                _putchar(35); // The putchar of 35 is '#'
            }
            _putchar('\n');
        }
    }
    /* _putchar('\n'); */
}
