#!/usr/bin/python3
"""gets a resource using the requests module...
but with exception handling"""

if __name__ == "__main__":
    url = sys.argv[1]
    rsvp = requests.get(url)
    stats = rsvp.status_code
    if (stats >= 400):
        # it's over 9000!
        print("Error code: {}".format(stats))
    else:
        print(rsvp.text)
