#!/usr/bin/python3
"""
Sends request to URL, and displays value of the X-Request-Id
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)
