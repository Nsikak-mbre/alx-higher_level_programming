#!/usr/bin/python3
"""This functions writes string to a text-file"""


def write_file(filename="", text=""):
    """
    Accepts filename, and string to write

    Args:
        filename(str): name of file to be processed
        text(character): contents of above file

    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
       char_written = file.write(text)
    return char_written
