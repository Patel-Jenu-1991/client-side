#!/usr/bin/env python3

# JSON Parsing 1

import json

# decodes the json file
output = json.load(open('cars.json'))

# display output to screen
print(output)

print()

# using the dumps method
print(json.dumps(output, indent=4, sort_keys=True))
