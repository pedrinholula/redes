#!/bin/bash
for messages in 1 10 100 1000
do
  for size in 10 100 1000 10000
  do
    python src/par2/client.py $messages $size
  done
done
