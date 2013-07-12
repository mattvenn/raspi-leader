# raspi leader

useful stuff for the person running the raspberry pi workshop:

* requirements.txt - necessary files to install
* networkstart.sh - starts the network for dhcp and nat
* udhcpd.conf - config for the dhcp server, includes static leases for raspi
* refreshpi.sh - resets all the pis (listed in pis.list symlink)
* pinghosts.sh - can be handy sometimes to keep the hosts up by pinging them

pis.list is a symlink to either pis.hostnames (for when raspberrypi1.local is working) or pis.ips for when you have to hard code ips for a network where the avahi lookup stuff doesn't work)


## refreshing the sd card for new images

need to write this up:
http://www.raspberrypi.org/phpBB3/viewtopic.php?f=66&t=11128
use gparted the find size in COUNT mb
dd if=/dev/sdb of=raspi.img bs=1M count=COUNT
