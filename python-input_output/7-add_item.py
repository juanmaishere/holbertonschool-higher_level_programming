#!/usr/bin/python3
"""summary"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

data += sys.argv[1:]

if not data:
    data = []

save_to_json_file(data, filename)
