#!/usr/bin/python3
import sys
print(len(sys.argv) - 1, 'arguments:')
for i in range(1, len(sys.argv)):
    print('{}:{}'.format(i, sys.argv[i]))

if __name__ == "__main__":
    print('anything you like'
