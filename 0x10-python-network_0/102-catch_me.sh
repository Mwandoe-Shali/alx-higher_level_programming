#!/bin/bash
# Script to make a request to a specific URL and get a specific response
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
