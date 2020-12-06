import RPi.GPIO as gpio
from time import sleep

class QuadTricks():

    def throttle_surge_fall(self, throttle_stick, min_throttle, max_throttle):
        print("Throttling from 0 to 50 percent in 4 steps....")
        for dc1 in range(min_throttle,max_throttle,1):
            print("sending a pulse with {} duty cycle".format(dc1))
            throttle_stick.ChangeDutyCycle(dc1)
            sleep(3)
	sleep(5)
        print("Throttling down from 50 to 0 percent in 4 steps....")
        for dc2 in range(max_throttle,min_throttle,  -1):
            print("sending a pulse with {} duty cycle".format(dc2))
            throttle_stick.ChangeDutyCycle(dc2)
            sleep(3)
