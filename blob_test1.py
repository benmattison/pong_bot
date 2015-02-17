from SimpleCV import Camera, Display, Image, Display, DrawingLayer, Color
from time import sleep

myCamera = Camera(prop_set={'width' : 320, 'height' : 240})

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
	green_stuff = myCamera.getImage().colorDistance(Color.RED)

	green_blobs = green_channel.findBlobs()
	#blobs are returned in order of area, smallest first

	print "largest red blob at " + str(green_blobs[-1].x) + ", " + str( green_blobs[-1].y)


	frame.save(myDisplay)
	sleep(0.1)

