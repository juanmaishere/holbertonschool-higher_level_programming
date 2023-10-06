#!/usr/bin/python3
""" Summary """


def write_file(filename="", text=""):
    """ Write function that writes"""
    with open(filename, 'w', encoding="utf-8") as f:
        c = f.write(text)
    return c
