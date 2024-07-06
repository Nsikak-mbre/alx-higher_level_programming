#!/bin/bash
# sends a delete request passed as first agument
# Diplays the body of the response

curl -sX DELETE "$1"
