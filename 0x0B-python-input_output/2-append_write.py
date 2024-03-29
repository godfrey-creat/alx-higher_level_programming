#!/usr/bin/python3
"""Defining a file-appending function"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    Args:
    filename (godfrey): The name of the file to  append to.
    text (godfrey): The string to append to the file.
    Returns:
    The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
