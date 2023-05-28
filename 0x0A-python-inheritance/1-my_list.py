#!/usr/bin/python3
"""Ït defines an inherited list in MyList"""

class MyList(list):
    """Ït implements sorted printing for the bult in list class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
