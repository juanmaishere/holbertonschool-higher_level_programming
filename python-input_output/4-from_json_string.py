#!/usr/bin/python3
"""summary"""
import json


def from_json_string(my_str):
    c = json.load(my_str)
    return c
