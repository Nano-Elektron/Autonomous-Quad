from bluedot import BlueDot
from signal import pause
import pwm_mimic as quad

throttle_value = 4.5


def ThrottleUp():
    global throttle_value
    throttle_value += 0.25
    print("throttle value: ", throttle_value)
    quad.throttle_ch3.ChangeDutyCycle(throttle_value)

def ThrottleDown():
    global throttle_value
    throttle_value -= 0.25
    print("throttle value: ", throttle_value)
    quad.throttle_ch3.ChangeDutyCycle(throttle_value)

    
def Movement(pos):
    pass


def ArmDisarm():
    if(not quad.modes.armed):
        quad.modes.armed_mode(quad.throttle_ch3, quad.rudder_ch4, quad.throttle_min,
                              quad.min_stick_position, quad.mid_stick_position)
        
    else:
        quad.modes.safe_mode(quad.throttle_ch3, quad.rudder_ch4, quad.throttle_min,
                            quad.max_stick_position, quad.mid_stick_position)



bd = BlueDot(cols=6, rows=3)



bd.color = "#001F4D"
bd[0, 0].visible = False
bd[0, 1].visible = False
bd[1, 0].visible = False
bd[1, 2].visible = False
bd[2, 1].visible = False
bd[3, 0].visible = False
bd[3, 2].visible = False
bd[4, 0].visible = False
bd[4, 1].visible = False
bd[5, 2].visible = False
bd[5, 0].visible = False

back = bd[2, 0]
back.square = True

left = bd[1, 1]
left.square = True

right = bd[3, 1]
right.square = True

front = bd[2, 2]
front.square = True

armDisarm = bd[5, 1]
armDisarm.color = "#FF0000"

throttleUp = bd[4, 2]
throttleUp.color = "#007628"

throttleDown = bd[0, 2]
throttleDown.color = "#ED729E"


throttleUp.when_pressed = ThrottleUp
throttleDown.when_pressed = ThrottleDown

back.when_pressed = Movement('back')
left.when_pressed = Movement('left')
right.when_pressed = Movement('right')
front.when_pressed = Movement('front')


armDisarm.when_released = ArmDisarm


pause()
