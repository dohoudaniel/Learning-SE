/* Revisit this file */
#include <stdio.h>
#include "main.h"

/**
 * main - Prints the sum of even-valued Fibonacci sequence terms not exceeding 4000000.
 * Return: Always 0.
 */
int main(void)
{
    unsigned long f1 = 0;
    unsigned long f2 = 1;
    unsigned long fAll;
    float total;

    while (1)
    {
        fAll = f1 + f2;
        if (fAll > 4000000)
        {
            break;
        }
        if ((fAll % 2) == 0)
        {
            total += fAll;
        }
        f1 = f2;
        f2 = fAll;
    }
    printf("%.0f\n", total);

    return (0);
}
