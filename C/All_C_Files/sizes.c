#include <stdio.h>

int main(void)
{
        int i;
        double d;
        char c;

        //This is a typical example of typecasting
        printf("The size of an int is: %lu\n", (unsigned long)sizeof(i));
        printf("The size of a double is: %lu\n", (unsigned long)sizeof(d));
        printf("The asie of a character is: %lu\n", (unsigned long)sizeof(c));

        return (0);
}
