#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    exit 1
fi

# Get the URL from the argument
url=$1

# Send GET request using curl with X-School-User-Id header and display the body of the response
response=$(curl -s -H "X-School-User-Id: 98" "$url")

# Display the body of the response
echo "$response"
