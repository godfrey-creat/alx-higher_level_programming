#!/usr/bin/python3
"""Defining a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """writing the object to the file in JSON representation"""
    with open(filename, 'w') as k:
        json.dump(my_obj, k)
