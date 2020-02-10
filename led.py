import RPi.GPIO as GPIO


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
        on(self.redPin)

    def turn_off_red(self):
        off(self.redPin)

    def flash_green(self):
        on(self.greenPin)
        off(self.greenPin)
