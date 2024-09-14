# Keys are immutable (strings)
my_dict = {"name": "John", "age": 25, (1, 2): "tuple_key"}

# Values can be mutable (list)
my_dict["hobbies"] = ["reading", "coding"]

print(my_dict["name"])

# Creating a new dictionary using a set comprehension
# Original dictionary
original_dict = {"old_key": "value", "another_key": "another_value"}

# Creating a new dictionary with modified keys
new_dict = {new_key: original_dict[old_key] for old_key, new_key in [("old_key", "new_key"), ("another_key", "different_key")]}
print(new_dict)

# Creating a list using a dictionary
my_list = list(my_dict)
print(my_list)
# sorted_dict = sorted(my_dict)

# Looping through dictionaries
for key, value in my_dict.items():
    print(key, ", ", value)

