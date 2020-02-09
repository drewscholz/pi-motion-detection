#!/usr/bin/python3
from io import BytesIO
from datetime import datetime
from PIL import Image
from . import Led

import os
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
filepath = "/home/pi/images"
disk_space_to_reserve = 40 * 1024 * 1024 # Keep 40 mb free on disk

# Capture a small test image to stdout and save to variable buffer
def capture_test_image():
    command = "raspistill -t 1 -w 100 -h 75 -e bmp -o -"
    image_data = BytesIO()
    image_data.write(subprocess.check_output(command, shell=True))
    image_data.seek(0)
    im = Image.open(image_data)
    buffer = im.load()
    image_data.close()
    print(".")
    return im, buffer

# Save a higher quality image to disk
def save_image():
    keep_disk_space_free()
    time = datetime.now()
    t = time.strftime("%Y-%m-%d_%H:%M:%S")
    filename = filepath + "/"+ t +".jpg"
    command = "raspistill -t 1 -w 1640 -h 1232 -q 50 -a 12 -e jpg -o %s" % filename
    subprocess.call(command, shell=True)
    print("SAVING IMAGE %s" % filename)

# Keep free space above given level
def keep_disk_space_free():
    if (get_free_space() < disk_space_to_reserve):
        for filename in sorted(os.listdir(filepath)):
            if filename.startswith("2020") and filename.endswith(".jpg"): # consider a unique filename beginning
                os.remove(filename)
                print("Deleted %s to avoid filling disk" % filename)
                if (get_free_space() > disk_space_to_reserve):
                    return

# Get available disk space
def get_free_space():
    st = os.statvfs(filepath)
    du = st.f_bavail * st.f_frsize
    return du

# Get first image
image1, buffer1 = capture_test_image()

# Reset last capture time
last_capture = time.time()

os.system('clear')
print("MOTION DETECTED STARTED")

while True:

    # Get comparison image
    image2, buffer2 = capture_test_image()

    # Count changed pixels
    changed_pixels = 0
    for x in range(0, 100):
        # Scan one line of image then check sensitivity for movement
        for y in range(0, 75):
            # Just check green channel as it's the highest quality channel
            pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])

            if pixdiff > threshold:
                changed_pixels += 1

        # If movement sensitivity exceeded then
        # save image and Exit before full image scan complete
        if changed_pixels > sensitivity:
            last_capture = time.time()
            save_image()
            break
        continue

    # Check force capture
    if force_capture:
        if time.time() - last_capture > force_capture_time:
            changed_pixels = sensitivity + 1

    # Swap comparison buffers
    image1  = image2
    buffer1 = buffer2

