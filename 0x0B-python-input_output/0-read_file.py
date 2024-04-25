#!/usr/bin/python3
"""Reads a text file and prints it out"""


def read_file(filename=""):
    """
    Accepts filename as parameter

    Args:
        filename(str): name of file to be processed

    Returns:
        Characters Read from file
    """
    if filename:
        with open(filename, encoding='utf-8') as file:
            for line in file:
            print(line, end='')
