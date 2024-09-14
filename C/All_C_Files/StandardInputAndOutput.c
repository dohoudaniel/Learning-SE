#include <stdio.h>

//Standard Input / Output Demo
#include <stdio.h>

//Standard Input and Output demo
int main(void)
{
        char b,m;
        int year, age;

        printf("Enter your acronyms for your nickname, your current year, and your current age: ");

        scanf("%c %c", &b, &m);
        scanf("%d %d", &year, &age);

        printf("My name is %s and I am %d years old.\n", "Dohou Daniel", age);
        printf("My nickname is Beautiful Mind ??, and the acronym is %c . %c.\n", b, m);
        printf("This program was written on 29th December, %d\n", year);

        return (0);
}
