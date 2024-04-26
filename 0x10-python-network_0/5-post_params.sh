#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    exit 1
fi

# Get the URL from the argument
url=$1

# Define the POST data
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request using curl with POST data and display the body of the response
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

# Display the body of the response
echo "$response"

