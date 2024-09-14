/* I Wrote This Code Myself 👨‍💻🎧🤍😎 */
/* Thank You, Jehovah. */
/* I made some changes here, because it is a Linux Environment */
/* TODO: Find out why! */

#include "main.h"
#include <stdio.h>

/**
 * main - prints the numbers from 1 to 100, followed by a new line.
 * For multiples of: 3 - it prints 'Fizz'
 *                   5 - it prints 'Buzz'
 *                   15 - it prints 'FizzBuzz'
 * Return: Always 0.
 */
int main(void)
{
    int a;

    for (a = 1; a <= 100; a++)
    {
        if (a % 3 == 0)
        {
            printf("Fizz ");
        }
        else if (a % 5 == 0)
        {
            printf("Buzz ");
        }
        else if (a % 15 == 0)
        {
            printf("FizzBuzz ");
        }
        else
        {
            printf("%d ", a);
        }

        /* _putchar(' '); */
    }
    /* _putchar('\n'); */
    printf("\n");

    return (0);
}
