# farenheit-to-celcius-converter.py
# A program that converts from Farenheit to Celcius
# By: Dohou Daniel

def temperature():
    print("This program converts temperature from Farenheit to Celcius")
    farenheit = eval(input("What is the Farenheit temperature: "))
    celcius = 5/9 * (farenheit - 32)
    print ("The temperature is", celcius, "degrees Celcius.")
