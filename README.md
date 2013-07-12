# raspi leader

useful stuff for the person running the raspberry pi workshop:

* requirements.txt - necessary files to install
* networkstart.sh - starts the network for dhcp and nat
* udhcpd.conf - config for the dhcp server
* refreshpi.sh - resets all the pis (listed in pis.list)
* pinghosts.sh - can be handy sometimes to keep the hosts up by pinging them

## refreshing the sd card

need to write this up:
http://www.raspberrypi.org/phpBB3/viewtopic.php?f=66&t=11128
use gparted the find size in COUNT mb
dd if=/dev/sdb of=raspi.img bs=1M count=COUNT
