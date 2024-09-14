#include "main.h"
/**
 * print_times_table - Prints a multiplication table of n
 * @n: The number to be treated
 * Return: Multiplication Table
 */
void print_times_table(int n)
{
    // Defined three integers
    int a, b, c;

    if (n >= 0 && n <= 14)
    {
        // These loops run as long as a and b are less than or equal to n

        for (a = 0; a <= n; a++)
        {
            for (b = 0; b <= n; b++)
            {
                c = a * b;
                if (c > 99)
                {
                    _putchar(',');
                    _putchar(32); // A space
                    _putchar((c / 100) + '0');
                    _putchar(((c / 10) % 10) + '0');
                    _putchar((c % 10) + '0');
                }
                else if (c > 9)
                {
                    _putchar(',');
                    _putchar(32);
                    _putchar(32);
                    _putchar(((c / 10) % 10) + '0');
                    _putchar((c % 10) + '0');
                }
                else
                {
                    if (b != 0)
                    {
                        _putchar(',');
                        _putchar(32);
                        _putchar(32);
                        _putchar(32);
                    }
                    _putchar(c + '0');
                }
            }
            _putchar('\n');
        }
    }
}
// Try using 10 and 100 to understand the way the loops work.
