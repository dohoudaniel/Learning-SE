/*
 * Question 2 - Write a program to calculate simple interest
 */

/*
 * main - Entry point of the program
 */
#include <stdio.h>
int main()
{
	int P, R, T;
	float SI;

	printf("Calculate your Simple Interest 😁.\nPlease note that Time given should be in years.\n");
	printf("Enter the following values as stated: Principal, then Rate, then Time: ");

	scanf("%u %u %u", &P, &R, &T);

	SI = ((float)(P * R * T) / 100);
	printf("Your Simple Interest, with a principal of %d, a rate of %u and a time of %u years is %f.\n", P, R, T, SI);

	printf("Recompile to try again.\nThank you 👨‍💻🎧.\n");
}
