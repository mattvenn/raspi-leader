#!/bin/bash
interface=eth1
echo bringing up $interface
sudo ifconfig $interface 192.168.2.1
echo NAT
sudo /sbin/iptables --table nat -A POSTROUTING -o wlan0 -j MASQUERADE
echo dchp server in background
sudo udhcpd udhcpd.conf -S
