#!/usr/bin/env python3

# Submitting to a web form

import requests

url = 'http://httpbin.org/post'
data = {'fname': 'Jenu', 'lname': 'Patel'}

# submit post request
r = requests.post(url, data=data)

# display the response to screen

print(r)
print()
print(r.content)
