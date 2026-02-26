import RPi.GPIO as GPIO
from time import sleep

class ServoController:
    def __init__(self, pin: int, freq: float = 50,
                 min_duty: float = 2, max_duty: float = 12,
                 min_angle: float = 0, max_angle: float = 180):
        """
        Initilizer for the ServoController

        Params:
            pin: GPIO pin for the raspberry pi.
            freq: PWM frequency in Hz (typically 50 for servos).
            min_duty: Duty cycle % at min_angle (default 2% = ~1ms at 50Hz).
            max_duty: Duty cycle % at max_angle (default 12% = ~2.4ms at 50Hz).
            min_angle: Minimum angle in degrees (default 0).
            max_angle: Maximum angle in degrees (default 180).
        """
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(pin, GPIO.OUT)
        self.servo_pin = pin
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.servo = GPIO.PWM(self.servo_pin, freq)
        self.servo.start(0)
        sleep(0.2)

    def set_pos(self, angle: float):
        """
        Set position of the servo.

        Params:
            angle: Angle between 0 and 180 degrees.
        """
        duty = self._angle_to_duty(angle)
        self.servo.ChangeDutyCycle(duty)
        sleep(0.5)
        self.servo.ChangeDutyCycle(0)

    def _angle_to_duty(self, angle: float) -> float:
        """
        Convert from angle to duty cycle.

        Params:
            angle: Angle between min_angle and max_angle degrees.
        """
        ratio = (angle - self.min_angle) / (self.max_angle - self.min_angle)
        return self.min_duty + ratio * (self.max_duty - self.min_duty)

    def cleanup(self):
        """Stop the servo and clean up GPIO."""
        self.servo.stop()
        GPIO.cleanup()
