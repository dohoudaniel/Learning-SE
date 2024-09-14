#include "main.h"

/**
 * _abs(): a function that prints the absolute value of the number passed in as an argument
 * @n: An integer that will be made absolute
 * Return: n or (n * -1)
*/
int _abs(int n)
{
    if (n > 0)
    {
        return (n);
    }
    else if (n == 0)
    {
        return (n);
    }
    else
    {
        return (n * -1);
    }
}
