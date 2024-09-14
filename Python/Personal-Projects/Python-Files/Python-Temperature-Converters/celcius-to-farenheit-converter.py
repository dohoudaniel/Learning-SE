# celcius-to-farenheit-converter.py
# A program to convert Celsius temps to Fahrenheit
# By: Dohou Daniel

def temperature() :
    print("This program converts temperature from Celcius to Farenheit")
    celsius = eval (input ("What is the Celsius temperature: ") )
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")
