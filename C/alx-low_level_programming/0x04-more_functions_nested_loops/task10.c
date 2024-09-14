#include "main.h"

/**
 * print_triangle - prints a triangle
 * @size: size of the triangle
 * Return: Nothing.
 */
void print_triangle(int size)
{
    int b, m;

    if (size <= 0)
    {
        _putchar('\n');
    }

    else
    {
        for (b = 1; b <= size; b++)
        {
            for (m = 1; m <= size; m++)
            {
                if ((b + m) <= size)
                {
                    _putchar(' ');
                }
                else
                {
                    _putchar('#');
                }
            }
            _putchar('\n');
        }
    }
}
