#!/bin/bash

IFACE=$(iw dev|grep "Interface"|sed "s/\Interface //")
#echo $IFACE
sudo iw dev $IFACE scan | awk '
BEGIN{} 
/BSS [a-z0-9:]{10}/{print ""; printf substr($2,1,17)}
/signal: /{printf "\t"$2"\t"}  
/DS Parameter set/{printf"\t\t"$5}
/SSID: /{printf " \t"$2"\t"}
/WPA:|RSN:|WPE:/{printf "\t"$1}
/* Authentication suites:/{printf $4}' | sort -k 2

