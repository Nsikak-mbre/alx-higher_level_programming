#!/usr/bin/python3
"""Adds adds command line arg to python list and saves to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            my_list.append(arg)
        save_to_json_file(my_list, "add_item.json")
