#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implementing a sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a sorted list in an ascending order."""
        print(sorted(self))
