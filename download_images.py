#!/usr/bin/python3

import os
import subprocess

# fill in these
user = 'user_name'
host = '192.168.*.*'
pi_image_dir = "from image directory"
web_host_image_dir = "to images directory"
ssh_public_key_name = "id_rsa"

command = f'/usr/bin/rsync -e "ssh -i ~/.ssh/{ssh_public_key_name} -v" -avz {user}@{host}:{pi_image_dir} {web_host_image_dir} 2>&1'

print(command)

os.system(command)
