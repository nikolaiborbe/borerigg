# Import libraries
import RPi.GPIO as GPIO
from servo_controller import ServoController
import time

TRIGGER_PIN = 36

def main():

    while GPIO.input(TRIGGER_PIN) == GPIO.HIGH:
        time.sleep(0.05)

    servo = ServoController(32)

    servo.set_pos(0)
    servo.set_pos(180)
    servo.set_pos(90)
    servo.set_pos(45)
    servo.set_pos(30)
    servo.set_pos(20)

    servo.cleanup()


if __name__ == "__main__": 
    main()