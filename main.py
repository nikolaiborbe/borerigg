import RPi.GPIO as GPIO
from servo_controller import ServoController
from time import sleep

TRIGGER_PIN = 36

def main():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while GPIO.input(TRIGGER_PIN) == GPIO.HIGH:
        sleep(0.05)

    servo = ServoController(32)

    servo.set_pos(0)
    servo.set_pos(180)
    servo.set_pos(90)
    servo.set_pos(45)
    servo.set_pos(30)
    servo.set_pos(20)

    servo.cleanup()

    sleep(1)


if __name__ == "__main__": 
    while True:
        main()