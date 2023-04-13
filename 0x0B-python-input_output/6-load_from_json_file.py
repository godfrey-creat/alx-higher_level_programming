#!/usr/bin/python3
"""Defining a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creating an object from a JSON file"""
    with open(filename) as k:
        return json.load(k)
