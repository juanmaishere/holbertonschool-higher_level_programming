#!/usr/bin/python3
"""summary"""
import json


def class_to_json(obj):
    """
    obj from class to json function
    """
    return obj.__dict__
