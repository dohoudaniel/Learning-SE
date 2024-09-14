"""
YouTube Video: Python Classes and Objects || Python Tutorial || Learn Python Programming
Link: https://www.youtube.com/watch?v=apACNr7DC_s
"""
class User:
    pass

# user1 is an instance of the class, and also an object of the class
user1 = User()
user1.first_name = "Dave"
user1.last_name = "Bowman"
# Since first_name and last_name are attached to the object, we call them fields
print(user1.first_name)    # Syntax: NameOfTheObject.NameOfTheField
# Do not capitalize the name of fields, and if you use more than more word for a field name, seperate the words by underscores
print(user1.last_name)

# Creating stand-alone variables
first_name = "Arthur"
last_name = "Clark"
print(first_name, last_name)

print(user1.first_name, user1.last_name)
# The output is different
# The variables hold a different value from the class object variables even though they are the same name.

# Creating another user
user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

# We will print the three names seperate to show that they belong to different objects
# Daniel: This works because there are different objects and instances.
print(user1.first_name, user1.last_name)
print(first_name, last_name)
print(user2.first_name, user2.last_name)

""" Classes are used to make objects, and these onjects can store different values for the same variable name """

# You can attach additional fields to the same objects and they do not have to be strings.
user1.age = 37
user1.favourite_book = "How To Have A Beautiful Mind"
print(user1.age)
# print(user2.age) # This returns an attribute error


""" Let's turn our simple class into a data powerhouse """
# A function inside a class is called a Method
# init is short for initialization. Some languages call the initialization methods, 'Constructors'
import datetime
class Users:
    # Let's add a helper text: A Docstring
    """A member of Friendface. For now we are
    only storing their names and birthdays.
    But soon we will store an uncomfortable
    amount of user information.
    """
    
    # The init method is called everytime you create a new instance of the class.
    def __init__(self, full_name, birthday):
        """ This method is called everytime you create the instance of a class. """
        self.name = full_name
        self.birthday = birthday     # yy/mm/dd format
        # Be careful. The birthday value provided (2nd statement of birthday in the line above is the value provided when you create
        # a Users object, but the 'birthday' in 'self.birthday' is the field that stores the value. Apply appropriately to others.

        #Extract the first and last names
        name_pieces = full_name.split(" ")
        # We called the split method on the full_name and passed in a space. This will chop the ame into pieces by cutting it whenever it encounters a space.
        # The pieces will be stored in an array.
        self.first_name = name_pieces[0]
        # last_name = name_pieces[1]   # This returns an attribute error. This is because last_name was not initialized
        self.last_name = name_pieces[1]    # This can also work: name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        # Since we will be working with dates, we need to import the datetime module.
        today = datetime.date(2001, 5, 12)
        # Using Indexes to extract the date
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)    # Date of Birth
        age_in_days = (today - dob).days    # You get a time-delta object for doing this.
        # The time-delta object has a field called days.
        
        # Ignoring leap years, we can now compute the age in years by dividing by 365.
        age_in_years = age_in_days // 365
        return int(age_in_years)

# Initializing an object
user = Users("Dave Bowman", "19710307")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age(), "years old")

# Calling the help() funtion to check out the docstring and for more information of a function or a class.
help(Users)

