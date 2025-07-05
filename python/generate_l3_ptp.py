# Generate standard IP configuration for L3 PTP links
# We use /31 subnets
# Output is a markdown file
import ipaddress
from lib import (
    lab_load_data,
    output_file_path,
    PTP_ROOT_SUBNET,
    PTP_MASK
)

lab_data = lab_load_data()

lab_name = lab_data['name']
output_file = output_file_path(f"{lab_name}_l3_ptp.md")

root_net = ipaddress.IPv4Network(PTP_ROOT_SUBNET)
ptp_subnets = root_net.subnets(new_prefix=PTP_MASK)

intf_data = {} # Key is host

# Get through all links
for link in lab_data['topology']['links']:
    endpoints = link['endpoints']

    if len(endpoints) != 2:
        print(f"W: Only links with two enpoints (PTP) are supported. This one isn't: {endpoints}")
        continue
    
    ptp_subnet = next(ptp_subnets)
    ptp_hosts = ptp_subnet.hosts()

    for endpoint in endpoints:
        addr = next(ptp_hosts)
        host, intf = endpoint.split(":")

        if host not in intf_data:
            intf_data[host] = {} # Key is interface
        
        intf_data[host][intf] = {
            'address' : str(addr) + f"/{PTP_MASK}",
        }

# Generate the output file
output_lines = []
output_lines.append("# L3 PTP interfaces configuration\n")

for host, interfaces in intf_data.items():
    output_lines.append(f"## {host}\n")
    output_lines.append("```")

    for intf, intf_data in interfaces.items():
        output_lines.append(f"interface {intf}")
        output_lines.append(f" ip address {intf_data['address']}")
        output_lines.append("")

    output_lines.append("```\n")

with open(output_file, 'w') as f:
    f.write("\n".join(output_lines))
