// This file is the ALX SE Prototype and version of the general putchar() C function
#include <unistd.h>
/**
 * _putchar - writes the character to stdout
 * @c: The character to print to stdout
 * 
 * Return: On success, 1
 * On error, -1 is returned and errno is set appropriately
*/

int _putchar(char c)
{
    return (write(1, &c, 1));
    // To call the write() function in c, you must include the 'unistd.h' header file.
    // The unistd.h header file provides the write() function in UNIX-like systems. 
}
