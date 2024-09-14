#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
"""
The reason why the checker fails if the code on
line 4 is `word[7:]` is because
using `word[-2:]` returns the last two characters of
string, even if its length changes.
This works efficiently for string of different lengths.
The code `word[7:]` assumes a specific starting index and
is not adaptive to different string lengths.
"""
