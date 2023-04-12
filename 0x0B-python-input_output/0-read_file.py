#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file and print its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
