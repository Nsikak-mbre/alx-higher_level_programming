#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """

    division of each element in a list by another

    """
    result = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")
                elif not (isinstance(my_list_1[i], (int, float))
                          or not isinstance(my_list_2[i], (int, float))):
                    raise TypeError("wrong type")
                elif my_list_2[i] == 0:
                    raise ZeroDivisionError("division by 0")
                else:
                    result.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
            except TypeError:
                result.append(0)
                print("wrong type")
            except IndexError:
                result.append(0)
                print("out of range")
    finally:
        return result
