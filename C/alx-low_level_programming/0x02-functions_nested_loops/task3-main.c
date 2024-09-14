#include "main.h"
/**
 * main - Check the code.
 * 
 * Return: Always 0.
 */
int main(void)
{
    int r;

    r = _islower('H');  // The return value for the ASCII Value of 'H' is stored in r
    _putchar(r + '0');
    // r has a value of 0 (from task3.c) and r (0) plus '0' (48, from the table) is equal to 48.
    // The putchar of 48 is 0. So, output is 0.

    r = _islower('o');  // The return value for the ASCII Value of 'o' is stored in r
    _putchar(r + '0');
    // r has a value of 1 (from task3.c) and r (1) plus '0' (48, from the table) is equal to 49.
    // The putchar of 49 is 1. So, output is 1.

    r = _islower(108);  // The return value for the ASCII Value of r here is 1 because 108 > 97 && 108 < 122
    _putchar(r + '0');
    // r has a value of 1 (from task3.c) and r (1) plus '0' (48, from the table) is equal to 49.
    // The putchar of 49 is 1. So, output is 1.
    
    _putchar('\n');
    return (0);
}
