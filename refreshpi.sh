#!/bin/bash
cmd='parallel-ssh -ih pis.list'
echo "rm all raspi-workshop"
$cmd rm -rf raspi-workshop
echo "clone git repo"
$cmd git clone git@github.com:mattvenn/raspi-workshop
echo "checking files"
$cmd ls
