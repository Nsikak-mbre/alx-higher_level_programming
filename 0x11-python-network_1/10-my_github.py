#!/usr/bin/python3
"""
Access github API, using github credentials to display ID
"""


import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        user_data = response.json()
        print('{}'.format(user_data['id']))
    else:
        print('None')
