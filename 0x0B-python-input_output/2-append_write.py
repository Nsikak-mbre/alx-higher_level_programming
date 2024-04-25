#!/usr/bin/python3
"""Appends strings at file end"""


def append_write(filename="", text=""):
    """
    Accepts two Parameters

    Args:
        filename(str): name of file to be processed
        text(character): contents of above file

    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
    return chars_added
