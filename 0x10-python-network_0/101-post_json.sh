#!/bin/bash
# sends a Json request displays the body response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
