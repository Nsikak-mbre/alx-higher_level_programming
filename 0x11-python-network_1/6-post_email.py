#!/bin/usr/python3
"""
POST request with email parameter, using request package
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data=data)
    print(response.text)
