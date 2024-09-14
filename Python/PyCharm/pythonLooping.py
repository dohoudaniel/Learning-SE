import sys
# name = "Daniel"
# print("Welcome to Pycharm, ", name)

"""
for i in [2,4,6,8,10]:
    print("i = ", i)     # Output is : i = 2, i = 4, i = 6, i = 8, i = 10
"""

"""
for b in range(10):
    print("b = ", b)     # Output is: b = 0, b =1, b = 2, b = 3, b = 4, b = 5, b = 6, b = 7, b = 8, b = 9
    # It does not include 10
"""

"""for a in range(2, 10):
    print("a = ", a)     # This prints 2 to 9
"""

# We use moduluds to know if a number is even or odd
# Modulus returns the remainder
# i = 2
# print((i % 2) == 0)      # Returns True

"""
Program to print odd numbers:

for i in range(1, 21):
    if ((i % 2) != 0):
        print("i = ", i)
"""


# Problem 1:
your_float = input("Enter a float: ")
your_float = float(your_float)
# Rounding up a float to 2 decimal places... ({:.2f})
print("Your float rounded to 2 decimal places is: {:.2f}".format(your_float))




# Problem 2:
# Have the user enter their investment amount and expected interest
# Each year, their investment will increase by their investment + their investment * interest rate is
# Print out the earnings after a 10 year period

# Ask for the money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("What is your desired interest rate? -> ")
# Convert the values to a float
money = float(money)
# Convert the values to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * 0.01
# Cycle through 10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)
# Output the results
print("Investment done after 10 years: {:.2f}".format(money))


"""
Floating Numbers in Python are not necessarily precise
i = 0.1 + 0.1 + 0.1 - 0.3
print(i)
"""

