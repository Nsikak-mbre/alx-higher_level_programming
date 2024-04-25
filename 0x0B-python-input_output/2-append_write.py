#!/usr/bin/python3
"""Appends strings at file end"""


def append_writw(filename="", text=""):
    """
    Accepts two Parameters

    Args:
        filename(str): name of file to be processed
        text(character): contents of above file

    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_append = file.write(text)
    return chars_append
