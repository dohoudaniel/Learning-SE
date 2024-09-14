#!/usr/bin/env bash

# A simple program to demonstrate for-loops

for n in {1..10}
# Same as for current_num in 1 2 3 4 5 6 7 8 9 10
do
	echo $n
	sleep 1
done

echo "This is outside the for-loop."
