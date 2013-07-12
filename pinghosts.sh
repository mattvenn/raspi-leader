#!/bin/bash
while true; do
    for pi in $(cat pis.list | sed -e 's/pi@//'); do
        ping -qc 1 $pi
    done
    echo wait ===================
    sleep 5 
done
