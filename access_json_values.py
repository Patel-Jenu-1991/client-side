#!/usr/bin/env python3

# JSON Parsing 2

import json

# decodes the json file

output = json.load(open('cars.json'))

# display output to screen
print("\n"+output[0]["CARS"][0]["MODEL"]+"\n")
