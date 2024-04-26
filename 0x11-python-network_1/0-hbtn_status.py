#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

from urllib import requests

rsvp = requests("https://alx-intranet.hbtn.io/status")
print(rsvp.status)
