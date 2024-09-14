#!/usr/bin/env bash

for file in logfiles/*.log
do
	tar -czvf $file.tar.gz $file 
done
