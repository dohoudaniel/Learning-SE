#!/usr/bin/python3

# ChatGPT

def append_after(filename="", search_string="", new_string=""):
    """Append a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to be inserted after each matching line.

    Returns:
        None
    """

    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Create a new list to store the modified lines
    modified_lines = []

    # Iterate through each line in the file
    for line in lines:
        # Append the current line to the modified list
        modified_lines.append(line)

        # Check if the search string is found in the current line
        if search_string in line:
            # Append the new string after the line containing the search string
            modified_lines.append(new_string)

    # Write the modified lines back to the file
    with open(filename, 'w') as file:
        file.writelines(modified_lines)

