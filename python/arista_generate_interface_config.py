#!/usr/bin/env python3
# Generate interfaces configuration
# TODO: MLAG ? PortChannel ? We'll see later

import ipaddress
import os
import re
import copy

from libs.base import validate_run_env
from libs.containerlab import lab_load_data
from libs.constants import (
    OUTPUT_DIR,
    PTP_ROOT_SUBNET,
    PTP_MASK,
    RE_LEAF,
    RE_SPINE,
    RE_HOST,
)

validate_run_env()

lab_data = lab_load_data()
lab_name = lab_data['name']

output_file = os.path.join(OUTPUT_DIR, f"{lab_name}_interfaces.md")

root_net = ipaddress.IPv4Network(PTP_ROOT_SUBNET)
ptp_subnets = root_net.subnets(new_prefix=PTP_MASK)

host_data = {} # Key is host

# Get through all links
for link in lab_data['topology']['links']:
    endpoints = link['endpoints']

    # Point-to-point links obviously only have two endpoints
    if len(endpoints) != 2:
        print(f"W: Only links with two enpoints (PTP) are supported. This one isn't: {endpoints}")
        continue

    host_found = False
    leaf_found = False
    spine_found = False

    for endpoint in endpoints:
        host = endpoint.split(":")[0]
        
        if re.match(RE_HOST, host):
            host_found = True

        if re.match(RE_LEAF, host):
            leaf_found = True

        if re.match(RE_SPINE, host):
            spine_found = True

    # L3 Leaf-Spine topology links kinds
    # - leaf-spine : L3
    # - leaf-host : L2
    # - leaf-leaf : L2 (MLAG)
    # - spine-spine : L3 (backbone)
    link_is_l3 = (leaf_found and spine_found) or (spine_found and not host_found)

    ptp_subnet = next(ptp_subnets) if link_is_l3 else None
    ptp_hosts = ptp_subnet.hosts() if ptp_subnet else None

    for endpoint in endpoints:
        intf_data = {}
        host, intf = endpoint.split(":")

        if link_is_l3:
            addr = next(ptp_hosts)
            intf_data['address'] = str(addr) + f"/{PTP_MASK}"

        if host not in host_data:
            host_data[host] = {
                'interfaces' : {}, # Key is interface
            }

        # Get other endpoint for description
        tmp_endpoints = copy.copy(endpoints)
        tmp_endpoints.remove(endpoint)
        intf_data['description'] = tmp_endpoints[0]
        
        host_data[host]['interfaces'][intf] = intf_data

# Generate the output file
# TODO jinja2 ?
output_lines = []
output_lines.append(f"# Lab {lab_name} - Interfaces configuration\n")

for host, data in host_data.items():
    output_lines.append(f"## {host}\n")
    output_lines.append("```")

    for intf, intf_data in data['interfaces'].items():
        intf_ip_address = intf_data.get('address')
        intf_description = intf_data.get('description')

        output_lines.append(f"interface {intf}")

        if intf_description:
            output_lines.append(f" description {intf_description}")
        else:
            output_lines.append(" no description")

        if intf_ip_address:
            output_lines.append(" no switchport")
            output_lines.append(f" ip address {intf_ip_address}")

        else:
            output_lines.append(" no ip address")
            output_lines.append(" switchport")

        output_lines.append("")

    output_lines.append("```\n")

with open(output_file, 'w') as f:
    f.write("\n".join(output_lines))
