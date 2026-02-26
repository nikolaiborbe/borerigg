# Import libraries
import RPi.GPIO as GPIO
from servo_controller import ServoController
import time

servo = ServoController(32)
servo.set_pos(0)
servo.set_pos(180)
servo.set_pos(90)
servo.set_pos(45)
servo.set_pos(30)
servo.set_pos(20)

servo.cleanup()