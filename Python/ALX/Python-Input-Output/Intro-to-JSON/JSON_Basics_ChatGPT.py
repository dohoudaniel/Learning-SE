#!/usr/bin/python3

# JSON Basics (ChatGPT) pdf

# Importing json
import json

# 1. Syntax:
example = {
    "name":"John",
    "age":25,
    "isStudent":True,
    "subjects":["Mathematics", "Physics"],
    "address":{
        "city":"New York",
        "zip":101283
    }
}

# 4. Python and JSON

# import json
data = {
    "name":"John",
    "age":25,
    "isStudent":True,
    "subjects":["Mathematics", "Physics"],
    "address":{
        "city":"New York",
        "zip":101283
    }
}

# Convert from a Python dictionary to a JSON string
json_data = json.dumps(data) # Converts the Python dictionary to a JSON string
print("json_data =", json_data)

print()

# To decode (convert JSON to Python objects)

# import json
data2 = json.loads(json_data) # Converts the JSON string to a Python Dictionary
print("data2 =", data2)

print()

# Accessing the values in the dictionary
print("The value for data[name] is", data["name"])
print("The value for data[age] is", data["age"])
print("The value for data[address] is", data["address"])

