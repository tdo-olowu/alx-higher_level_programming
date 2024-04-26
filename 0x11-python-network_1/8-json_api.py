#!/usr/bin/python3
"""json api"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    ac = len(sys.argv)
    if (ac < 1):
        q = ""
    else:
        q = sys.argv[1]

    params = {"q": q}
    rsvp = requests.post(url, data=params)

    try:
        json_data = rsvp.json()
        if json_data:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
