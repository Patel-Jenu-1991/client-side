#!/usr/bin/env python3

# Downloading a web page

import requests

r = requests.get("http://www.python.org/")

# write the content to test_request.html
with open("test_request.html", "wb") as code:
    code.write(r.content)
