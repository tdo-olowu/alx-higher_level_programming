#!/bin/bash
# script doing x`jj

url=$1

response=$(curl -s -H "X-School-User-Id: 98" "$url")

# Display the body of the response
echo "$response"
