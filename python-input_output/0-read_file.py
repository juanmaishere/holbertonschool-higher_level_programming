#!/usr/bin/python3
"""
Summary
"""


def read_file(filename=""):
    """
    function that reads a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
