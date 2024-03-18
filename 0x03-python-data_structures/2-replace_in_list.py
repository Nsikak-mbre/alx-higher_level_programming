#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if not my_list or idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        my_list[:] = new_list[:]
        return new_list
