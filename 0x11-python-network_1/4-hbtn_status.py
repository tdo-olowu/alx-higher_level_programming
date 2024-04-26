#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

url = "https://alx-intranet.hbtn.io/status"
rsvp = requests.get(url)
msg = "Body response:\n"
msg += "\t- type: {}\n".format(type(rsvp.text))
msg += "\t- content: {}".format(rsvp.text)
print(msg)
