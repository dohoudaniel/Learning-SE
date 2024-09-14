/* Credit -> The C Handbook */
DISCLAIMER: This file deserves none of my credit.

The ternary operator
--------------------
The ternary operator is the only operator in C that works with 3 operands,
and it’s a short way to express conditionals.
This is how it looks:
<condition> ? <expression> : <expression>
Example:
a ? b : c
If a is evaluated to true , then the b statement is executed, otherwise c
is.
The ternary operator is functionality-wise same as an if/else conditional,
except it is shorter to express and it can be inlined into an expression.
