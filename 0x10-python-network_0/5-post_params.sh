#!/bin/bash
# script doing h

url=$1

# Define the POST data
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request using curl with POST data and display the body of the response
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

# Display the body of the response
echo "$response"
