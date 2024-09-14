#include "main.h"
/**
 * _islower - Checks for lowercase characters
 * @c: a variable
 * 
 * Return: 1 if c is lowercase,
 *         0 if c is uppercase
*/
int _islower(int c)
{
    if (c >= 'a' && c <= 'z')
    {
        return (1);
    }
    else
    {
        return (0);
    }
}
// If the argument passed to _islower is having an ASCII Value lower that that of 'a' (97) and 'z' (122), 
// for example 'H' having an ASCII Value of 72, it returns 0. But if is in that range of 'a' to 'z', it 
// returns a value of 1.
