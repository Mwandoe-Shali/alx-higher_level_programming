#!/bin/bash
# Script to send a GET request to a URL with a custom header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
