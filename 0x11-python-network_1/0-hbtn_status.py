#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

link = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(link) as rsvp:
    response = rsvp.read()
    msg = "Body response:\n"
    msg += "\t-type: {}\n".format(type(response))
    msg += "\t-content: {}\n".format(response)
    msg += "\t-utf8 content: {}".format(response.decode("utf-8"))
    print(msg)
