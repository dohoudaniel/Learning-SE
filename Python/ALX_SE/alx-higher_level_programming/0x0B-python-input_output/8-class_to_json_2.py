#!/usr/bin/python3

# Done with ChatGPT

def class_to_json(obj):
    """
    Converts an object to a dictionary description with simple data structures (list, dictionary, string, integer, and boolean)
    for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing the serializable attributes of the object.

    Note:
        This function assumes that all attributes of the object are serializable (list, dictionary, string, integer, and boolean).
        Non-serializable attributes or attributes stored in nested objects may not be included in the result.

    """

    # Check if the object is already serializable
    if not isinstance(obj, type):
        return obj

    # Create an empty dictionary to store the serializable attributes
    result = {}

    # Iterate over the attributes of the class
    for key, value in obj.__dict__.items():
        # Check if the value is an instance of a serializable data type
        if isinstance(value, (list, dict, str, int, bool)):
            # Add the attribute to the result dictionary
            result[key] = value

    # Return the dictionary containing the serializable attributes
    return result
