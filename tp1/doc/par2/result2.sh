#!/bin/bash

rm all-results.csv
for bw in 01 1 10 100
do
	for dy in 1ms 5ms 10ms 50ms 100ms 500ms
	do
		echo $bw $dy
		echo "messages	10	100	1000	10000"
		for me in 1 10 100
		do
			echo -n "$me	"
			for size in 10 100 1000
			do
				awk 'END {printf "%f\t", $NF}' $bw-$dy/resultp2-$me-$size.txt
			done
			echo ''
		done
	done
done
