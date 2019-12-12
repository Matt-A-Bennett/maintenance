#!/bin/bash

#sshcism

used=$(ssh mbennett@storage.cism.ucl.ac.be "df | grep ions ")
used=$(echo $used | awk '{print $5}' | cut -c 1-2)

if [[ used -gt 80 ]]; then
	if [[ used -gt 90 ]]; then
		level="warning"
	else
		level="critical"
	fi	
	echo "$level: cism storage is at $used% ($(date))" >> ~/monitor.log
fi
