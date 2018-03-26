#!/bin/sh
echo Enter two numbers
read firstNumber
read secondNumber
if ![[ "$firstNumber" =~ ^[0-9]+$ ]]
then
	echo please enter valid numbers

else
	sum=$(expr $firstNumber + $secondNumber)
	echo $sum

fi
