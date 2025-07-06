import yaml
import sys

def gen_hostname(lab_name, host):
    """
    Generate hostname for lab host
    """
    return f"clab-{lab_name}-{host}"

def lab_load_data():
    """
    Load the lab yaml data
    """

    if len(sys.argv) <=1:
        print(f"Usage: {sys.argv[0]} [yourlab.clab.yml]")
        exit(1)

    lab_file = sys.argv[1]
    lab_data = {}

    with open(lab_file, 'r') as f:
        lab_data = yaml.safe_load(f.read())

    return lab_data
