/* 
 * This file contains an example of use cases for predefined macros in C.
 * The predefined macros in C are:
 * Macro 	Description
 * __DATE__ 	The current date as a character literal in "MMM DD YYYY" format
 * __TIME__ 	The current time as a character literal in "HH:MM:SS" format
 * __FILE__ 	This contains the current filename as a string literal.
 * __LINE__ 	This contains the current line number as a decimal constant.
 * __STDC__ 	Defined as 1 when the compiler complies with the ANSI standard.
 */

/*
 * Name of file: tests.c
 * Use-case: Uses predefined macros in C
 */

#include <stdio.h>

int main()
{
	printf("Name Of File :%s\n", __FILE__);
	printf("Current Date :%s\n", __DATE__);
	printf("Current Time :%s\n", __TIME__);
	printf("Line :%d\n", __LINE__);
	printf("ANSI :%d\n", __STDC__);
}
