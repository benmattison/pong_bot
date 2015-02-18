from SimpleCV import Camera, Display, Image, Display, DrawingLayer, Color, ColorModel
from time import sleep

myCamera = Camera(prop_set={'width' : 320, 'height' : 240})
#redImage = Image("red.jpg")
#redCrop = redImage.crop(0,0,320,240)

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
	frame = myCamera.getImage().colorDistance(Color.RED)
	negative = frame.colorDistance(Color.WHITE)

	#cm = ColorModel()
	#cm.add(Color.BLACK)
	#cup = cm.threshold(frame)

	blobs = negative.findBlobs()

	#cups = blobs.filter([b.isRectangle(0.5) for b in blobs])

	for b in blobs:
		b.drawOutline()


	#blobs are returned in order of area, smallest first
	print(blobs)

	#myDrawingLayer = DrawingLayer((frame.width,frame.height))
	#myDrawingLayer.sprite(cup)
	#frame.addDrawingLayer(myDrawingLayer)
	#frame.applyLayers()
	
	negative.save(myDisplay)
	sleep(5)

