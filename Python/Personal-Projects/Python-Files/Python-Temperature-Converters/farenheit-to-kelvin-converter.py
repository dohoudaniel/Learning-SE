# farenheit-to-kelvin-converter.py
# A program that converts temperature from farenheit to kelvin
# By: Dohou Daniel

def temperature():
    print("This program converts temperature from Farenheit to Kelvin")
    farenheit = eval(input("What is the Farenheit Temperature: "))
    kelvin = (5/9 * (farenheit - 32)) + 273
    print("The temperature is", kelvin, "degrees Kelvin.")
