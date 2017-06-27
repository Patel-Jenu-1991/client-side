#!/usr/bin/env python3

import requests, json

url = "https://maps.googleapis.com/maps/api/directions/json?\
origin=Central+Park&destination=Times+Square&sensor=false&mode=walking"

data = requests.get(url)
binary = data.content
output = json.loads(str(binary, 'utf-8'))
print(output['status'])
print()

# prints directions

for route in output['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print(step['html_instructions'])

print()
# prints the start and end address
for route in output['routes']:
    for leg in route['legs']:
        print(leg['start_address'])
        print(leg['end_address'])
