#!/bin/bash

rm p2r2.csv
for bw in 01 1 10 100
do
	for dy in 1ms 5ms 10ms 50ms 100ms 500ms
	do
		echo $bw $dy >> p2r2.csv
		echo "messages	10	100	1000" >> p2r2.csv
		for me in 1 10 100
		do
			echo -n "$me	" >> p2r2.csv
			for size in 10 100 1000
			do
				awk 'END {printf "%f\t", $NF}' $bw-$dy/resultp2-$me-$size.txt >> p2r2.csv
			done
			echo '' >> p2r2.csv
		done
	done
done
