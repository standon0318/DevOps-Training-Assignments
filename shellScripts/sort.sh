#!/bin/bash
echo "enter 5 numbers to sort"
for (( i = 0; i < 5; i++ ))
do
read numbers[$i]
done
   for (( i = 0; i < 5 ; i++ ))
do
     for (( j = 0; j < 5 ; j++ ))
do
  if [ ${numbers[$i]} -lt ${numbers[$j]} ]
    then
	temp=${numbers[$i]}
	numbers[$i]=${numbers[$j]}
	numbers[$j]=$temp
fi
     done
  done

for (( i=0; i < 5 ; i++ ))
do
echo ${numbers[$i]}
done
