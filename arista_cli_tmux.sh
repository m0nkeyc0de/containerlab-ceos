#!/bin/bash 
# Start all lab Arista host shells in TMUX
session_name=clab

tmux kill-session -t ${session_name}

window=0
for container_name in $(sudo docker ps --format '{{.Names}}' | grep clab- | sort); do
   
    window_title=$(echo ${container_name} | rev | cut -d '-' -f1 | rev)

    if [ "$window" -eq "0" ]; then
        tmux new-session -d -s ${session_name} -n ${window_title} "sudo docker container exec -it ${container_name} /usr/bin/FastCli"
    else
        tmux new-window -t ${session_name}:${window} -n ${window_title} "sudo docker container exec -it ${container_name} /usr/bin/FastCli"
    fi
    
    window=$((window+1))
done;

tmux attach-session -t ${session_name}
