from SimpleCV import Camera, Display, Image, Display, DrawingLayer, Color
from time import sleep

myCamera = Camera(prop_set={'width' : 320, 'height' : 240})

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
	frame = myCamera.getImage()
	myDrawingLayer = DrawingLayer((frame.width,frame.height))
	myDrawingLayer.setFontSize(45)
	faces = frame.findHaarFeatures('face')
	if faces:
		for face in faces:
			print "Face at: " + str(face.coordinates())
			coords = face.coordinates()-(70,0)
			boxStart = face.coordinates()-(70,100)
			boxEnd = face.coordinates()+(70,50)
			myDrawingLayer.rectangle(boxStart,boxEnd,filled=False)
			myDrawingLayer.text("I SEE YOU",coords,color=Color.WHITE)
			frame.addDrawingLayer(myDrawingLayer)
			frame.applyLayers()
	else:
		print "No faces detected"
	frame.save(myDisplay)
	sleep(0.1)

