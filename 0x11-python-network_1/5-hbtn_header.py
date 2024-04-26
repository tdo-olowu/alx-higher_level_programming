#!/usr/bin/python3
"""uses requests to request url and display x-request-id"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    rsvp = requests.get(url)
    xrid = rsvp.headers.get("X-Request-Id")
    print(xrid)
