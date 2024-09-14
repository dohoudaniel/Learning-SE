#!/usr/bin/python3
""" Virus.py -> YouTube """
from turtle import *
import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.title("Turtle Graphics")
window.geometry("800x600")

# Create a turtle graphics canvas inside the window
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Initialize turtle graphics
t = Turtle(canvas)
t.speed(10)
t.color('cyan')
window.configure(bg='black')

# Define the virus drawing function
def draw_virus():
    b = 200
    while b > 0:
        t.left(b)
        t.forward(b * 3)
        b = b - 1

# Call the virus drawing function
draw_virus()

# Run the tkinter event loop
window.mainloop()
