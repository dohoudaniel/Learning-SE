/* This file explains defined operators in C */
/*
 * The preprocessor defined operator is used in constant expressions to determine if an identifier is
 * defined using #define. If the specified identifier is defined, the value is true non − zero. If the symbol
 * is not defined, the value is false zero.
 */
// Example:
#include <stdio.h>

#if !defined (DANIEL)
#define DANIEL "Beautiful Mind!"
#endif

int main(void)
{
	printf("I am a %s\n", DANIEL);
	return (0);
}
