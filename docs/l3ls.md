# L3 Leaf-Spine
This network has following requirements
* VLAN must be stretched against two datacenter
* We have two physical links to connect the datacenters
* Big remote sites have two routers, each one connected to one of the datacenters
* Tiny remote sites only have one router connected to one datacenter

## Addressing plan

Address | Usage
--- | ---
10.1.0.0/16 | Point-to-point links
169.254.254.254/31 | MLAG interfaces (link-local)