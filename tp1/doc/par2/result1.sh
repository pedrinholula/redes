#!/bin/bash

rm p2r1.csv
for size in 10 100 1000
do
	echo "size: $size" >> p2r1.csv
	echo 'delay	0,1	1	10	100' >> p2r1.csv
	for dy in 1ms 5ms 10ms 50ms 100ms 500ms
	do
		echo -n "$dy	" >> p2r1.csv
		for bw in 01 1 10 100
		do
			awk 'END {printf "%f\t", $NF}' $bw-$dy/resultp2-1-$size.txt >> p2r1.csv
		done
		echo '' >> p2r1.csv
	done
	echo '' >> p2r1.csv
done
