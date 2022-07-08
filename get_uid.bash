#!/bin/bash
count=0
while IFS= read -r line;do
	tgl=`echo $line|awk '{print $2}'`
	count=$(($count + 1 ))
	if [[ "$tgl" == "NEVER" ]]; then
		uidd=`echo $line|awk '{print $3}'|wc -m`
	else
		uidd=`echo $line|awk '{print $4}'|wc -m`
	fi
	if [[ "$uidd" == 37 ]]; then
		echo -e "number ${count} True total uuid ${uidd}"
	else
		echo -e "number ${count} False total uuid ${uidd}"
	fi
done <<< $(cat exp)
