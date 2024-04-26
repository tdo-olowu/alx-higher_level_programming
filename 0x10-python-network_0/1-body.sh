#!/bin/bash

if [ $# -ne 1 ]; then
    exit 1
fi

url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
if [ "$response" -eq 200 ]; then
    body=$(curl -s "$url")
    echo "$body"
fi
