/* This program uses looping to print the factorial of 10 or less than 10 numbers */
/* Name: 10-or-less-digit-multiplier */

#include <stdio.h>
int main(void)
{
	int answer = 1;
	int i;

	for(i = 2; i <= 10; i++)
	{
		answer = answer * 1;
		//answer++;
	}
	printf("Answer = %d.\n", answer);

	return (0);
}
