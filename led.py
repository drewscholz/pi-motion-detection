import RPi.GPIO as GPIO
import time


class Led():
    redPin = 11
    greenPin = 13
    bluePin = 15

    def on(pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def off(pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def cleanip():
    mmmmGPIO.cleanup()

    def turn_on_red():
        on(self.redPin)

    def torn_off_red():
        off(self.redPin)

    def flash_green():
        on(self.greenPin)
        off(self.greenPin)

