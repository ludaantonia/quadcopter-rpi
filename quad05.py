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
        c1.forward(t)
        c2.forward(t)
        ccw1.backward(t*abs(x))
        ccw2.backward(t*abs(x))
    elif x>0:
        c1.forward(t*x)
        c2.forward(t*x)
        ccw1.backward(t)
        ccw2.backward(t)


def setTranslationValue(x, y, t):
    if abs(x) > abs(y):
        if x > 0:
            c1.forward(t*x)
            c2.forward(t)
            ccw1.backward(t)
            ccw2.backward(t*x)
        elif x < 0:
            c1.forward(t)
            c2.forward(t*abs(x))
            ccw1.backward(t*abs(x))
            ccw2.backward(t)
    elif abs(x) < abs(y):
        if y > 0:
            c1.forward(t*y)
            c2.forward(t)
            ccw1.backward(t*y)
            ccw2.backward(t)
        elif y < 0:
            c1.forward(t)
            c2.forward(t*abs(y))
            ccw1.backward(t)
            ccw2.backward(t*abs(y))    


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
