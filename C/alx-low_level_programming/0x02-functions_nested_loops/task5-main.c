#include "main.h"
/**
 * main - check the code.
 *
 * Return: Always 0.
 */

int main(void)
{
    int d;

    d = print_sign(98);
    // Since the argument passed print_sign() is greater than 0, it prints '+', and d stores the
    // return value of 1.
    _putchar(',');
    _putchar(' ');
    _putchar(d + '0'); // The putchar of d(1) + '0'(48) = 1 + 48 = 49. The putchar of 49 is 1.
    _putchar('\n'); // Prints a new line.

    d = print_sign(0);
    // Since the argument passed print_sign() is equal to 0, it prints '0', and d stores the
    // return value of 0.
    _putchar(',');
    _putchar(' ');
    _putchar(d + '0'); // The putchar of d(0) + '0'(48) = 0 + 48 = 48. The putchar of 48 is 0.
    _putchar('\n'); // Prints a new line.

    d = print_sign(0xff);
    /**
     * In C we can represent a hexadecimal value by prefixing it with a "0x". For example "x=0xf;
     * " sets "x" to the decimal value 15 (or the binary value 1111). The statement "x=0xff" 
     * would set x to the binary value "11111111", which is 255 in decimal.
    */
    // Since the argument passed print_sign() is greater than 0, it prints '1', and d stores the
    // return value of 1.
    _putchar(',');
    _putchar(' ');
    _putchar(d + '0'); // The putchar of d(1) + '0'(48) = 1 + 48 = 49. The putchar of 49 is 1.
    _putchar('\n'); // Prints a new line.

    d = print_sign(-1);
    // Since the argument passed print_sign() is less than 0, it prints '-', and d stores the
    // return value of -1.
    _putchar(',');
    _putchar(' ');
    _putchar(d + '0'); // The putchar of d(-11) + '0'(48) = -1 + 48 = 47. The putchar of 47 is '/' .

    _putchar('\n'); // Prints a new line.
    return (0);
}
