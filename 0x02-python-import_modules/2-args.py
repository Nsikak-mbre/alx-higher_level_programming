#!/usr/bin/python3
import sys
size = len(sys.argv)
if size == 1:
    print('{} arguments.'.format(size - 1))
elif size == 2:
    print('{} argument:'.format(size - 1))
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
else:
    print('{} arguments:'.format(size - 1))
    for a in range(1, len(sys.argv)):
        print('{}: {}'.format(a, sys.argv[a]))


if __name__ == "__main__":
    """Print list and arg"""
