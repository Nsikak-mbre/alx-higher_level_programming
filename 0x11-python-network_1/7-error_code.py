#!/usr/bin/python3
"""
sends URL request using requests, displays body of response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if (response.status_code >= 400):
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
