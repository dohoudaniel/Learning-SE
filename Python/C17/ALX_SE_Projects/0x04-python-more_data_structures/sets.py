# Learning Python DSAs: Sets and Dictionaries

my_basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(my_basket) # Duplicate values are not printed

print('orange' in my_basket)
print('crabgrass' in my_basket)

# Demonstration of set operations on unique letters from two words
my_a = set('abracadabra')
my_b = set('alacazam')
print(my_a) # Unique letters in a
print(my_b) # Unique letters in b
print(my_a - my_b) # Letters in a but not in b
print(my_a | my_b)  # Letters in a but not in b
print(my_a & my_b)  # Letters in a and in b
print(my_a ^ my_b) # Letters in a or in b but not in both

