from SimpleCV import Camera, Display, Image, Display, DrawingLayer, Color, ColorModel
from time import sleep

myCamera = Camera(prop_set={'width' : 320, 'height' : 240})
#redImage = Image("red.jpg")
#redCrop = redImage.crop(0,0,320,240)

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
	frame = myCamera.getImage()
	cm = ColorModel()
	cm.add(Color.RED)

	cup = cm.threshold(frame)

	#cup = frame.findBlobs()
	cup.show()
	#blobs are returned in order of area, smallest first
	#print(cup)

	#frame.save(myDisplay)
	sleep(5)

