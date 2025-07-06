# cEOS with containerlab
Playing around with *cEOS* and *containerlab*.

## Network topologies

* [test.clab.ym](test.clab.yml) : testing topology
* [l3ls.clab.ym](l3ls.clab.yml) : L3 Leaf-Spine

### Underlay addressing plan

Configuration is generated through Python scripts using following addressing plans. Addresses will be distributed in the order things are declared in the lab YAML file.

Subnet | Usage | Interface(s)
--- | --- | ---
10.1.0.0/16 | Point-to-point links (/31) | Ethernet...
10.10.10.0/24 | Underlay loopback interfaces (/32). Also used as router ID. | Loopback10
10.10.11.0/24 | Overlay loopback interfaces (/32) | Loopback20
169.254.254.254/31 | MLAG interfaces (link-local) | Vlan4094


BGP AS range | Usage
--- | ---
64601 - 64699 | Spines
64701 - 64799 | Leafs


### Overlay networks

VRF | VNI | Leafs | Comment
--- | --- | --- | ---
vrf001 | 10001 | leaf1 + leaf2 | Symmetric IRB
vrf002 | 10002 | leaf1 | Asymmetric IRB

VLAN | VNI | Subnet | VRF | Comment
--- | --- | --- | --- | ---
11 | 20011 | 192.168.11.0/24 | vrf001 | leaf1 only 
12 | 20012 | 192.168.12.0/24 | vrf001 | leaf2 only
13 | 20013 | 192.168.13.0/24 | vrf001 | Stretched VLAN
14 | 20014 | 192.168.14.0/24 | vrf001 | Stretched VLAN
21 | 20021 | 192.168.21.0/24 | vrf002 | Stretched VLAN
21 | 20022 | 192.168.22.0/24 | vrf002 | Stretched VLAN

Device | Subnet host IP
--- | ---
vrf | 1
host | host number + 100

## Handy commands
Import docker image
```
sudo docker import cEOS64-lab-4.34.1F.tar.xz ceos64lab:4.34.1F
```

Handy *nmcli* commands
```
nmcli con show
nmcli con add type bridge ifname ceos-operdown
```

Bootstrap python venv

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r python/requirements.txt
```
