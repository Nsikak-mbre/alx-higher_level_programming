#!/usr/bin/python3
"""
sends POST request, display the body of the response
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = 'email={}'.format(email)
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
