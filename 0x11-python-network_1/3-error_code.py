#!/usr/bin/python3
"""requests an URL, displays the body of the response...
but with error handling! Manages urllib.error.HTTPError"""


import urllib.request as uquest
import urllib.parse as uparse
import urllib.error as uerror
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with uquest.urlopen(url) as rsvp:
            response = rsvp.read()
            body = response.decode("utf-8")
            print(body)
    except uerror.HTTPError as err:
        print("Error code: {}".format(err.code))
