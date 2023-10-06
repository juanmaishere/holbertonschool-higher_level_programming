#!/usr/bin/python3
"""summary"""
import json


def save_to_json_file(my_obj, filename):
    """
    save an object to json and a file
    """
    with open(filename, 'w') as f:
        c = json.dumps(my_obj)
        f.write(c)
