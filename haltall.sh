#!/bin/bash
cmd='parallel-ssh -ih pis.list'
echo "halt"
$cmd sudo halt
