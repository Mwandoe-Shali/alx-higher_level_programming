#!/bin/bash
# Script to display all HTTP methods the server will accept from a given URL
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
