#!/bin/bash
# sends url request as argument, displays response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
