import RPi.GPIO as gpio
from time import sleep
from quadPI.calibrate import *
from quadPI.quad_modes import  *
from quadPI.quad_tricks import *

ch1 = 11
ch2 = 12
ch3 = 15
ch4 = 16

throttle_max = 9
throttle_min = 3

max_stick_position = 9
mid_stick_position = 7
min_stick_position = 4

signal_frequency = 50


gpio.setmode(gpio.BOARD)
gpio.setup(ch1, gpio.OUT)
gpio.setup(ch2, gpio.OUT)
gpio.setup(ch3, gpio.OUT)
gpio.setup(ch4, gpio.OUT)


aileron_ch1 = gpio.PWM(ch1,signal_frequency)
aileron_ch1.start(mid_stick_position)
elevator_ch2 = gpio.PWM(ch2,signal_frequency)
elevator_ch2.start(mid_stick_position)
throttle_ch3 = gpio.PWM(ch3,signal_frequency)
throttle_ch3.start(throttle_min)
rudder_ch4 = gpio.PWM(ch4,signal_frequency)
rudder_ch4.start(mid_stick_position)

cb = Calibrate()
modes = Modes()
tricks = QuadTricks()



def resetAll():
    aileron_ch1.ChangeDutyCycle(mid_stick_position)
    elevator_ch2.ChangeDutyCycle(mid_stick_position)
    throttle_ch3.ChangeDutyCycle(throttle_min)
    rudder_ch4.ChangeDutyCycle(mid_stick_position)


def stopAll():
    aileron_ch1.stop()
    elevator_ch2.stop()
    throttle_ch3.stop()
    rudder_ch4.stop()
    sleep(2)
    gpio.cleanup()




try:
    calibrate = raw_input("y -> to calibrate throttle  n -> to arm the quad and rise the throttle : ")
    if(calibrate == 'y'):
        cb.throttle_calibrate(throttle_ch3, throttle_max, throttle_min)
    else:
        modes.armed_mode(throttle_ch3,rudder_ch4,throttle_min,min_stick_position, mid_stick_position)
        sleep(2)
        tricks.throttle_surge_fall(throttle_ch3, 3 , 8)
	sleep(2)
	print("disArming.....")
    	sleep(2)
    	modes.safe_mode(throttle_ch3, rudder_ch4, throttle_min, max_stick_position, mid_stick_position)

    sleep(2)
    resetAll()
    print("stopping...")
    sleep(2)
    stopAll()

except Exception as e:
    print('error')
    print(e)
    stopAll()





