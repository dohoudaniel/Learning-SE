# kelvin-to-farenheit.py
# A program that converts temperature from kelvin to farenheit
# By: Dohou Daniel

def temperature():
    print("This program converts temperature from Kelvin to Farenheit")
    kelvin = eval(input("What is the Kelvin Temperature: "))
    farenheit = (9/5 * (kelvin - 273)) + 32
    print("The temperature is", farenheit, "degrees Farenheit.")
