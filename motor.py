import RPi.GPIO as GPIO
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')

args = parser.parse_args()

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

SetAngle(args.accumulate(args.integers)) 
pwm.stop()
GPIO.cleanup()