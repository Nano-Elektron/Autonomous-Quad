import RPi.GPIO as gpio
from time import sleep

class Calibrate():

    def throttle_calibrate(self,throttle_channel, throttle_max, throttle_min):
        throttle_channel.ChangeDutyCycle(throttle_max)
        print("Power and initialise the quad for throttle calibration...")
        pass_through = raw_input("press enter for throttle to passthrough down after buzzer is heard...")
        throttle_channel.ChangeDutyCycle(throttle_min)
        sleep(3)
        print("Calibration should be successful....restart the flight stabilizer")
