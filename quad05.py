import RPi.GPIO as GPIO
from gpiozero import Motor
import pygame

# motor setup
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

c1 = Motor(port1, port2)
c2 = Motor(port1, port2)
ccw1 = Motor(port1, port2)
ccw2 = Motor(port1, port2)

# joystick setup
pygame.init()
joystick_count = pygame.joystick.get_count()

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()


# functions
def setThrottleValue(t):
    c1.forward(t)
    c2.forward(t)
    ccw1.backward(t)
    ccw2.backward(t)


def setRotateValue(x, t):
    if x<0:
        c1.forward(1)
        c2.forward(1)
        ccw1.backward(0.7)
        ccw2.backward(0.7)
    elif x>0:
        c1.forward(0.7)
        c2.forward(0.7)
        ccw1.backward(1)
        ccw2.backward(1)


def setTranslationValue(x, y, t):
    if abs(x) > abs(y):
        if x > 0:
            c1.forward(0.7)
            c2.forward(1)
            ccw1.backward(1)
            ccw2.backward(0.7)
        elif x < 0:
            c1.forward(1)
            c2.forward(0.7)
            ccw1.backward(0.7)
            ccw2.backward(1)
    elif abs(x) < abs(y):
        if y > 0:
            c1.forward(0.7)
            c2.forward(1)
            ccw1.backward(0.7)
            ccw2.backward(1)
        elif y < 0:
            c1.forward(1)
            c2.forward(0.7)
            ccw1.backward(1)
            ccw2.backward(0.7)    


# joystick input values converted to electrical output
        
while True:
    pygame.event.pump()

    # quit
    if joystick.get_button(0):
        print("quit program")
        GPIO.cleanup()
        break

    # translation
    rightJoyX = joystick.get_axis(3)
    rightJoyY = joystick.get_axis(4)
    # rotation
    leftJoyX = joystick.get_axis(0)
    # throttle
    leftJoyY = joystick.get_axis(1)
    
    print("rightJoyX:" + rightJoyX)
    print("rightJoyY:" + rightJoyY)
    print("leftJoyX:" + leftJoyX)
    print("leftJoyY:" + leftJoyY)

    setThrottleValue(leftJoyY)
    setRotateValue(leftJoyX, leftJoyY)
    setTranslationValue(rightJoyX, rightJoyY, leftJoyY)

print("program was quit")
