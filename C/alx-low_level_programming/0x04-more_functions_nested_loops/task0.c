#include "main.h"
#include <stdio.h>

/**
 * _isupper - checks for uppercase
 * @c: the character to be checked
 * Return: 1 if c is uppercase, 0 if otherwise
 */
int _isupper(int c)
{
    if (c >= 65 && c <= 90)
    {
        return (1);
    }
    else
    {
        return (0);
    }
    /* The putchar values table comes in here. So if c >= 65 (with a putchar value of 'A'), 
    and c <= 90 (with a putchar value of 'Z'), it returns 1. I f otherwise, it returns 0. */
}
