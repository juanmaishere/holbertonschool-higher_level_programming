#!/usr/bin/python3
"""summary"""
import json


def load_from_json_file(filename):
    """
    load a json file
    """
    with open(filename, 'r') as f:
        c = json.load(filename)
