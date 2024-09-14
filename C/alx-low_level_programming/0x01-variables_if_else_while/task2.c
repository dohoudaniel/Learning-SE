#include <stdio.h>
/**
 * main - Entry point of the program
 * function main - Lists all letters of the alphabet
 * j  - a character variable
 * Return: Always 0
*/
int main(void)
{
    char j;

    for (j = 'a'; j <= 'z'; j++)
    {
        putchar(j);
    }

    putchar('\n');
    return(0);
}
