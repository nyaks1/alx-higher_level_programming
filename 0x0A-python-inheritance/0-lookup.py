#!/usr/bin/python3

"""
Defines an object attribute lookup function and returns a list of an object's available attributes.
"""

def lookup(obj):
    return (dir(obj))
