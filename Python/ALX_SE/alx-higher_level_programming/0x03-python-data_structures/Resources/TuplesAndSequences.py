# Tuples and Sequences

# Tuples are closed by brackets.
# A tuple consists of a number of values separated by commas.
# The statement below is an example of tutle packing. The values are packed into a tuple:
d = (12345, 678910, "A Beautiful Mind")
print(d)
print(d[2])


# Tuples may be nested
rm = d, (11, 12, 13, 14, 15)
print(rm)
print(rm[0])

# Tuples are immutable but they can contain mmutable objects
# Tuples are immutable, and usually contain a heterogeneous sequence of elements or
# indexing (or even by attribute in the case of namedtuples).that are accessed via unpacking.

# A special problem is the construction of tuples containing 0 or 1 items: the syntax has
# Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is
# constructed by following a value with a comma (it is not sufficient to enclose a single
#  value in parentheses). Ugly, but effective. For example: some extra quirks to accommodate these.
bola = ()    # An empty tuple 
singleton = 'hello',  # A tuple with one item followed by a coma, <-- note the comma
print(len(bola))
print(len(singleton))


# The reverse is also the case
x, y, z = mishael
print(mishael)
# This is called, sequence unpacking, and works for any sequence on the right hand.
# Sequence unpacking requires that there are as many variables on the left side of the equals sign
# as there are elements in the sequence. 
# Multiple assignment is really just a combination of tuple packing and sequence unpacking.

