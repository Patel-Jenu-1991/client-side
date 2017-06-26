#!/usr/bin/env python3

# XML Parsing 2 (Extracting all the data using loops)

from xml.etree import ElementTree as et

doc = et.parse("cars.xml")

# outputs the make, model and cost of each car to the screen
print()
for element in doc.findall("CAR"):
    print(element.find("MAKE").text + " " +
            element.find("MODEL").text +
            ", $" + element.find("COST").text)
print()
