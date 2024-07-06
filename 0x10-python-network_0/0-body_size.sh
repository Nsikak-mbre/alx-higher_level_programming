#!/bin/bash
# sends a request to a url and displays the body size
url="#1"
curl -s "$url" | wc -c