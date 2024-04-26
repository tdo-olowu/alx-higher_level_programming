#!/usr/bin/python3
"""script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
displays the body of the response (decoded in utf-8)
"""

import urllib.request as uquest
import urllib.parse as uparse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = uparse.urlencode({'email': email}).encode("utf-8")
    with uquest.urlopen(url, data=params) as rsvp:
        rsvp.post(url, data=params)
        response = rsvp.read()
        msg = response.decode("utf-8")
        print("Your email is: {}".format(msg))
