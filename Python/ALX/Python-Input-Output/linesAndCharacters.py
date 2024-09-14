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
        
        # Using split() to know the words in a line
        wordList = line.split()
        print("wordList = ", wordList)
        
        # Usng len() to get the number of words
        numOfWords = len(wordList)
        print("Number of words on line {} = {}".format(lineNum, numOfWords))
        
        # Looping through to count characters in the word list:
        charCount = 0
        for word in wordList:
            for char in word:
                charCount += 1
        
        # Print number of characters
        print("Number of characters: ", charCount)
        
        # Divide character count by length of word list
        avgNumOfChars = charCount / numOfWords
        print("Average Word Length : {:.2}".format(avgNumOfChars))
        
        # Increment line number
        lineNum += 1
        
        # Print new line
        print()

# Print file used
print(myFile2.name)
