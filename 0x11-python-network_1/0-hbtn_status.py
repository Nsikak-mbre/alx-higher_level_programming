#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
and displays the body of the resp.
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        body = resp.read()

    print('Body resp:')
    print('\t- type', type(body))
    print('\t- content:', body)
    print('\t- utf8 content:', body.decode('utf-8'))
