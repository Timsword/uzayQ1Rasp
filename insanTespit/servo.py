# Import libraries
import RPi.GPIO as GPIO
import time

def servoCalistir():
    # Set GPIO numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Set pin 11 as an output, and define as servo1 as PWM pin
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

    # Start PWM running, with value of 0 (pulse off)
    servo1.start(0)

    # Loop to allow user to set servo angle. Try/finally allows exit
    # with execution of servo.stop and GPIO cleanup :)


    #Ask user for angle and turn servo to it
    angle = float(0)
    servo1.ChangeDutyCycle(2+(angle/18))
    time.sleep(1)
    servo1.ChangeDutyCycle(0)
    time.sleep(3)

    angle = float(160)
    servo1.ChangeDutyCycle(2+(angle/18))
    time.sleep(1)
    servo1.ChangeDutyCycle(0)

    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")
