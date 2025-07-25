import os
import sys
from jinja2 import Environment, FileSystemLoader
from .constants import OUTPUT_DIR, BACKUP_DIR, SCRIPT_DIR

def validate_run_env():
    """
    Ensure we run our Python scripts in a working environment
    """
    if os.getcwd().endswith(SCRIPT_DIR):
        print("E: You must run this script in the root directory.")
        exit(1)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
        print(f"I: Generated configuration directory '{OUTPUT_DIR}' created.")
    
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)
        print(f"I: Lab devices backup directory '{BACKUP_DIR}' created.")

def jinja2_render(template_file, data):
    """
    Render Jinja2 template file with provided data
    """
    environment = Environment(loader=FileSystemLoader("arista/"))
    template = environment.get_template(template_file)
    return template.render(data)
