#include <stdio.h>
/**
 * main - Entry point of the program
 * Function main - Prints the lowercase alphabet in reverse, followed by a new line
 * Return: Always 0
*/
int main(void)
{
    char f;

    for (f = 'z'; f >= 'a'; f--)
    {
        putchar(f);
    }
    putchar('\n');
    return (0);
}
