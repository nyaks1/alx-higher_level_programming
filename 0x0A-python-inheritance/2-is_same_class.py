#!/usr/bin/python3
"""It defines a class checking function."""

def is_same_class(obj, a_class):
    """It checks if an object is an instance of a given class."""
    if type(obj) == a_class:
        return True 
    return False
