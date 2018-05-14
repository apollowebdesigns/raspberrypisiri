#You can import any modules required here

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(3, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(3, False)
	pwm.ChangeDutyCycle(0)
#This is name of the module - it can be anything you want
moduleName = "life"

#These are the words you must say for this module to be executed
commandWords = ["meaning","life"]

#This is the main function which will be execute when the above command words are said
def execute(command):
    SetAngle(90) 
    pwm.stop()
    GPIO.cleanup()
