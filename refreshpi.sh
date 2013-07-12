#!/bin/bash
cmd='parallel-ssh -ih pis.list'
echo "rm all"
$cmd 'rm -rf *'
echo "clone git repo"
$cmd git clone https://github.com/mattvenn/raspi-workshop.git
echo "checking files"
$cmd ls
