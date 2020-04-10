#!/usr/bin/python3

from datetime import datetime
from PIL import Image
from Led import Led
from Camera import Camera

import os
import time
import subprocess
import pandas as pd
import cv2

#email = "#@vtext.com"
#message = "message"
#text_message_timeout = 60 * 60 * 2

#old sensitivity ~2000
#sensitivity_percent = 10
#start_time = time.time()

cam = Camera("/home/pi/images")
led = Led()

min_threshold = 100
max_threshold = 170

img1 = cam.get_test_image()

#img_size = len(img_df_1.index)
#print('img_size: ', img_size)
#sensitivity = (sensitivity_percent/100) * img_size
#sensitivity = (sensitivity_percent/100) * img_df_1.size # not right
#print('sensitivity: ', sensitivity)
print("MOTION DETECTED STARTED")

try:
    led.turn_on('red')
    while True:
        img2 = cam.get_test_image()

	# image subtraction
        img_sub = cv2.subtract(img1, img2)
        
        # smooth the image
        #img = cv2.blur(img, (5,5))
        #img = cv2.medianBlur(img, 5) # salt and pepper
        #img_smooth = cv2.GaussianBlur(img_sub, (3,3), 0)
        
        # convert image to binary
        #ret3, thres_img = cv2.threshold(img_smooth, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        # Canny edge detection to outline object and convert image to binary
        edges = cv2.Canny(img_sub, min_threshold, max_threshold)
        
        # Find contour lines from object
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #print(f'num contours: {len(contours)}')
        
        # Filter contour lines by area
        #contours_area = []
        #for contour in contours:
            #area = cv2.contourArea(contour)
            #print(area)
            #if 300 < area:
                #contours_area.append(contour)
        #print(f'num contour area: {len(contours_area)}')

        if len(contours) > 0:
            led.turn_on('green')
            cam.save_image()
            led.turn_on('red')

            # send text message alert (move to class)
            #capture_time = time.time()
            #if capture_time - start_time >= text_message_timeout:
                #os.system(mail(email=email, message=message))
                #start_time = time.time()
                #pass

        img1 = img2

except KeyboardInterrupt:
    led.cleanup()
