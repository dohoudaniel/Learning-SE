#include "main.h"
/**
 * print_alphabet - Function to print alphabets
 * @d: A var of type char
 * Return: Nothing
*/
void print_alphabet(void)
{
    char d;

    for (d = 'a'; d <= 'z'; d++)
    {
        _putchar(d);
    }

    _putchar('\n');
}
