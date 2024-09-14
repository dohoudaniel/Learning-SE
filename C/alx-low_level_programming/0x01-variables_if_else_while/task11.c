#include <stdio.h>
/**
 * main - entry point
 *function main - Prints a combination of three digits
 *Return: 0
 */
int main(void)
{
    int a, b, c;

    for (a = 0; a <= 9; a++)
    {
        for (b = 0; b <= 9; b++)
        {
            for (c = 0; c <= 9; c++)
            {
                if (c > b && b > a)      // Standard output starts from here when all conditions of this loop are satisfied
                {
                    putchar(a + '0');
                    putchar(b + '0');
                    putchar(c + '0');

                    if (a != 7 || b != 8 || c != 9)
                    {
                        putchar(',');
                        putchar(' ');
                    }
                }
            }
        }
    }

    putchar('\n');
    return (0);

    /**
     * Just like the way putchar() worked in the other place, it works also the same way here
     * But the standard output is printed based on the if-loop on line 17, only if the statements are satisfied i.e c > b AND b > a
    */
}
