# Defining a list
squares = [1, 2, 3, 4]

# Printing a list
print(squares)

# Printing using indexes
print(squares[2])

# Printing using indexes
print(squares[1:])

# Adding two lists
MyList = [36, 49, 64, 81, 100]
squares = squares + MyList
print(squares)

# Concatenation
squares = squares + [36, 49, 64, 81, 100]
# print(squares)
# print(squares[:])

# Updating a list
squares[3] = 7
print(squares)

# You can also add new items at the end of the list, by using the append() method (we will see more about methods later)
squares.append(144)
print(squares)

# Updating a list using indexes
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)

# Using the len() function on lists
print(len(squares))
print(len(letters))

# Nesting Lists
dan = [squares, letters]
print(dan)

