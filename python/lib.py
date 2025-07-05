import yaml
import os
import sys

SCRIPT_DIR = "/python"
OUTPUT_DIR = "generated"

PTP_ROOT_SUBNET = "10.1.0.0/16"
PTP_MASK = 31


def lab_load_data():
    """
    Load the lab yaml data
    """
    if os.getcwd().endswith(SCRIPT_DIR):
        print("E: You must run this script in the root directory.")
        exit(1)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    if len(sys.argv) <=1:
        print(f"Usage: {sys.argv[0]} [yourlab.clab.yml]")
        exit(1)

    lab_file = sys.argv[1]
    lab_data = {}

    with open(lab_file, 'r') as f:
        lab_data = yaml.safe_load(f.read())

    return lab_data

def output_file_path(file_name):
    """
    Generate the output file path
    """
    return os.path.join(OUTPUT_DIR, file_name)