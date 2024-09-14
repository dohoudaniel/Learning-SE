# celcius-to-kelvin-converter.py
# A program that converts temperature from celcius to kelvin
# By: Dohou Daniel

def temperature():
    print("This program converts temperature from Celcius to Kelvin")
    celcius = eval(input("What is the Celcius temperature: "))
    kelvin = celcius + 273
    print("The temperature is", kelvin, "degrees Kelvin.")
