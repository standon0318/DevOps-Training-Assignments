#!/bin/sh
echo "enter the number to reverse"
read inputNumber
rev=0;
while [ $inputNumber -gt 0 ]
do 
	rem=$(( $inputNumber % 10))
	rev=$(( $rev *\ 10 + $rem ))  
	inputNumber=$(( $inputNumber / 10))
done
echo "the reverse number is $rev"
