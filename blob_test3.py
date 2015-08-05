from SimpleCV import Camera, Display, Image, Display, DrawingLayer, Color, ColorModel
from time import sleep

myCamera = Camera(prop_set={'width' : 640, 'height' : 480})

while True:
	frame = myCamera.getImage().colorDistance(Color.RED)
	negative = frame.colorDistance(Color.WHITE)

	blobs = negative.findBlobs(threshval=(210,210,210),minsize=10)

	height = blobs[-1].height()

	for b in blobs:
		b.drawOutline(color=Color.RED)

	distance = 9249/height

	print "max height is " + str(height)
	print "distance to target is " + str(distance) + "cm"
	
	sleep(5)