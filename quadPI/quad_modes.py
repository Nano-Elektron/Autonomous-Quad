import RPi.GPIO as gpio
from time import sleep


class Modes():

    armed = False

    def armed_mode(self, throttle_stick, rudder_stick, min_throttle, min_rudder, mid_rudder):
        print("quad to be armed")
        throttle_stick.ChangeDutyCycle(min_throttle)
        rudder_stick.ChangeDutyCycle(min_rudder)
        sleep(2)
        rudder_stick.ChangeDutyCycle(mid_rudder)
        print("quadquad successfully armed and stick positions set to normal")
        self.armed = True

    def safe_mode(self, throttle_stick, rudder_stick, min_throttle, max_rudder, mid_rudder):
        print("disarming quad")
        throttle_stick.ChangeDutyCycle(min_throttle)
        sleep(1)
        rudder_stick.ChangeDutyCycle(max_rudder)
        sleep(1)
        rudder_stick.ChangeDutyCycle(mid_rudder)
        sleep(1)
        print("quad successfully disarmed and stick positions set to normal....")
        self.armed = False
