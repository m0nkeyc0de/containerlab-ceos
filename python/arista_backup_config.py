#!/usr/bin/env python3
# Create a copy of startup-config files

import os
import shutil
from libs.constants import BACKUP_DIR
from libs.base import validate_run_env
from libs.containerlab import lab_load_data

validate_run_env()

lab_data = lab_load_data()
lab_name = lab_data['name']

lab_dir = f"clab-{lab_name}"
if not os.path.exists(lab_dir):
    print(f"E: Lab directory {lab_dir} does not exist. Have you started it at least once ?")

for host in lab_data['topology']['nodes']:
    live_config_path = os.path.join(lab_dir, host, "flash/startup-config")
    
    backup_dir = os.path.join(BACKUP_DIR, lab_name)
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

    backup_file = os.path.join(backup_dir, f"{host}_startup-config")

    if os.path.isfile(live_config_path):
        shutil.copyfile(live_config_path, backup_file)
        print(f"I: {live_config_path} backuped.")
