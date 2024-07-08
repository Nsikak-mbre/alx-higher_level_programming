#!/user/bin/python3
"""
sends POST request using requests
"""

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ''
    data = {'q': letter}
    try:
        response = requests.post(url, data=data)
        json_response = response.json()
        if json_response:
            print('[{json_response.get('id')}] {json_response.get('name')}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
