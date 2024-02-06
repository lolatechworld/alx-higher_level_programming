#!/usr/bin/python3
"""This defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns: object: the Python object representation by a JSON string."""
    return json.loads(my_str)
