#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_list = set(my_list)
    total_sum = sum(sorted_list)
    print('Result: {}'.format(total_sum))
