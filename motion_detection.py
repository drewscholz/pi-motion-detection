#!/usr/bin/python3
from datetime import datetime
from PIL import Image
from Led import Led
from Camera import Camera

import os
import time
import subprocess
import pandas as pd


# Threshold      - (how much a pixel has to change by to be marked as "changed")
# Sensitivity    - (how many changed pixels before capturing an image) needs to be higher if noisy view

# threshold = 10
# sensitivity = 180

sensitivity = 2000

cam = Camera("/home/pi/images")
led = Led()

img_df_1 = cam.get_test_image()
# ToDo: grab pixel count and calculate a percentage for sensitivity

print("MOTION DETECTED STARTED")

try:
    led.turn_on_red()
    while True:
        img_df_2 = cam.get_test_image()

        # check for differences in the red
        changed_pixels = (img_df_1['red'] != img_df_2['red']).any(1)

        if changed_pixels > sensitivity:
            led.turn_off_red()
            led.turn_on_green()
            cam.save_image()
            led.turn_off_green()
            led.turn_on_red()

        img_df_1 = img_df_2

except KeyboardInterrupt:
    led.cleanup()
