#include <stdio.h>
#include <stdlib.h>

int main()
{
	int D = 100;
	
	if (D < 20) {
		printf("You are less than 100\n");
	} else if (D <= 30) {
		printf("You are still less than 100\n");
	} else if (D == 40) {
		printf("Try harder, you are now greater then 40\n");
	} else if (D == 50) {
		printf("Keep pushing! Almost there!!\n");
	} else {
		printf("Well-done. You are now equal to 100\n");
	}
}
