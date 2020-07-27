#!/bin/bash

IFACE=$(iw dev|grep "Interface"|sed "s/\Interface //")
#echo $IFACE
sudo iw dev $IFACE scan | egrep "signal:|SSID:|BSS|DS Parameter set:|Authentication suites:"| sed -e "s/\tsignal: //" -e "s/\tSSID: //" -e "s/* Authentication suites: //" -e "s/\tDS Parameter set: //" -e "s/BSS //" -e "s/(on wlp2s0)//"|sort| awk '{printf "\t"$1"\t"}'