# pi-motion-detection
Motion detection script for a Raspberry PI with v2 camera

Raspi will continually take low resolution images and compare then to identify motion using opencv

Once motion is detected it will save a high resolution image

LED will remain red while the motion detection script is running and flash green while saving an image

Additional web server will rsync the raspi image directory regularly to keep an update list of image for the admin to view

Raspi has a cronjob to clean out the image directory once a day for 3 day old images

Motion detection script will check memory before saving to avoid accidentally bricking itself

Use in conjunction with the gallery app on the web server to view the raspi images
