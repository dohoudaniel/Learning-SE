#include "main.h"

/**
 * _isalpha - A function that checks for alphabetic characters
 * @c: The argument
 * 
 * Return: 1 if c is a letter, uppercase or lowercase, 0 if otherwise.
 */

int _isalpha(int c)
{
    if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
    {
        return (1);
    }
    else
    {
        return (0);
    }
}
