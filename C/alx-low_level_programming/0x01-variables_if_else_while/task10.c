#include <stdio.h>
/**
 *  main - Entry point
 *  function main - Prints all possible different combinations of two digits.
 * Return: Always 0.
*/
int main(void)
{
    int a, b;
    
    for (a = 10; a <= 19; a++)          // This for-loop for a will run 9(the range of a)
    {
        for (b = 10; b <= 19; b++)      //This for-loop for b will run 9(the range of b) times for one value of a
        {
            if ((b % 10) > (a % 10))
            {
                putchar((a % 10) + '0');     
                putchar((b % 10) + '0');

                if (a != 18 || b != 19)
                {
                    putchar(',');
                    putchar(' ');
                }
            }
            /*
                Explanation on the loop and the putchar()
                When a = 0, b will run through the loop 9 times (from 11 to 19)
                so, when b = 11, and a = 10,
                (a % 10) = 10 % 10 = '0', and '0' + '0' is '0'. The putchar value from the ASCII table for '0' is 48, so it will print the value of 48
                    from th ASCII Table, which is 0.
                (b % 10) = 11 % 10 = '1', and '1' + '0' is '1'. The putchar value from the ASCII table for '1' is 49, so it will print the value of 49
                    from the ASCII Table, which is 1.
                So, it will print 0, and since a != 18 and b != 19 yet, it will print ',' and ' '.

                This loop will happen with b being 11 till 19 for every value of a(10, 11, 12, 13, 14, 15, 16, 17 and 18)

                Thank you Astro
                */
        }
    }
    putchar('\n');
    return (0);
}
