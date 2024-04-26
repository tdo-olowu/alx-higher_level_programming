#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

    The email must be sent in the email variable
    You must use the packages urllib and sys
    You are not allowed to import packages other than urllib and sys
    You don’t need to check arguments passed to the script (number or type)
    You must use the with statement
"""

import urllib.request as uquest
import urllib.parse as uparse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = uparse.urlencode({'email':email}).encode("utf-8")
    with uquest.urlopen(url, data=params) as rsvp:
        rsvp.post(url, data=params)
        response = rsvp.read()
        msg = response.decode("utf-8")
        print("Your email is: {}".format(msg))
