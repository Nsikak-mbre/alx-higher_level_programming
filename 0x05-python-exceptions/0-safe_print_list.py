#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elem of a list

    Args:
        my_list(list): The list to print elements from
        x (int): The number of elements of my_list to print

    Return:
        The number of printed elements.
    """

    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except (IndexError, ValueError):
        pass
    finally:
        print()
        return count
