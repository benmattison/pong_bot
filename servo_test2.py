from time import sleep
from subprocess import call

def convertAngle( angle ):
	return angle*200/180 + 50

delay = 1
angle = 0

while True:
	if angle > 150:
		angle = 0

	pwmTime = convertAngle(angle)

	echoString = "echo 2=" + str(pwmTime) + " > /dev/servoblaster"

	call([echoString],shell=True)

	angle = angle + 20

	sleep(delay)