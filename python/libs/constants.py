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

MLAG_SUBNET = "169.254.254.254/31"
MLAG_VLAN = 4094

HOST_LOOPBACK = 10
HOST_LOOPBACK_SUBNET = f"10.10.{HOST_LOOPBACK}.0/24"
SVC_LOOPBACK = 11
SVC_LOOPBACK_SUBNET = f"10.10.{SVC_LOOPBACK}.0/24"

SPINE_AS_NUMBERS = range(64601, 64700)
LEAF_AS_NUMBERS = range(64701, 64800)