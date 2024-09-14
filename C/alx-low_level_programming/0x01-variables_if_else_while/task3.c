#include <stdio.h>
/**
 * main - Entry point of the program
 * Function main - Prints all letters of the alphabet in lowercase and then in uppercase
 * Return: Always o
 */

int main(void)
{
    char k;

    for (k = 'a'; k <= 'z'; k++)
    {
        putchar(k);
    }

    for (k = 'A'; k <= 'Z'; k++)
    {
        putchar(k);
    }
    putchar('\n');

    return (0);
}
