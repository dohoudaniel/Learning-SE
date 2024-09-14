#include <stdio.h>
#include "main.h"
/**
 * print_to_98 - Prints the numbers entered up to 98
 *
 * Return: The numbers to be printed
 */
void print_to_98(int n)
{
    if (n <= 98)
    {
        for (; n <= 98; n++)
        {
            if (n == 98)
            {
                printf("%d", n);
                printf("\n");
                break; // This was added because of the post increment (n++)
            }
            else
            {
                printf("%d, ", n);
            }
        }
    }
    else
    {
        for (; n >= 98; n--)
        {
            if (n == 98)
            {
                printf("%d", n);
                printf("\n");
                break; // This is because of the post increment (n++)
            }
            else
            {
                printf("%d, ", n);
            }
        }
    }
}
// To be continued
