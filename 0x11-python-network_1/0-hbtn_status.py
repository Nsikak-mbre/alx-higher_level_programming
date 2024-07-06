#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()

print('Body response:')
print('\t- type', type(body))
print('\t- content:', body)
print('\t- utf8 content:', body.decode('utf-8'))
