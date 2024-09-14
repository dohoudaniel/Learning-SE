#include <stdio.h>
/**
 * main - Entry point of the program
 * function main - Prints all possible combinations of single-digit numbers.
 * Return: Always 0.
 */
int main()
{
    int dan;

    for (dan = 48; dan <= 57; dan++)
    // ASCII code for '0' is 48
    // ASCII code for '0' is 48
    {
        putchar(dan);    //putchar(dan) converts dan to an ASCII character and prints from '0' to '9' as specified in the for-loop.
        if (dan  != 57)
        {
            putchar(',');
            putchar(' ');
        }
    }
    putchar('\n');
    return (0);
}
