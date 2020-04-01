# pi-motion-detection
Motion detection script for a Raspberry PI with v2 camera


# crontab for web hosting server:
## rsync from pi-cam every minute
* * * * * /home/drew/download_images.py 2>&1

## remove week old images everyday at 1:00 AM
0 1 * * * /home/drew/weekly_cleanup.py 2>&1

# crontab for pi:
## start motion detection script on reboot
@reboot sleep 30 && /home/pi/pi-motion-detection/motion_detection.py 2>&1
