# List Comprehensions
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
# List comprehensions provide a concise way to create lists. Common applications are to make new
# lists where each element is the result of some operations applied to each member of another
# sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
daniel = []
for d in range(11):
    daniel.append(d ** 2)
print(daniel)  # d contains the squares of numbers in the range from 0 to 10 (11 chars)


# Note that this creates (or overwrites) a variable named x that still exists after the
# loop completes. We can calculate the list of squares without any side effects using:
man = list(map(lambda x: x ** 2, range(11)))
print(man)
# Or equivalently,
mane = [y ** 2 for y in range(11)]  # Ihis is more concise and readable.
print(mane)


# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating
# the expression in the context of the for and if clauses which follow it. For example, this
# listcomp combines the elements of two lists if they are not equal:
pin = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6] if a != b]
print(pin)
# This is an equivalent too
comb = []
for r in [1, 2, 3]:
    for s in [4, 5, 6]:
        if r != s:
            comb.append((r, s))
            # print(comb)
print(comb)


# List comprehensions can contain complex expressions and nested functions:
from math import pi
panda = [str(round(pi, i)) for i in range(1, 6)]
print(panda)
# TODO: Find the work of round() here



# Nested List Comprehensions:
# ---------------------------
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
# The following list comprehension will transpose rows and columns:
humn = [[row[l] for row in matrix] for l in range(4)]
print(humn)
# TODO: Find out how the row


# As we saw in the previous section, the inner list comprehension is evaluated in the context
# of the for that follows it, so this example is equivalent to:
transpose = []
for m in range(4):
    transpose.append([row[m] for row in matrix])
    print(transpose)
# Which, in turn, is the same as:
transposed = []
for g in range(4):
    # the following 3 lines implement the nested list comprehensions
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[g])
    transposed.append(transposed_row)
print(transposed)

# In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a great job for this use case:
pal = list(zip(matrix))
print(pal)
pals = list(zip(*matrix))
print(pals)

# The del statement
# There is a way to remove an item from a list given its index instead of its value:
# the del statement. This differs from the pop() method which returns a value. The del
# statement can also be used to remove slices from a list or clear the entire list
# (which we did earlier by assignment of an empty list to the slice). Example:
r = [-1, -2, -3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del r[0]
print(r)
del r[0]
print(r)
del r[0]
print(r)
# The del can also be used to delete entire variables
del r
print(r)
# Referencing the name a hereafter is an error (at least until another value is assigned to it). 

