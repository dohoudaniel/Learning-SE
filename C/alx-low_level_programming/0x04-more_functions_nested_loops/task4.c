#include "main.h"

/**
 * print_most_numbers - Prints all numbers from 0 to 9 except 2 and 4
 * Return: Nothing.
*/
void print_most_numbers(void)
{
    int d;

    for (d = 0; d <= 9; d++)
    {
        if (d == 2 || d == 4)
        {
            continue;
            /* This skips the loop when the values of d are 2 or 4 */
        }
        _putchar(d + 48);
    }
    _putchar('\n');
}
