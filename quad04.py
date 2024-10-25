import RPi.GPIO as GPIO
import pygame

# motor setup
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

c1a = 
c1b =
c1 =

c2a =
c2b =
c2 = 

ccw1a =
ccw1b =
ccw1 =

ccw2a =
ccw2b =
ccw2 =


GPIO.setup(c1a,GPIO.OUT)
GPIO.setup(c1b,GPIO.OUT)
GPIO.setup(c1,GPIO.OUT)

GPIO.setup(c2a,GPIO.OUT)
GPIO.setup(c2b,GPIO.OUT)
GPIO.setup(c2,GPIO.OUT)
 
GPIO.setup(ccw1a,GPIO.OUT)
GPIO.setup(ccw1b,GPIO.OUT)
GPIO.setup(ccw1,GPIO.OUT)

GPIO.setup(ccw2a,GPIO.OUT)
GPIO.setup(ccw2b,GPIO.OUT)
GPIO.setup(ccw2,GPIO.OUT)

# PWM setup
c1PWM = GPIO.PWM(c1, 100)
c1PWM.start(0)
c2PWM = GPIO.PWM(c2, 100)
c2PWM.start(0)
ccw1PWM = GPIO.PWM(ccw1, 100)
ccw1PWM.start(0)
ccw2PWM = GPIO.PWM(ccw2, 100)
ccw2PWM.start(0)

# joystick setup
pygame.init()
joystick_count = pygame.joystick.get_count()

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()


# functions
def setThrottleValue(t):
    GPIO.output(c1a, GPIO.HIGH)
    GPIO.output(c1b, GPIO.LOW)
    GPIO.output(c1, GPIO.HIGH)
    pwmc1.ChangeDutyCycle(t*100)

    GPIO.output(c2a, GPIO.HIGH)
    GPIO.output(c2b, GPIO.LOW)
    GPIO.output(c2, GPIO.HIGH)
    pwmc2.ChangeDutyCycle(t*100)

    GPIO.output(ccw1a, GPIO.LOW)
    GPIO.output(ccw1b, GPIO.HIGH)
    GPIO.output(ccw1, GPIO.HIGH)
    pwmccw1.ChangeDutyCycle(t*100)

    GPIO.output(ccw2a, GPIO.LOW)
    GPIO.output(ccw2b, GPIO.HIGH)
    GPIO.output(ccw2, GPIO.HIGH)
    pwmccw2.ChangeDutyCycle(t*100)
    

def setRotateValue(x, t):
    if x<0:
        GPIO.output(c1a, GPIO.HIGH)
        GPIO.output(c1b, GPIO.LOW)
        GPIO.output(c1, GPIO.HIGH)
        pwmc1.ChangeDutyCycle(t*100)

        GPIO.output(c2a, GPIO.HIGH)
        GPIO.output(c2b, GPIO.LOW)
        GPIO.output(c2, GPIO.HIGH)
        pwmc2.ChangeDutyCycle(t*100)

        GPIO.output(ccw1a, GPIO.LOW)
        GPIO.output(ccw1b, GPIO.HIGH)
        GPIO.output(ccw1, GPIO.HIGH)
        pwmccw1.ChangeDutyCycle(t*x*100)

        GPIO.output(ccw2a, GPIO.LOW)
        GPIO.output(ccw2b, GPIO.HIGH)
        GPIO.output(ccw2, GPIO.HIGH)
        pwmccw2.ChangeDutyCycle(t*x*100)
    elif x>0:
        GPIO.output(c1a, GPIO.HIGH)
        GPIO.output(c1b, GPIO.LOW)
        GPIO.output(c1, GPIO.HIGH)
        pwmc1.ChangeDutyCycle(t*x*100)

        GPIO.output(c2a, GPIO.HIGH)
        GPIO.output(c2b, GPIO.LOW)
        GPIO.output(c2, GPIO.HIGH)
        pwmc2.ChangeDutyCycle(t*x*100)

        GPIO.output(ccw1a, GPIO.LOW)
        GPIO.output(ccw1b, GPIO.HIGH)
        GPIO.output(ccw1, GPIO.HIGH)
        pwmccw1.ChangeDutyCycle(t*100)

        GPIO.output(ccw2a, GPIO.LOW)
        GPIO.output(ccw2b, GPIO.HIGH)
        GPIO.output(ccw2, GPIO.HIGH)
        pwmccw2.ChangeDutyCycle(t*100)




