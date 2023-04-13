#!/usr/bin/python3
""" Defining a Python class-to-JSON function."""


def class_to_json(obj):
    """returning the dict representation of the object's instance variables"""
    return obj.__dict__
