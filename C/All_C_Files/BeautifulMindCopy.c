// Test file for question 1
// Question: Write a program in which to declare all data type like integer ,double,float,long int and print value in specified format:

#include <stdio.h>
// #include <conio.h>

void main()
{
        int a;
        double b;
        float c;
        long int d;

        printf("Enter the values of a, b, c and d: \n");
        scanf("%d %lf %f %ld", &a, &b, &c, &d);

        printf("The value of a = %d, b = %lf, c = %f, d = %ld.\n", a, b, c, d);
        // getc();
}
