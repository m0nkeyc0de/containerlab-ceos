# cEOS with containerlab
Playing around with *cEOS* and *containerlab*.

## Network topologies

* [test.clab.ym](test.clab.yml) : testing topology
* [l3ls.clab.ym](l3ls.clab.yml) : L3 Leaf-Spine

## Handy commands
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
