// This is the practice.c file.
#include <stdio.h>

void Daniel(int i)
{
	do {
		printf("The value of i is %i\n", i);
		i++;
	}
	while ( i < 20);
}

int main()
{
	Daniel(2);
	return (0);
}
