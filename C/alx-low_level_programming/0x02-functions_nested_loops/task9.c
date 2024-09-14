#include "main.h"
/**
 * times_table - Prints the 9 times table, starting from 0.
 *
 * Return: Nothing.
 */
void times_table(void)
{
    int a, b, c, d, e;

    // b will increase 10 times (from 0 to 9) for one value of a (one increment in a)
    // So, b will increase 100 times. This is because a increases from 0 to 9 too.

    for (a = 0; a <= 9; a++)
    {
        for (b = 0; b <= 9; b++)
        {
            c = a * b;

            if (c > 9)
            {
                // d != c. d can never be equal to c.
                // This loop first occurs when a = 2, and b = 5.
                // As thus, d = 0 (10 % 10), e = 1 ((10 - 0) / 10).
                // Therefore, the putchar of e + '0' = putchar of 1 + 48 = putchar of 49 = 1.
                // Also, the putchar of d + '0' = putchar of 0 + 48 = putchar of 48 = 0.
                d = c % 10;
                e = (c - d) / 10;

                _putchar(44); // _putchar of 44 is ','
                _putchar(32); // _putchar of 32 is SP (Space).
                _putchar(e + '0');
                _putchar(d + '0');

                /* Explanation of this loop */
                // d != c. d can never be equal to c.
                // This loop first occurs when a = 2, and b = 5.
                // As thus, d = 0 (10 % 10), e = 1 ((10 - 0) / 10).
                // Therefore, the putchar of e + '0' = putchar of 1 + 48 = putchar of 49 = 1.
                // Also, the putchar of d + '0' = putchar of 0 + 48 = putchar of 48 = 0.
            }
            else
            {
                // This if-loop will keep occurring until c is greater than 9
                // and because b can never be equal to 0
                if (b != 0)
                {
                    _putchar(44); // _putchar of 44 is ','
                    _putchar(32);
                    _putchar(32);
                }

                _putchar(c + '0');
            }
        }
        _putchar('\n');
    }
}
