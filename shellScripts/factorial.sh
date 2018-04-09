#!/bin/bash -x
echo "enter the number for factorial"
read number
fact=1
while [ $number -ge 1 ]
do
 fact=`expr $fact \* $number`
 number=`expr $number - 1`
done
echo $fact
