#!/usr/bin/python3
"""summary"""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        c = json.dumps(my_obj)
        f.write(my_obj)
