#include <stdio.h>
/**
 * Demonstration of an initialized read-only area of the data segment.
 */

char *Str= "Amlendra Kumar";

int main(void)
{
	Str[0]='k';

	printf("%s\n",Str); /* Returns 'Segmentation Fault' */

	return 0;
}

/**
 * In the above example, we are not able to change the array character is because it is a literal string.
 * A constant string does not only go in the data section but all types of const global data go in that section.
 * It is not necessarily that const global and constant string go in the data section.
 * It can be also in the text section of the program (normally the .rodata segment),
 * as it is normally not modifiable by a program.
 */
