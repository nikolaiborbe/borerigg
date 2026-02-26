import RPi.GPIO as GPIO
from servo_controller import ServoController
import time

GPIO.setmode(GPIO.BOARD)

TRIGGER_PIN = 36

GPIO.setup(TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
    GPIO.cleanup()


if __name__ == "__main__": 
    while True:
        main()