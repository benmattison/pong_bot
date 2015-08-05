from SimpleCV import Camera, Image, Display, DrawingLayer, Color, ColorModel
from time import sleep
from subprocess import call
import math

def convertAngle( angle ):
	return angle*200/180 + 50

myCamera = Camera(prop_set={'width' : 640, 'height' : 480})
delay = 5 # s
angle = 0 # degrees
launchSpeed = 2 # m/s
g = 9.81 # m/s^2
h = 12 # cm

while True:
	frame = myCamera.getImage().colorDistance(Color.RED)
	negative = frame.colorDistance(Color.WHITE)

	blobs = negative.findBlobs(threshval=(210,210,210),minsize=10)

	height = blobs[-1].height()

	for b in blobs:
		b.drawOutline(color=Color.RED)

	distance = 9249/height

	print "max height is " + str(height) + " pixels"
	print "distance to target is " + str(distance) + "cm"

	d2 = math.pow(distance,2)
	v2 = math.pow(launchSpeed,2)
	
	angle = 180/math.pi * math.atan( distance + math.sqrt( d2 - 4*g*d2*(h+g*d2/(2*v2))/(2*v2) ) / (g*d2/v2) )

	if angle > 89:
		angle = angle = 180/math.pi * math.atan( distance - math.sqrt( d2 - 4*g*d2*(h+g*d2/(2*v2))/(2*v2) ) / (g*d2/v2) )


	print "optimal angle is " + str(angle) + " degrees"

	pwmTime = convertAngle(angle)

	echoString = "echo 2=" + str(pwmTime) + " > /dev/servoblaster"

	call([echoString],shell=True)

	sleep(delay)