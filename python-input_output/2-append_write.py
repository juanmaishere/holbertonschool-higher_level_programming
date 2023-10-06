#!/usr/bin/python3
""" Summary """


def append_write(filename="", text=""):
    """Append function"""
    with open(filename, 'a', encoding="utf-8") as f:
        c = f.write(text)
    return c
