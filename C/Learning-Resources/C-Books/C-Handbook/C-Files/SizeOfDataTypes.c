#include <stdio.h>

//This program, when compiled prints the size of data types in C
int main(void)
{
	printf("The size of an Integer is %lu\n", sizeof(int));
	printf("The size of a Character is %lu\n", sizeof(char));
	printf("The size of a Float is %lu\n",sizeof(float));
	printf("The size of a Double is %lu\n",sizeof(double));
	printf("The size of a Short Int is %lu\n",sizeof(short int));
	printf("The size of a Unsigned Int is %lu\n",sizeof(unsigned int));
	printf("The size of a Long Int is %lu\n",sizeof(long int));
	printf("The size of a Long Long Int is %lu\n",sizeof(long long int));
	printf("The size of a Unsigned Long Int is %lu\n",sizeof(unsigned long int));
	printf("The size of a Unsigned Long Long Int is %lu\n",sizeof(unsigned long long int));
	printf("The size of a Signed Char is %lu\n",sizeof(signed char));
	printf("The size of a Unsigned Char is %lu\n",sizeof(unsigned char));
	printf("The size of a Long Double is %lu\n",sizeof(long double));
	printf("The size of an Unsigned is %lu\n",sizeof(unsigned));
	printf("The size of a Signed is %lu\n",sizeof(signed));
	printf("The size of a Signed Int is %lu\n",sizeof(signed int));
}

/*
Output:
The size of an Integer is 4
The size of a Character is 1
The size of a Float is 4
The size of a Double is 8
The size of a Short Int is 2
The size of a Unsigned Int is 4
The size of a Long Int is 4
The size of a Long Long Int is 8
The size of a Unsigned Long Int is 4
The size of a Unsigned Long Long Int is 8
The size of a Signed Char is 1
The size of a Unsigned Char is 1
The size of a Long Double is 16
The size of an Unsigned is 4
The size of a Signed is 4
The size of a Signed Int is 4
*/
