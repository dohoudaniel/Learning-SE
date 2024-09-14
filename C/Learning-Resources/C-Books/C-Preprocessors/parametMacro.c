// Parameterizing Macros
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

#define DAN(x, y) ((x) > (y) ? (x * y) : (y - x))

/*
 * This program uses if and else statements to print values of numbers
 */
int main(void)
{
	printf("The calculation between X and Y is %u\n", DAN(10, 20));
	return (0);
}
