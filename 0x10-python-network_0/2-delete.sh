#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    exit 1
fi

# Get the URL from the argument
url=$1

# Send DELETE request using curl and display the body of the response
response=$(curl -s -X DELETE "$url")

# Display the body of the response
echo "$response"
