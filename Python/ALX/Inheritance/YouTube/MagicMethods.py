#!/usr/bin/python3

# Link: https://www.youtube.com/watch?v=d8kCdLCi6Lk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=42
"""
# Magic Methods
# __eq__ equals
# __ne__ not equal
# __lt__ less than
# __gt__ greater than
# __le__ less than or equal
# __ge__ greater than or equal
# __add__ addition
# __sub__ subtraction
# __mul__ multiplication
# __div__ division
# __mod__ modulus
# __pow__ exponential
# __str__ converts object to string
# __len__ length
# __getitem__ indexing
# __setitem__ assigning to indexed values
# __delitem__ deleting indexed values
# __iter__ iteration over objects (e.g., in for loops)
# __contains__ check if item contained
# __call__ call object as a function
# __int__ convert to integer
# __float__ convert to float
# __bool__ convert to boolean
# __repr__ used to print the object
# __doc__ used to print the docstring of an object (if it exists)
"""

class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()
        # Add the seconds and correct if sum > 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second
        # Add the minutes and correct if sum > 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute
        # Add the hours and correct if sum > 24
        if (self.hour + other_time.hour) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour
        return new_time

def main():
    time1 = Time(1, 20, 30)
    print(time1)
    print()

    time2 = Time(24, 41, 30)
    print(time1 + time2)
    print(time1.__add__(time2))
    print()

main()
