#include <stdio.h>
/**
 *  main - Entry point of a c program
 *  function main - Prints all single digit numbers of base 10 starting from 0
 *  Return: Always 0.
*/
int main(void)
{
    char g;

    for (g = '0'; g <= '9'; g++)
    {
        putchar(g);
    }
    putchar('\n');

    return (0);
}
