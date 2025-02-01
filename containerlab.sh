#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Go faster by providing command and topology file in parameters:"
    echo "$0 [deploy|destroy] [topology.clab.yml]"

    sudo docker run --rm -it --privileged \
        --network host \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /var/run/netns:/var/run/netns \
        -v /etc/hosts:/etc/hosts \
        -v /var/lib/docker/containers:/var/lib/docker/containers \
        --pid="host" \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        ghcr.io/srl-labs/clab bash
    
else
    action=$1
    topology=$2

    sudo docker run --rm -it --privileged \
        --network host \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /var/run/netns:/var/run/netns \
        -v /etc/hosts:/etc/hosts \
        -v /var/lib/docker/containers:/var/lib/docker/containers \
        --pid="host" \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        ghcr.io/srl-labs/clab bash -c "containerlab ${action} -t ${topology}"
fi
