#!/usr/bin/python3
"""summary"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        c = json.load(filename)
