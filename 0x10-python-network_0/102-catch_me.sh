#!/bin/bash
#  sends a request with, which causes a custom return message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me