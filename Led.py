import RPi.GPIO as GPIO
import time

def verify_color(func):
    def wrapper(self, color):
        try:
            color = str(color).lower
            if color not in self.pins:
                raise
        except:
            raise
        return func(color)
    return wrapper

class Led():
    # redPin = 11
    # greenPin = 13
    # bluePin = 15
    state = None

    pins = {'red': 11, 'green': 13, 'blue': 15}

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
        self.on(self.pins['red'])

    def turn_off_red(self):
        self.off(self.pins['red'])

    def turn_on_green(self):
        self.on(self.pins['green'])

    def turn_off_green(self):
        self.off(self.pins['green'])

    def red_to_green(self):
        self.off(self.pins['red'])
        self.on(self.pins['green'])

    def green_to_red(self):
        self.off(self.pins['green'])
        self.on(self.pins['red'])

    ###########################################

    def turn_off(self):
        if self.state is not None:
            self.off(self.pins.get(self.state))

    #@verify_color
    def turn_on(self, color):
        if self.state is not None:
            self.off(self.pins.get(self.state))
        self.on(self.pins.get(color))
        self.state = color

    #@verify_color
    def change_color(self, color):
        if self.state is not None:
            self.off(self.pins.get(self.state))
        self.on(self.pins.get(color))
        self.state = color


