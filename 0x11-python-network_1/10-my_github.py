#!/usr/bin/python3
"""accesses your github using requests"""

import requests
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    passw = sys.argv[2]

    url = "https://api.github.com/user"
    rsvp = requests.get(url, auth=(uname, passw))
    if (rsvp.status_code == 200):
        data = rsvp.json()
        print(data["id"])
