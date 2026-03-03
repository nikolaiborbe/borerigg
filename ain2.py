import RPi.GPIO as GPIO
import struct
from servo_controller import ServoController

MOUSE_DEVICE = "/dev/input/mice"
angle =50 
sl = 5

GPIO.setmode(GPIO.BOARD)
servo = ServoController(32)
servo.set_pos(angle)

with open(MOUSE_DEVICE, "rb") as f:
    while True:
        data = f.read(3)
        buttons = data[0]

        if buttons & 0x01:
            angle = min(180, angle + sl)
            servo.set_pos(angle)
            print(f"Angle: {angle}")

        if buttons & 0x02:
            angle = max(0, angle - sl)
            servo.set_pos(angle)
            print(f"Angle: {angle}")
