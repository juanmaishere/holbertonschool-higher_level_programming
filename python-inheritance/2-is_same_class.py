#!/usr/bin/python3
"""
Function checking if an object is the exact same of x class
"""


def is_same_class(obj, a_class):
    """Is it the same class?"""
    a = type(obj)
    return a is a_class
