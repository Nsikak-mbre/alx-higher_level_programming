#!/usr/bin/python3
"""
Sends URL request, display received request body, handle error codes
"""


import urllib.error


if __name__ == '__main__':
    import urllib.request
    import sys

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
