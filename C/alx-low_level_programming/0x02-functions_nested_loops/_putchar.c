/*
 *  This file is the ALX SE Prototype and version of the general putchar() C function
 */
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
    /*
     * To call the write() function in c, you must include the 'unistd.h' header file.
     * The unistd.h header file provides the write() function in UNIX-like systems.
     */
}

/**
 *
 * Explanation of the _putchar() function:
 * ---------------------------------------
 * # Geeks for Geeks
 * ----------------
 * The _putchar(int char) method in C is used to write a character, of unsigned char type,
 *  to stdout. This character (c) is passed as the parameter to this method.
 *                 int _putchar(char c)
 *
 * Parameters: This method accepts a mandatory parameter char which is the character to be
 * written to stdout.
 * Return Value: This function returns the character written on the stdout as an unsigned char.
 *  It also returns EOF when some error occurs.
 * The putchar function is specified in the C standard library header file stdio.h.
 * 
 *
 * # Tutorials Point
 * -----------------
 * The C library function int putchar(int char) writes a character (an unsigned char) specified
 *  by the argument char to stdout.
 *                  int _putchar(char c)
 * Parameters: c − This is the character to be written. This is passed as its int promotion.
 * Return Value: This function returns the character written as an unsigned char cast to an int or EOF on error.
 * The putchar function is specified in the C standard library header file stdio.h.
 */
