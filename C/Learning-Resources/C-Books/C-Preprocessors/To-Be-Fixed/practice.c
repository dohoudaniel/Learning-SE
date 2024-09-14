// Practice file on parameterizing Macros
/*
 * One of the powerful functions of the CPP is the ability to simulate functions using parameterized
 * macros.
 */
/*
 * Macros with arguments must be defined using the #define directive before they can be used. The
 * argument list is enclosed in parentheses and must immediately follow the macro name. Spaces
 * are not allowed between and macro name and open parenthesis.
 */

#include <stdio.h>

#define DAN(x, y)
#if x > y printf("The product of x and y is %u\n", x * y)
#elif x == y printf("The value of x is %u\n", x)
#elif x < y printf("The difference between x and y is %u\n", y - x)
#else printf("Breautiful Mind")
#endif

/*
 * This program uses if and else statements to print values of numbers
 */
int main(void)
{
	DAN(10, 20);
	return (0);
}
