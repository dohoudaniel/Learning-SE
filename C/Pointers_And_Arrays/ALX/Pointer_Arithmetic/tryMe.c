#include <stdio.h>

/**
 * main - Solve me.
 *
 * Return: Always 0.
 */
int main(void)
{
	int a[5];
	int *p;
	int *p2;

	*a = 98;
	printf("*a = %d\n\n", *a);

	*(a + 1) = 198;
	printf("*(a + 1) = %d\n\n", *a);

	*(a + 2) = 298;
	printf("*(a + 2) = %d\n\n", *(a + 2));

	a[3] = 398;
	printf("*a[3] = %d\n", a[3]);
	printf("*(a + 2) = %d\n\n", *(a + 3));

	*(a + 4) = 498;
	printf("*(a + 4) = %d\n\n", *(a + 4));

	p = a + 1;
	printf("The value of p is %p\n", p);
	/* printf("The value of p is %p\n\n", &p); */

	*p = 98;
	printf("The value of *p is %d\n\n", *p);

	p2 = a + 3;
	printf("The value of p2 is %p\n\n", p2);

	*p2 = *p + 1337;
	printf("The value of *p2 is %d\n\n", *p2);

	return (0);
}
