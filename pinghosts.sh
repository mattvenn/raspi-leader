#!/bin/bash
while true; do
    for i in $(seq 5 ); do
        ping -qc 1 raspberrypi$i.local
    done
    sleep 5 
done
