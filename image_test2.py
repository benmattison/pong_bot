from SimpleCV import Image, Display, DrawingLayer, Color
from time import sleep

myDisplay = Display()

raspberryImage = Image("beer-pong.jpg")

myDrawingLayer = DrawingLayer((raspberryImage.width,raspberryImage.height))

#myDrawingLayer.rectangle((50,20),(250,60),filled=True)
myDrawingLayer.setFontSize(45)
myDrawingLayer.text("Jesus Loves Beer Pong!",(50,20),color=Color.WHITE)

raspberryImage.addDrawingLayer(myDrawingLayer)
raspberryImage.applyLayers()

raspberryImage.save(myDisplay)

while not myDisplay.isDone():
	sleep(0.1)

