#!/bin/bash
# sends a request to a url and displays the body size
curl -s "$1" | wc -c
