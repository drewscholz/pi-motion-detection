#!/usr/bin/python3
from datetime import datetime
from PIL import Image
from Led import Led
from Camera import Camera

import os
import time
import subprocess
import pandas as pd

email = "5092880719@vtext.com"
message = "message"
text_message_timeout = 60 * 60 * 2

#sensitivity = 2000
sensitivity_percent = 5
start_time = time.time()

cam = Camera("/home/pi/images")
led = Led()

img_df_1 = cam.get_test_image()
img_size = len(img_df_1.index)
sensitivity = (sensitivity_percent/100) * img_size

print("MOTION DETECTED STARTED")

try:
    led.turn_on('red')
    while True:
        img_df_2 = cam.get_test_image()

        # check for differences in the red
        changed_pixels = compare_img_dfs(img_df_2, img_df_2)

        if changed_pixels > sensitivity:
            led.turn_on('green')
            cam.save_image()
            led.turn_on('red')

            # send text message alert (move to class)
            capture_time = time.time()
            if capture_time - start_time >= text_message_timeout:
                #os.system(mail(email=email, message=message))
                start_time = time.time()
                pass

        img_df_1 = img_df_2

except KeyboardInterrupt:
    led.cleanup()
