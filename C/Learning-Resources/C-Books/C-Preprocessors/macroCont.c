/*
 * This is a C file on macro continuation under preprocessor operators
 */

/* A macro usually must be contained on a single line. The macro continuation operator ( / )is used to
 * continue a macro that is too long for a single line.
 * The stringize or number-sign operator '#' , when used within a macro definition, converts a macro
 * parameter into a string constant. This operator may be used only in a macro that has a specified
 * argument or parameter list.
 *
 * srtingize - '#'
 */
/* Example: */

#include <stdio.h>

#define message_for(a, b) \
	printf(#a " and " #b ": We love you!\n")     // 'a' and 'b' are the string literals here ( #a , #b )

int main(void)
{
	message_for(Carole, Debra);
	return (0);
}
