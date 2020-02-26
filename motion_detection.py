#!/usr/bin/python3
from datetime import datetime
from PIL import Image
from Led import Led
from Camera import Camera

import os
import time
import subprocess


# Original code written by brainflakes and modified by pageauc to exit
# image scanning for loop as soon as the sensitivity value is exceeded.
# this can speed taking of larger photo if motion detected early in scan

# Motion detection settings:
# need future changes to read values dynamically via command line parameter or xml file
# --------------------------
# Threshold      - (how much a pixel has to change by to be marked as "changed")
# Sensitivity    - (how many changed pixels before capturing an image) needs to be higher if noisy view
# ForceCapture   - (whether to force an image to be captured every forceCaptureTime seconds)
# filepath       - location of folder to save photos
# filenamePrefix - string that prefixes the file name for easier identification of files.


threshold = 10
sensitivity = 180
force_capture = True
force_capture_time = 60 * 60 # Once an hour

cam = Camera("/home/pi/images")
led = Led()

image1, buffer1 = cam.capture_test_image()

last_capture = time.time()

os.system('clear')
print("MOTION DETECTED STARTED")


try:
    led.turn_on_red()
    while True:
        image2, buffer2 = cam.capture_test_image()
        changed_pixels = 0

        for x in range(0, 100):
            for y in range(0, 75):
                pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])

                if pixdiff > threshold:
                    changed_pixels += 1

            if changed_pixels > sensitivity:
                led.turn_off_red()
                last_capture = time.time()
                led.turn_on_green()
                cam.save_image()
                led.turn_off_green()
                led.turn_on_red()
                break
            continue

        #if force_capture:
            #if time.time() - last_capture > force_capture_time:
                #changed_pixels = sensitivity + 1

        image1  = image2
        buffer1 = buffer2

except KeyboardInterrupt:
    led.cleanup()
