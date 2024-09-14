/* Just like static variables in C, we also have static arrays in C */

#include <stdio.h>

int main(void)
{
	/* This is how static arrays are definec */
	static int classes[20];
	classes[0]++;
	return classes[0];
}
