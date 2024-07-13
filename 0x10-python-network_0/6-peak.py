def find_peak(list_of_integers):
    """
    Find a peak element in a list of unsorted integers.
    A peak element is an element that is greater than its neighbors.
    :param list_of_integers: List of integers
    :return: A peak element
    """
    if not list_of_integers:
        return None

    return _find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak_helper(arr, low, high):
    """
    Helper function to find peak element using binary search.
    :param arr: List of integers
    :param low: Starting index
    :param high: Ending index
    :return: A peak element
    """
    mid = (low + high) // 2

    if (mid == 0 or arr[mid] >= arr[mid - 1]) and (
        mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]
    ):
        return arr[mid]
    elif mid > 0 and arr[mid] < arr[mid - 1]:
        return _find_peak_helper(arr, low, mid - 1)
    else:
        return _find_peak_helper(arr, mid + 1, high)
