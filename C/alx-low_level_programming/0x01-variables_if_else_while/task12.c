#include <stdio.h>
/**
 * main - Entry point of the program
 * Function main - Prints all possible combinations of two two-digit numbers.
 * Return: Always 0.
*/
int main(void)
{
    int a, b, c, d;

    //Note that the putchar() function, and thus, the ASCII Values, are used in this loop. 48 has a value of 0 and 57 has an ASCII value of 9
    for (a = 48; a <= 57; a++)
    {
        for (b = 48; b <= 57; b++)
        {
            for (c = 48; c <= 57; c++)
            {
                for (d = 48; d <= 57; d++)
                {
                    if (((c + d) > (a + b) && c >= a) || a < c)
                    {
                        putchar(a);
                        putchar(b);
                        putchar(' ');
                        putchar(c);
                        putchar(d);

                        if (a + b + c + d == 227 && a == 57)
                        {
                            break;
                        }
                        else 
                        {
                            putchar(',');
                            putchar(' ');
                        }
                    }
                }
            }
        }
    }

    putchar('\n');

    return (0);
}
