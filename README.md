# cEOS with containerlab
Playing around with *cEOS* and *containerlab*.

Network topologies

* `test.clab.yml` : random tests

Configuration files

* `et_mapping.json` : container to EOS interface mappping file which uses the *et* scheme
* `base-startup-config.tpl` : custom base configuration adapted from the original file from the containerlab project

Bash scripts

* `containerlab.sh` : helper script to start containerlab
* `arista_cli_tmux.sh` : open all clab container shells in a tmux session

Python scripts

* ``

Bootstrap python

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

