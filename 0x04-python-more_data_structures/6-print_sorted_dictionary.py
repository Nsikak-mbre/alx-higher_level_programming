#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_d = sorted(a_dictionary)
    for key in sorted_d:
        print('{}: {}'.format(key, a_dictionary[key]))
