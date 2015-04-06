#!/bin/bash
for bw in 01 1 10 100
do
	for dy in 1ms 5ms 10ms 50ms 100ms 500ms
	do
		mkdir doc/par1/$bw-$dy
		mkdir doc/par2/$bw-$dy
	done
done
