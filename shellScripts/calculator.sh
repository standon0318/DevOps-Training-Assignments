#!/bin/sh
echo "Enter Your choice:1:add 2:subtract 3:multiply 4:divide"


 read inputChoice
 echo Enter two Numbers:
 read  firstNum secondNum
 case $inputChoice in
    1)echo  $firstNum + $secondNum | bc
	;;
    2)echo $firstNum - $secondNum | bc
	;;
    3)echo $firstNum \* $secondNum | bc
	;;
    4)echo $firstNum \/ $secondNum | bc
	;;
    *)echo please enter a valid choice
 esac

