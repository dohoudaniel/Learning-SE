# Array Type Decay
When the name of an array is used in an expression, the array type gets automatically implicitly converted to pointer-to-element type in almost all contexts. The resultant pointer is a completely independent temporary value, that is the address of the first element of the array.

However, there are two exceptions to this:
- When the array name is an operand of sizeof or unary '&' (address-of), the name of the array then refers to the array object itself. 

# Auto Implicit Conversion
Implicit type conversion in C language is the conversion of one data type into another datatype by the compiler during the execution of the program. It is also called automatic type conversion.
