#include "main.h"
/**
 * jack_bauer - Prints the clock format of 24 hours, every minuite of the day using for loops and the _putchar() function.
 * @b: An integer for the hour format
 * @m: An integer for the minuites format
 * Return: Nothing.
*/
void jack_bauer(void)
{
    int b, m;

    for (b = 0; b <= 23; b++)
    {
        for (m = 0; m <= 59; m++)
        {
            _putchar(b / 10 + '0');
            _putchar(b % 10 + '0');
            _putchar(':');
            _putchar(m / 10 + '0');
            _putchar(m % 10 + '0');
            _putchar('\n');
        }
    }
}
