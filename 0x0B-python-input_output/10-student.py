#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): a list of attribute names to retrieve

        Returns:
            dict: a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with the
        corresponding attributes in a JSON dictionary

        Args:
            json (dict): a JSON dictionary
        """
        for k, v in json.items():
            setattr(self, k, v)
