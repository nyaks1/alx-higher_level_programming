#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    Returns:
        The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
