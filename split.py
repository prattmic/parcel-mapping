#!/usr/bin/env python3

import xml.etree.ElementTree as ET

ET.register_namespace("", "http://www.opengis.net/kml/2.2")

tree = ET.parse("parcel.kml")
root = tree.getroot()

document = root[0]
schema = document[0]
folder = document[1]
placemarks = folder.findall('{http://www.opengis.net/kml/2.2}Placemark')

i = 1
while placemarks:
    print("Part %d" % i)

    # Empty folder
    folder.clear()

    name = ET.Element('{http://www.opengis.net/kml/2.2}name')
    name.text = "Part %d" % i
    folder.append(name)

    j = 0
    while placemarks and j < 1400:
        folder.append(placemarks.pop(0))
        j += 1

    tree.write("out/%04d.kml" % i)
    i += 1
