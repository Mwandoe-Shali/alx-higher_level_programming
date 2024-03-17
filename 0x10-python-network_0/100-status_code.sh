#!/bin/bash
# Script to send a request to a URL and display only the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
