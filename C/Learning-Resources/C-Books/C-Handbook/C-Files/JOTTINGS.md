1. Naming of variables really matter.
2. Arrays indexes start from 0, so an array of 5 items, like the prices array above, will have items ranging from 0 to 4.
3. Elements in an array are stored sequentially, one right after the other.
4. The variable name of an array (e.g 'prices' like above) is a pointer to the first element of the array, and can also be used as a normal pointer.
5. In strings (check the srings.c file), for the example used, 'Beautiful Mind' is 14 chars long, but we define the array (Daniel) as 15 characters. This is because the last character in a string MUST be a 0 value (the string terminator), and we must make space for it. This is EXTREMELY important especially when we are manipulating strings.
6. The name of a declared array is a pointer to the first item of the array.
