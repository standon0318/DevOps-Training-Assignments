#!/bin/sh
echo enter three numbers
read firstNum secondNum thirdNum
if [ $firstNum -gt $secondNum -a $firstNum -gt $thirdNum ]
 then
	echo largest Number is: $firstNum
elif [ $secondNum -gt $firstNum -a $secondNum -gt $thirdNum ]
 then
	echo largest Number is: $secondNum
else
	echo largest Number is:$thirdNum
fi

