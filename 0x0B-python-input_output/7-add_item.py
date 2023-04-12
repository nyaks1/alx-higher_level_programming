#!/usr/bin/python3
"""Script that adds all arguments to a Python list and save them to a file"""
import sys
from os import path
from typing import List

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename: str, args: List[str]) -> List[str]:
    """Adds all arguments to a Python list and save them to a file"""
    if path.isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)
    return my_list


if __name__ == '__main__':
    args = sys.argv[1:]
    add_item('add_item.json', args)
