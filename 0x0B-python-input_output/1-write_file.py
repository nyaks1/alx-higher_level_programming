#!/usr/bin/python3
"""
Defines a function that writes a string to a text file (UTF8) and returns the
number of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters
    written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.

    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(tex)

