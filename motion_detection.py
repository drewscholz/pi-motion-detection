#!/usr/bin/python3

from datetime import datetime
from PIL import Image
from Led import Led
from Camera import Camera

import os
import time
import subprocess
import pandas as pd

#email = "#@vtext.com"
#message = "message"
#text_message_timeout = 60 * 60 * 2

#old sensitivity ~2000
sensitivity_percent = 10
#start_time = time.time()

cam = Camera("/home/pi/images")
led = Led()

img_df_1 = cam.get_test_image()

img_size = len(img_df_1.index)
print('img_size: ', img_size)
sensitivity = (sensitivity_percent/100) * img_size
print('sensitivity: ', sensitivity)
print("MOTION DETECTED STARTED")

try:
    led.turn_on('red')
    while True:
        img_df_2 = cam.get_test_image()

        changed_pixels= (abs(img_df_1['red'] - img_df_2['red']) > 4).sum()
        #print('changed pixels: ', changed_pixels)
        if changed_pixels > sensitivity:
            led.turn_on('green')
            cam.save_image()
            led.turn_on('red')
            #print(img_df_1)
            #print(img_df_2)
            # send text message alert (move to class)
            #capture_time = time.time()
            #if capture_time - start_time >= text_message_timeout:
                #os.system(mail(email=email, message=message))
                #start_time = time.time()
                #pass

        img_df_1 = img_df_2

except KeyboardInterrupt:
    led.cleanup()
