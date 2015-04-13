#!/bin/bash

rm doc/par1/all-results.txt
for bw in 01 1 10 100
do
	for dy in 1ms 5ms 10ms 50ms 100ms 500ms
	do
		echo $bw $dy >> doc/par1/all-results.txt
		for me in 1 10 100
		do
			for size in 10 100 1000 10000
			do
				echo $me $size >> doc/par1/all-results.txt
				awk 'END {print $NF}' doc/par1/$bw-$dy/resultp1-$me-$size.txt >> doc/par1/all-results.txt
			done
		done
		echo  '' >> doc/par1/all-results.txt
	done
done

rm doc/par2/all-results.txt
for bw in 01 1 10 100
do
	for dy in 1ms 5ms 10ms 50ms 100ms 500ms
	do
		echo $bw $dy >> doc/par2/all-results.txt
		for me in 1 10 100
		do
			for size in 10 100 1000
			do
				echo $me $size >> doc/par2/all-results.txt
				awk 'END {print $NF}' doc/par1/$bw-$dy/resultp1-$me-$size.txt >> doc/par2/all-results.txt
			done
		done
		echo '' >> doc/par2/all-results.txt
	done
done
