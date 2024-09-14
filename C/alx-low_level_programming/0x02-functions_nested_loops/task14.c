/* Revisit this file */
#include <stdio.h>
#include "main.h"

/**
 * main - Prints the  first 50 Fibonacci numbers, starting with 1 and 2, seperated by a comma, followed by a space 
 * Return: Always 0.
*/
int main(void)
{
    int a;
    unsigned long b = 0;
    unsigned long c = 1;
    unsigned long d;

    for (a = 0; a < 50; a++)
    {
        d = b + c;
        printf("%lu", d);

        b = c;
        c = d;

        if (a == 49)
        {
            printf("\n");
        }
        else
        {
            printf(", ");
        }
    }

    return (0);
}
