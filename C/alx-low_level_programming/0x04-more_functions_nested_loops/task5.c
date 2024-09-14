#include "main.h"

/**
 * more_numbers - Prints the numbers 0 through 14 ten times
 * @a: A variable that stores from 1 to 10
 * @b: A variable that stores from 0 to 14
 * @c: A variable that stores the remainder when b > 9 and  b < 15
 * 
 * Return: Nothing
 */
void more_numbers(void)
{
    int a, b, c;

    for (a = 1; a <= 10; ++a)
    {
        for (b = 0; b <= 14; ++b)
        {
            c = b;  // We used c here so that it will be useful in the if-loop.

            if (c > 9)
            {
                _putchar(49); // Prints '1' to STDOUT.
                c = b % 10;
            }
            _putchar(c + 48); // This will occur when c (which is equal to b) > 9, and when c < 9 too.
        }
        _putchar('\n');
    }
}
