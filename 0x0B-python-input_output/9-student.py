#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object
        Args:
            first_name (gody): The first name of the student.
            last_name (gody): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dict representation of the Student."""
        return self.__dict__
