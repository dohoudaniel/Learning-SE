#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/*
 * doHardThings() - A function that takes in numbers from standard input and prints them on the screen.
 * val - a variable that stores values from standard input
 */
void doHardThings()
{
	int val;
	printf("Enter any integer: ");
	scanf("%u", &val);
	printf("\'val\' is of value %u\n", val);
	
	int squareVal = val * val;
	printf("The value of the square of \'val\' is %u\n", squareVal);
}



/* 
 * main() - The entry point of any c program
 */
int main()
{
	doHardThings();
	return(0);
}
