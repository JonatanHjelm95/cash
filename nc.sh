#!/bin/bash
nc pwctf.dk 19937
while [ 1 -lt 3 ];
do
	python outputter.py 1234
	i = i+1
#while read l-r ine; do
#	echo -n '$line'
#	python outputter.py 1234
done
