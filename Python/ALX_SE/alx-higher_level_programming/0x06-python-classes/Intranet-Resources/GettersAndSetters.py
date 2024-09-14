"""
Python: Getters and Setters
Link: https://python-course.eu/oop/properties-vs-getters-and-setters.php
"""
# Example 1: In The Javalike Way
class P:
    def __init__(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
# Instantiation -- Run for Output
p1 = P(42)
p2 = P(4711)
print(p1.get_x())
p1.set_x(47)
p1.set_x(p1.get_x() + p2.get_x())
print(p1.get_x())

# Example 2: The Pythonic Way (Using a Public Attribute)
class P:
    def __init__(self, x):
        self.x = x
# Instantiation -- Run for Output
p1 = P(42)
p2 = P(4711)
print(p1.x)
p1.x = 47
p1.x = p1.x + p2.x
print(p1.x)

# Example 3:
# Problem: But what happens if we want to change the implementation in the future? This is a serious argument.
#   Let's assume we want to change the implementation like this: The attribute x can have values between 0 and 1000.
#   If a value larger than 1000 is assigned, x should be set to 1000. Correspondingly, x should be set to 0, if the value is less than 0.
#   It is easy to change our first P class to cover this problem. We change the set_x method accordingly:
class P:
    def __init__(self, x):
        self.set_x(x)
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    def get_x(self):
        return self.__x

# Instantiation -- Run for Output
p1 = P(1001)
p1.get_x()
print(p1.get_x())    # Returns 1000
p2 = P(15)
p2.get_x()
print(p2.get_x())    # Returns 15
p3 = P(-1)
p3.get_x()
print(p3.get_x())    # Returns 0


# Example 4 (You should perfectly undersand this):
class P2:
    def __init__(self, x):
        self.__x = x
        # return x -> This returns an error instead:  TypeError: __init__() should return None, not 'int'
# Instantiation -- Run for Output
p1 = P2(42)
p1.x = 1001
print(p1.x)



# If we would change P2 now in the way of the class P, our new class would break the interface, because the attribute x will not be available anymore.
# That's why in Java e.g. people are recommended to use only private attributes with getters and setters, so that they can change the implementation
# without having to change the interface.
# But Python offers a solution to this problem. The solution is called properties!
# The class with a property looks like this:
class P:
    def __init__(self, x):
        self.x = x
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
"""
The method which is used for getting a value is decorated with "@property", i.e. we put this line directly in front of the header.
The method which has to function as the setter is decorated with "@x.setter". If the function had been called "f",
we would have to decorate it with "@f.setter". Two things are noteworthy: We just put the code line "self.x = x" in the __init__ method
and the property method x is used to check the limits of the values. The second interesting thing is that we wrote "two" methods with the
same name and a different number of parameters "def x(self)" and "def x(self,x)".
"""
p1 = P(1001)
print(p1.x)
p1.x = -12
print(p1.x)


"""
Alternatively, we could have used a different syntax without decorators to define the property. As you can see, the code is definitely
less elegant and we have to make sure that we use the getter function in the __init__ method again:
"""
class P:
    def __init__(self, x):
        self.set_x(x)
    def get_x(self):
        return self.__x
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(get_x, set_x)
"""
There is still another problem in the most recent version. We have now two ways to access or change the value of x: Either by using "p1.x = 42"
or by "p1.set_x(42)". This way we are violating one of the fundamentals of Python:
"There should be one-- and preferably only one --obvious way to do it." (see Zen of Python - https://python-course.eu/python-tutorial/history-and-philosophy-of-python.php )

We can easily fix this problem by turning the getter and the setter methods into private methods, which can't be accessed anymore by the users of our class P:
"""
class P:
    def __init__(self, x):
        self.__set_x(x)
    def __get_x(self):
        return self.__x
    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x, __set_x)



"""
The following example shows a class, which has internal attributes, which can't be accessed from outside.
These are the private attributes self.__potential _physical and self.__potential_psychic.
Furthermore we show that a property can be deduced from the values of more than one attribute.
The property "condition" of our example returns the condition of the robot in a descriptive string.
The condition depends on the sum of the values of the psychic and the physical conditions of the robot.
"""
class Robot:
    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp
    
    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!" 
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)


"""
Public instead of Private Attributes
"""
class OurClass:
    def __init__(self, a):
        self.OurAtt = a
    @property
    def OurAtt(self):
        return self.__OurAtt
    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val
x = OurClass(10)
print(x.OurAtt)
"""
This is great, isn't it? You can start with the simplest implementation imaginable, and you are free to later migrate to a
property version without having to change the interface! So properties are not just a replacement for getters and setters!
Something else you might have already noticed: For the users of a class, properties are syntactically identical to ordinary attributes.
"""

