#include <stdio.h>
#include <unistd.h>

int main()
{
    int a, b, c;

    for (a = '0'; a <= '9'; a++)
    {
        for (b = '0'; b <= '9'; b++)
        {
            for (c = '0'; c <= '9'; c++)
            {
                if (a < b && b < c)
                {
                    putchar(a);
                    putchar(b);
                    putchar(c);
                    if (a != '7')
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
}
//if a < b
//if a < c
//if b < c &&
