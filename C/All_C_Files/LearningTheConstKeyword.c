#include <stdio.h>

int main()
{
	int i = 4, j = 10, k = 16;
	const int *ip = &i;
	ip = j;
	
	return (0);
}
