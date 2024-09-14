#include "main.h"

/**
 * main - check the code
 * 
 * Return: Always 0.
*/
/**
 * For comments to understand this file, check the task3-main.c comments.
*/

int main(void)
{
    int r;

    r = _isalpha('H');
    _putchar(r + '0');

    r = _isalpha('o');
    _putchar(r + '0');

    r = _isalpha(108);
    _putchar(r + '0');

    r = _isalpha(';');
    _putchar(r + '0');

    _putchar('\n');
    return (0);
}
