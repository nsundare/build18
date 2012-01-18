#!/usr/bin/python

import time
import freenect
import os

# clock.py

from urllib import urlretrieve
import imp
urlretrieve('https://raw.github.com/gist/1194123/fbconsole.py', '.fbconsole.py')
fb = imp.load_source('fb', '.fbconsole.py')

fb.AUTH_SCOPE = ['publish_stream']
fb.authenticate()

print "Welcome to the Embarrass-You-Awake-inator!"

now = list(time.localtime())
print "The current time is %(hour)d:%(min)02d:%(sec)02d" % {"hour": now[3], "min": now[4], "sec": now[5]}
print "Please enter the time you want to wake up: "
hour = input("Hour: (0-23) ")
min = input("Minute: (0-59) ")
sec = input("Seconds: (0-59) ")
print "An alarm has been set for %(hour)d:%(min)02d:%(sec)02d" % {"hour": hour, "min": min, "sec": sec}
print "Sleep, we'll wake you up!"

wait = 1
while(wait):
	now = list(time.localtime())
	now_hour = now[3]
	now_minute = now[4]
	now_second = now[5]
	if now_hour == hour and now_minute == min and now_second == sec:
		os.popen2("open /Users/Neereja/Desktop/19\ The\ resurrection\ stone.mp3")
		# Freenect commands to take picture
		
		# Post picture to Facebook
		status = fb.graph_post("/me/feed", {"message": "I overslept"})
		fb.graph_post("/me/photos", {'name': 'I can\'t wake up \:\(', 'source': open("sleepy.jpg")})
		wait = 0