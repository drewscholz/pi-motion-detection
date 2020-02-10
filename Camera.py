from io import BytesIO
from datetime import datetime
from PIL import Image
from . import Led

import os
import subprocess


class Camera():

    disk_space_to_reserve = 40 * 1024 * 1024 # Keep 40 mb free on disk

    def capture_test_image(self):
        command = "raspistill -t 1 -w 100 -h 75 -e bmp -o -"
        image_data = BytesIO()
        image_data.write(subprocess.check_output(command, shell=True))
        image_data.seek(0)
        im = Image.open(image_data)
        buffer = im.load()
        image_data.close()
        print(".")
        return im, buffer


    def save_image(self):
        keep_disk_space_free()
        time = datetime.now()
        t = time.strftime("%Y-%m-%d_%H:%M:%S")
        filename = filepath + "/"+ t +".jpg"
        command = "raspistill -t 1 -w 1640 -h 1232 -q 50 -a 12 -e jpg -o %s" % filename
        subprocess.call(command, shell=True)
        print("SAVING IMAGE %s" % filename)

     # Keep free space above given level
    def keep_disk_space_free(self):
        if (get_free_space() < disk_space_to_reserve):
            for filename in sorted(os.listdir(filepath)):
                if filename.startswith("2020") and filename.endswith(".jpg"): # consider a unique filename beginning
                    os.remove(filename)
                    print("Deleted %s to avoid filling disk" % filename)
                    if (get_free_space() > disk_space_to_reserve):
                        return

     # Get available disk space
    def get_free_space(self):
        st = os.statvfs(filepath)
        du = st.f_bavail * st.f_frsize
        return du
