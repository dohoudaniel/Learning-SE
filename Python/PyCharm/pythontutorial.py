import sys
print (sys.version_info)

# - This is how you write a comment in Python
"""
This is how you write a
multiline comment in
Python
"""



# Ask the user to input their name and assign it to a variable named 'name'
# - Create the variable name
name = input('What is your name? -> ')  # - Display message is 'What is your name?'

# Print out 'Hello' followed by the name entererd by the user
print('Hello ', name)




"""
You cannot use any of the following for variable names, because they are keywords/commands in Python:
and    del    from    not     while     as     elif      global     or      with     lambda
assert     else     if      pass    yield    break      except    import     print     try
class     exec    in     raise    continue     finally    is    return    def    for    any
"""



# Ask the user to input 2 values and store them in variables num1 & num2
num1, num2 = input('Enter 2 numbers: ').split()
# split.() seperates the values of the input if there is whitespace found between the inputs

# Typecasting the values entered as by the users to regular numbers (Integers)
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store them in a variable named 'sum'
sum = num1 + num2

# Subtract and store values in a variable called 'difference'
difference = num1 - num2

# Multiply the values and store them in a variable 'product'
product = num1 * num2

# Divide the values and store them in a variable 'quotient'
quotient = num1 / num2

# Use modulus on the values to find the remainders and assign it to a var 'remainder'
remainder = num1 % num2

# Print the results on the screen :)
# To print the results on the screen, you need to format the output using the .format()
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))





# Problem: Receive miles and convert to kilometres
# kilometres = miles * 1.60934
# Message is: 'Enter Miles: ' -> 5
# '5 miles = x kilometres'

# Ask the user to input a value and assign it to the variable 'miles'
miles = input("Enter the number in miles: ")

# Convert the value from string to integer
miles = int(miles)

# Perform the calculation by multiplying miles by 1.60934 and store it in a variable 'kilometres'
kilometres = miles * 1.60934

# Print the result on the screen
print("1 kilometre = 1.60934 miles")
print("{} miles = {} kilometres".format(miles, kilometres))




# A program that functions liks a calculator
# Message: 'Enter Calculation: 5 * 6
# 5 * 6 = 30

# Store the user input of 2 nubers and the operator
num1, operator, num2 = input('Enter Calculation: ').split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# if operand is '+', then we need to provide output based on addition.... and so on for other operators
# Print the result
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    # elif -> else + if
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Use either +, -, *, / or % next time.")




# We will provide different outputs based on age
# 1 to 10 -> 'Important'
# 21, 50, >65 -> 'Important'
# All others - Not important

# Receive age and store in a variable called 'age'
age = eval((input("Enter Age: ")))
# eval() automatically converts a string to an integer

# and -> Returns true if both conditions are true
# or -> Returns true if either condition is true
# not -> Convert a tue condition to a false

# if age is both greater than or equal to 1 and less than or equal to 18 -> Important
if (age >= 1) and (age <= 18):
    print("This is an important timeline")

# if age is either 21 or 50 ->  Important
elif (age == 21) or (age == 50):
    print("This is also an important timeline")

# check if age is less than 65 and then convert true to false
elif not (age < 65):
    # not converts true into false anf false into true
    print("This is also an imporant timeline")

# Else All others -> Not Important
else:
    print("This timeline is not important")



# Challenge:
# if age is 5 -> Go to Kindergarten
# Age 6 to 17 goes to grade 1 to 12
# if age is greater than 17, go to college
# Complete with 10 or less lines

# - My Answer
age = eval((input("Enter Age: ")))
if (age < 5):
    print("You're too young to go to school")
if (age == 5):
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):     # Same as: elif (5 < age <= 17):
    print("Go to grade 1 to 12")
elif (age > 17):
    print("Go to college")



# Solution to challenge:
# if age is 5 -> Go to Kindergarten
# Age 6 to 17 goes to grade 1 to 12
# if age is greater than 17, go to college
# Complete with 10 or less lines

# Ask for the age
age = eval(input("Enter Age: "))

# Handle if age < 5
if (age < 5):
    print("You're too young for school")
# Special Output for age 5
elif (age == 5):
    print("Go to Kindergarten")
# Since a number is the result of ages 6 to 17, we can check them all with a condition
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
# Handle everything else
else:
    print("Go to College")

