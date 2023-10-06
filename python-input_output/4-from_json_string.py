#!/usr/bin/python3
"""summary"""
import json


def from_json_string(my_str):
    """
    Function to load a str from json format
    """
    c = json.load(my_str)
    return c
