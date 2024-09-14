#include "main.h"
/**
 * print_last_digit - prints the last digit of a number
 * @n: The number to be printed from
 * Returns: the value of the last digit of n
*/
// The last value of an integer can be gotten using the modulo operation (%) 😲

int print_last_digit(int b)
{
    int m, n;
    if (b == 0 || b > 0)
    {
        m = b % 10;     // m stores the remainder of (b divided by 10), which is the last digit of b 😲
        _putchar(m + '0');
        return (m);
    }
    else
    {
        m = b * -1;    // m stores the positive value of b if b is < 0, which is negative.
        n = m % 10;    // n stores the remainder of (b divided by 10), which is the last digit of b 😲
        _putchar(n + '0');
        return(n);
    }
}
