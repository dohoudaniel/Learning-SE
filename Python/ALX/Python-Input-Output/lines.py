#!/usr/bin/python3

# How to read one line at a time in a file
import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myFile2:
    myFile2.write("Some random text\nAnd even more random text\nAnd Much More")

with open("mydata2.txt", encoding="utf-8") as myFile2:
    lineNum = 1
    # Using a loop to make sure the data is all read
    while True:
        line = myFile2.readline()
        
        # Check if line doesn't have any data
        if not line:
            break
        
        # Printing the line
        print("Line ", lineNum, " : ", line, end="")
        
        # Increasing the value of lineNum
        lineNum += 1

print()

print(myFile2.name)

