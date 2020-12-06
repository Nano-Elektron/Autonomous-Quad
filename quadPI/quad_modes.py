import RPi.GPIO as gpio
from time import sleep

class Modes():

    def armed_mode(self, throttle_stick, rudder_stick, min_throttle, min_rudder, mid_rudder):
        print("quad to be armed in....")
        sleep(1)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        throttle_stick.ChangeDutyCycle(min_throttle)
        rudder_stick.ChangeDutyCycle(min_rudder)
        sleep(3)
        rudder_stick.ChangeDutyCycle(mid_rudder)
        print("quadquad successfully armed and stick positions set to normal....")
        sleep(2)


    def safe_mode(self, throttle_stick, rudder_stick, min_throttle, max_rudder, mid_rudder):
        print("disarming quad")
        throttle_stick.ChangeDutyCycle(min_throttle)
        sleep(2)
        rudder_stick.ChangeDutyCycle(max_rudder)
        sleep(3)
        rudder_stick.ChangeDutyCycle(mid_rudder)
        sleep(2)
        print("quad successfully disarmed and stick positions set to normal....")





