#!/usr/bin/python3
"""Sends a request to a URL and
   displays the value of the X-Request-Id variable.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = dict(response.headers).get("X-Request-Id")
        print(x_request_id)
