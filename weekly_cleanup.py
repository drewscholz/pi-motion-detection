#!/usr/bin/python3

# script for hosting server that rsyncs the pi cam

from datetime import datetime, timedelta
from dateutil.parser import parse as date_parse
import time
import os

print("Start weekly cleanup")

filepath = "/var/www/img/images"
one_week_ago = datetime.today() - timedelta(days=7)

for filename in sorted(os.listdir(filepath)):
    file_date = filename.split("_")[0]
    file_date = date_parse(file_date)

    if file_date < one_week_ago:
        os.remove(filename)
        print("Removed file %s: ", file_date)

print("End weekly cleanup")
