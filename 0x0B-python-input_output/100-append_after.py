#!/usr/bin/python3
"""Module for append after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string

    Args:
        filename (str): Name of the file
        search_string (str): String to search for in the file
        new_string (str): New string to insert

    Returns:
        None
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
