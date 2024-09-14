# kelvin-to-celcius-converter.py
# A program that converts temperature from kelvin to celcius
# By: Dohou Daniel

def temperature():
    print("This program converts temperature from Kelvin to Celcius")
    kelvin = eval(input("What is the Kelvin temperature: "))
    celcius = kelvin - 273
    print("The temperature is", celcius, "degrees Celcius.")
