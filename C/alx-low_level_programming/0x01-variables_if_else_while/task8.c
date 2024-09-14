#include <stdio.h>
/**
 * main - Entry point of the program
 * Function main - Prints the lowercase alphabet in reverse, followed by a new line
 * Return: Always 0
*/
int main(void)
{
    char m;
    char f;

    for (m = '0'; m <= '9'; m++)
    {
        putchar(m);
    }

    for (f = 'a'; f <= 'f'; f++)
    {
        putchar(f);
    }

    putchar('\n');
    return (0);
}
