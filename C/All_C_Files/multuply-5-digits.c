/*
 * This C Program multiplies any number inputted into standard input.
 * Name: 5-digit-multiplier
*/

#include <stdio.h>

int main(void)
{
    int a, b, c, d, e;
    
	printf("Welcome to the 5-digit-Multiplier ??.");
    printf("Enter the 5 digits you wish: ");
    scanf("%i %i %i %i %i", &a, &b, &c, &d, &e);
	
	int answer = a * b * c * d * e;
    printf("The product of all the numbers you entered is: %i\n", answer);
	
	printf("Try again. Recompile to start the calculator again.\n");
}
