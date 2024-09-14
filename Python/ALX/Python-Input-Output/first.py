#!/usr/bin/python3

import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("I am Dohou Daniel\nI am A Beautiful Mind\nAnd I am much more.")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print(myFile.closed)  # Returns True

# Returns the name of the file it is associated with. Here, it is mydata.txt
print(myFile.name)

# Prints the mode used on the file.
print(myFile.mode)

# Renaming a file.
# os.rename("mydata.txt", "mydata2.txt")
# This renames mydata.txt to mydata2.txt

# Removing a file
# os.remove("mydata.txt")

# Creating a directory
# os.mkdir("myDirectory")

# Change the current working directory to the specified path.
# os.chdir("myDirectory")

# Print working directory (current directory)
print("Current Directory : ", os.getcwd())

# Move to a directory
# os.chdir("..")
# print("Current Directory : ", os.getcwd()) # To confirm

# Remove a directory
# os.rmdir("myDirectory")
