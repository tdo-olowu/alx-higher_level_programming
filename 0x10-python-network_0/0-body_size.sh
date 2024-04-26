#!/bin/bash

if [ $# -eq 1 ]; then
	url=$1
	size=$(curl -sI "$url" | grep -i '^content-length:' | awk '{print $2}' | tr -d '\r')
	echo "$size"
fi
