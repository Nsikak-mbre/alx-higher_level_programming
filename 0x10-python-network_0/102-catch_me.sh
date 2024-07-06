#!/bin/bash
#  sends a request with, which causes a custom return message
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
