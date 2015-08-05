from time import sleep
from subprocess import call

def convertAngle( angle ):
	return angle*200/180 + 50

delay = 1
angle = 0

while True:
	if angle > 180:
		angle = 0

	pwmTime = convertAngle(angle)

	echoString = "echo 2=" + pwmTime + " > /dev/servoblaster"

	call(echoString)

	angle = angle + 30
	