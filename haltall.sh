#!/bin/bash
#cmd='parallel-ssh -ih pis.list'
cmd="parallel-ssh -ih pis.list -X -F -X ssh_config"
echo "halt"
$cmd sudo halt
