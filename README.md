# Mapping using Python

This is the sample code demostrated in Kaohsiung.py meetup on 2015/03/30.  The code is written in quick and dirty way, so feel free to modify it yourself.

You may bring up a CGIHTTPServer to test the code.

```
python -m CGIHTTPServer
```

Test if CGIHTTPServer and the code are running correctly by connecting to http://localhost:8000/cgi-bin/HelloWorld.py .

For static map, try: http://localhost:8000/cgi-bin/markers.py

For interactive map, you may need to have folium installed first. Then try: http://localhost:8000/cgi-bin/trackers.py .  You might encounter problems running the code under Windows due to some issue with folium.

For real time Google Earth application, try open realtimedemo.kml from Google Earth, then Google Earth will try to get the updated KML data from http://localhost:8000/cgi-bin/randomlocations.py .

Enjoy!