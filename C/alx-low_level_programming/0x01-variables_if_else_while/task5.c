#include <stdio.h>
/**
 * main - Entry point
 * function main - Prints all single digit numbers
 * Return: Always 0;
*/
int main()
{
    int d;

    for (d = 0; d <= 9; d++)
    {
        printf("%u", d);
    }
    printf("\n");

    return (0);
}
