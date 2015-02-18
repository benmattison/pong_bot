from SimpleCV import Camera, Display, Image, Display, DrawingLayer, Color
from time import sleep

myCamera = Camera(prop_set={'width' : 320, 'height' : 240})

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
	frame = myCamera.getImage()

	cup = frame.findBlobs()
	cup.draw()
	#blobs are returned in order of area, smallest first

	print(cup)

	frame.save(myDisplay)
	sleep(5)

