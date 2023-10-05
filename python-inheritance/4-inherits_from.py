#!/usr/bin/python3
"""
checks if it is a subclass or not
"""


def inherits_from(obj, a_class):
    """check if its a subclass or not"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
