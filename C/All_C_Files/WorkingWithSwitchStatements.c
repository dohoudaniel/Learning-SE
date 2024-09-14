#include <stdio.h>
#include <stdlib.h>

int main()
{
	int Daniel = 16;
	
	switch (Daniel) {
		case 5:
			printf("You are not my age");
			break;
		case 10:
			printf("You are still not my age\n");
			break;
		case 15:
			printf("Hmmmm..... Almost my age!\n");
			break;
		case 16:
			printf("Well, well, well, you are my age now!");
			break;
		case 20:
			printf("You are greater than my age, and yo are oler than me! Respect sir!");
			break;
		//The default keywork is executed if all the cases explicitly declared do not match the value of our variable
		default:
			printf("I can now handle all cases because I used the C Keyword  default  !");
			break;
	}
}
