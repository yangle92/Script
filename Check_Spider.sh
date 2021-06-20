#!/bin/bash

flg=`date '+%Y%m%d%H%M%S'`

if [ ! -d /root/data/log ]; then 
	mkdir /root/data/log
fi

if  [ `ps -ef | grep Spider_CDSN.py |grep -v 'grep' |wc -l` == 0 ]; then
	/usr/bin/python3 /root/data/Spider_CDSN.py >/root/data/log/log$flg 2>&1
fi
