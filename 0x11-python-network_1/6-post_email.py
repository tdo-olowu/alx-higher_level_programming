#!/usr/bin/python3
"""posts to email using the requests module"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    rsvp = requests.post(url, data=params)
    print("Your email is: {}".format(rsvp.text))