def setTranslationValue(x, y, t):
    if abs(x) > abs(y):
        if x > 0:
            GPIO.output(c1a, GPIO.HIGH)
            GPIO.output(c1b, GPIO.LOW)
            GPIO.output(c1, GPIO.HIGH)
            pwmc1.ChangeDutyCycle(t*x*100)

            GPIO.output(c2a, GPIO.HIGH)
            GPIO.output(c2b, GPIO.LOW)
            GPIO.output(c2, GPIO.HIGH)
            pwmc2.ChangeDutyCycle(t*100)

            GPIO.output(ccw1a, GPIO.LOW)
            GPIO.output(ccw1b, GPIO.HIGH)
            GPIO.output(ccw1, GPIO.HIGH)
            pwmccw1.ChangeDutyCycle(t*100)

            GPIO.output(ccw2a, GPIO.LOW)
            GPIO.output(ccw2b, GPIO.HIGH)
            GPIO.output(ccw2, GPIO.HIGH)
            pwmccw2.ChangeDutyCycle(t*x*100)
            
        elif x < 0:
            GPIO.output(c1a, GPIO.HIGH)
            GPIO.output(c1b, GPIO.LOW)
            GPIO.output(c1, GPIO.HIGH)
            pwmc1.ChangeDutyCycle(t*100)

            GPIO.output(c2a, GPIO.HIGH)
            GPIO.output(c2b, GPIO.LOW)
            GPIO.output(c2, GPIO.HIGH)
            pwmc2.ChangeDutyCycle(t*x*100)

            GPIO.output(ccw1a, GPIO.LOW)
            GPIO.output(ccw1b, GPIO.HIGH)
            GPIO.output(ccw1, GPIO.HIGH)
            pwmccw1.ChangeDutyCycle(t*x*100)

            GPIO.output(ccw2a, GPIO.LOW)
            GPIO.output(ccw2b, GPIO.HIGH)
            GPIO.output(ccw2, GPIO.HIGH)
            pwmccw2.ChangeDutyCycle(t*100)
            
    elif abs(x) < abs(y):
        low = 60 + (y*100)
        if low > 100:
            low = 100
        if y > 0:
            GPIO.output(c1a, GPIO.HIGH)
            GPIO.output(c1b, GPIO.LOW)
            GPIO.output(c1, GPIO.HIGH)
            pwmc1.ChangeDutyCycle(t*y*100)

            GPIO.output(c2a, GPIO.HIGH)
            GPIO.output(c2b, GPIO.LOW)
            GPIO.output(c2, GPIO.HIGH)
            pwmc2.ChangeDutyCycle(t*100)

            GPIO.output(ccw1a, GPIO.LOW)
            GPIO.output(ccw1b, GPIO.HIGH)
            GPIO.output(ccw1, GPIO.HIGH)
            pwmccw1.ChangeDutyCycle(t*y*100)

            GPIO.output(ccw2a, GPIO.LOW)
            GPIO.output(ccw2b, GPIO.HIGH)
            GPIO.output(ccw2, GPIO.HIGH)
            pwmccw2.ChangeDutyCycle(t*100)
       
        elif y < 0:
            GPIO.output(c1a, GPIO.HIGH)
            GPIO.output(c1b, GPIO.LOW)
            GPIO.output(c1, GPIO.HIGH)
            pwmc1.ChangeDutyCycle(t*100)

            GPIO.output(c2a, GPIO.HIGH)
            GPIO.output(c2b, GPIO.LOW)
            GPIO.output(c2, GPIO.HIGH)
            pwmc2.ChangeDutyCycle(t*y*100)

            GPIO.output(ccw1a, GPIO.LOW)
            GPIO.output(ccw1b, GPIO.HIGH)
            GPIO.output(ccw1, GPIO.HIGH)
            pwmccw1.ChangeDutyCycle(t*100)

            GPIO.output(ccw2a, GPIO.LOW)
            GPIO.output(ccw2b, GPIO.HIGH)
            GPIO.output(ccw2, GPIO.HIGH)
            pwmccw2.ChangeDutyCycle(t*y*100)     


# joystick input values converted to electrical output
        
while True:
    pygame.event.pump()

    # quit
    if joystick.get_button(0):
        print("quit program")
        pwm.ChangeDutyCycle(0)
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
    if (rightJoyX + rightJoyY) != 0:
        setTranslationValue(rightJoyX, rightJoyY, leftJoyY)


print("program was quit")
