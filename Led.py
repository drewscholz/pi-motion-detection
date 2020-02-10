import RPi.GPIO as GPIO
import time

class Led():
    redPin = 11
    greenPin = 13
    bluePin = 15

    def on(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def off(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

    def turn_on_red(self):
        self.on(self.redPin)

    def turn_off_red(self):
        self.off(self.redPin)

    def flash_green(self):
        self.on(self.greenPin)
        time.sleep(0.10)
        self.off(self.greenPin)
