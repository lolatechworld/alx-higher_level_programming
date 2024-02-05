#!/usr/bin/python3
"""Defines an inherited list class named MyList."""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Print the list ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
