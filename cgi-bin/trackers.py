#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import folium

def generateMarkers(n = 5):
    c = 0
    markers = []
    while c < n:
        lat = 25.042185 + 0.002 * (random.random() - 0.5)
        lon = 121.614548 + 0.002 * (random.random() - 0.5)
        markers.append((lat,lon))
        c = c + 1
    return markers

def getCenter(markers):
    lat = 0.0
    lon = 0.0

    for marker in markers:
        lat = lat + marker[0]
        lon = lon + marker[1]

    lat = lat / float(len(markers))    
    lon = lon / float(len(markers))
    return [lat, lon]

def generateMap(markers, mapFile):
    center = getCenter(markers)
    map = folium.Map(location=center, zoom_start=18)
    for marker in markers:
        map.simple_marker([marker[0], marker[1]], popup=str(marker))
    map.create_map(path=mapFile)

def main():
    mapFile = "trackers.html"
    markers = generateMarkers(5)
    generateMap(markers,mapFile)
    print "Content-Type: text/html"
    print
    file = open(mapFile)
    print file.read()
    file.close()

if __name__=="__main__":
    main()