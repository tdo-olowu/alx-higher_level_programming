#!/bin/bash
# script doing y

# Get the URL from the argument
url=$1

# Array to hold HTTP methods
http_methods=("GET" "POST" "PUT" "DELETE" "HEAD" "OPTIONS" "PATCH")

# Loop through each HTTP method and send a request to the URL
for method in "${http_methods[@]}"; do
    response=$(curl -s -X "$method" -I "$url")
    if [[ $response =~ "Allow" ]]; then
        allow_methods=$(echo "$response" | grep -i "Allow" | cut -d ":" -f 2 | tr -d '\r')
        echo "URL $url allows $method method(s): $allow_methods"
    fi
done
