#include <stdio.h>
#include <unistd.h>

int main()
{
    int a, b;
    for (a = '0'; a <= '9'; a++)
    {  
        for (b = '0'; b <= '9'; b++)
        {
            if (a <= b)
            {
                putchar (a);
                putchar (b);
                
                if (a != '9')
                {
                    putchar (',');
                    putchar (' ');
                }
            }
        }
    }
    putchar('\n');
    
    return (0);
}
