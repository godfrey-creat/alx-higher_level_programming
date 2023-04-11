#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of the objects available attributes."""
    return (dir(obj))
