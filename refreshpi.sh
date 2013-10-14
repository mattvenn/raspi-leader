#!/bin/bash

#the -X is about passing in the -F ssh_config, -x didn't work because of quoting issues
cmd="parallel-ssh -ih pis.list -X -F -X ssh_config"
#cmd='parallel-ssh -ih pis.list'

echo "rm all"
$cmd 'rm -rf *'
echo "clone git repo"
$cmd git clone https://github.com/mattvenn/raspi-workshop.git
echo "checking files"
$cmd ls
echo "turning on all outputs"
$cmd sudo python /home/pi/raspi-workshop/flash_led/all_on.py
