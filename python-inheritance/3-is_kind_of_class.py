#!/usr/bin/python3
"""
Function to check wether is the same class or
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
