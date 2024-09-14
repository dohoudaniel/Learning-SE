#include <stdio.h>

/**
 * main - Entry point of the program
 * function main - Prints the letters of the alphabet in lowercase except from 'q' and 'e'
 * Return: Always 0
 */
int main(void)
{
    char m;

    for (m = 'a'; m <= 'z'; m++)
    {
        if (m != 'e' && m != 'q')
        {
            putchar(m);
        }
    }

    putchar('\n');

    return (0);
}
