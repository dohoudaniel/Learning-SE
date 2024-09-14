#!/usr/bin/python3
# Link: https://www.youtube.com/watch?v=d8kCdLCi6Lk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=42
# Python Inheritance
# Inheritance: Allows us to define a class that inherits all the methods and properties from another class.
class Animal:

    def __init__(self, birthType="Unknown",
                 appearance="Unknown",
                 blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # Using magic methods
    # Using the __str__ method to return a string
    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birthType, self.appearance, self.blooded)


class Mammal(Animal):

    def __init__(self, birthType="born alive",
                 appearance="hair or fur",
                 blooded="warm blooded",
                 nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # Overriding the __str__ method
    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)

class Reptile(Animal):

    def __init__(self, birthDayType="born in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold blooded"):
        Animal.__init__(self, birthDayType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum # Return the sum

    # Overriding the __str__ method
    def __str__(self):
        return super().__str__()
    def getBirthType(theObject):
        print("The {} is {}".format(type(theObject).__name__, theObject.birthType))

def main():
    animal = Animal("born alive")
    print(animal.birthType)
    print(animal)
    print()

    mammal = Mammal()
    print(mammal.birthType)
    print(mammal.appearance)
    print(mammal.blooded)
    print(mammal.nurseYoung)
    print(mammal)
    print()

    reptile = Reptile()
    print(reptile.birthType)
    print(reptile.appearance)
    print(reptile.blooded)
    print(reptile)
    print("Sum : ".format(reptile.sumAll(1,2,3,4,5)))

    Reptile.getBirthType(mammal)
    Reptile.getBirthType(reptile)

main()
