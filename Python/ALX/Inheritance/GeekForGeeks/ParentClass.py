#!/usr/bin/python3

# A Python program to demonstrate inheritance.
class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)

# Driver Code
emp = Person("Daniel", 17) # An object of a person
emp.Display()
