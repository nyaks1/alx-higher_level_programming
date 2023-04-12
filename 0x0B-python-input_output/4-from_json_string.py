#!/usr/bin/python3
#6-from_json_string.py
"""Defines a function that returns a Python data structure represented by a JSON string."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string."""
    return json.loads(my_str)
