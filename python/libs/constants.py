# Directories and files used by the scripts
SCRIPT_DIR = "/python"  # Where Python code resides
OUTPUT_DIR = "generated"  # Folder for generated configuration output
BACKUP_DIR = "backups"  # Folder for lab configuration backups
CREDS = "arista.yml.secret"

# Container lab fixed stuff
MGMT_SUBNET = "172.20.20.0/24"

# Regular expressions to differentiate devices roles ffrom name
RE_SPINE = r"^(.*)?spine.*" # Spines
RE_LEAF = r"^(.*)?leaf.*" # leafs
RE_HOST = r"^(.*)?host.*" # hosts

# L3 point-to-point links
PTP_ROOT_SUBNET = "10.1.0.0/16"
PTP_MASK = 31
