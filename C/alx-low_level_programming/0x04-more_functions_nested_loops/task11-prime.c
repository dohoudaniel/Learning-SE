/*  */

#include <stdio.h>

/**
 * Asqrt - finds the square root
 * @x: inputted number
 * Return: Square root of x
 */
double Asqrt(double x)
{
    float sqrt, tmp;

    sqrt = x / 2;
    tmp = 0;

    while (sqrt != tmp)
    {
        tmp = sqrt;
        sqrt = ((x / tmp) + tmp) / 2;
    }
    return (sqrt);
}

/**
 * largest_prime_factor - finds and prints the largest prime factor of a number (num)
 * @num: The number to find
 * Return: Nothing.
 */
void largest_prime_factor(long int num)
{
    int prmNum, largest;

    /* First, divide the smallest number by two */
    while (num % 2 == 0)
    {
        num = num / 2;
    }

    /* num must be odd so we proceed to the next prime number (plus two) */
    for (prmNum = 3; prmNum <= Asqrt(num); prmNum += 2)
    {
        while (num % prmNum == 0)
        {
            num = num / prmNum;
            largest = prmNum;
        }
    }

    if (num > 2)
    {
        largest = num;
    }
    printf("%d\n", largest);
}

/**
 * main - Entry point
 * Return: Always 0 (Success).
*/
int main(void)
{
    largest_prime_factor(612852475143);

    return (0);
}
