#!/bin/bash

for size in 10 100 1000 10000
do
	echo "size: $size"
	echo 'delay	0,1	1	10	100'
	for dy in 1ms 5ms 10ms 50ms 100ms 500ms
	do
		echo -n "$dy	"
		for bw in 01 1 10 100
		do
			awk 'END {printf "%f\t", $NF}' $bw-$dy/resultp2-1-$size.txt
		done
		echo ''
	done
	echo ''
done
