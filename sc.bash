#!/bin/bash
num=0
for uid_acc in $(awk -F '"' '{print $2}' acc); do
#	num=`echo -e "$gr"|awk -F ':' '{print $1}'`
	num=$(($num+1))
	echo -e "$num. "
	while IFS= read -r line; do
		tgl=`echo $line|awk '{print $2}'`
		if [[ "$tgl" == "NEVER" ]]; then
			uidd=`echo $line|awk '{print $3}'`
		else
			uidd=`echo $line|awk '{print $4}'`
		fi
		if [[ "$uidd" == "$uid_acc" ]];then
			echo -e True
		fi
	done <<< $(cat exp)
done
