#!/bin/bash


numbers=(3 8 15 100)

largest=${numbers[0]}

for number in "${numbers[@]}";
do
    if [ $number -gt $largest ];then
    largest=$number
    fi
done

echo "Largest number is $largest"

numbers1=(901 19 1 39)
numbers2=(32 11 102 34)

largest=${numbers1[0]}

for ((i=0;i < ${#numbers1[@]};i++));
do
    if [ ${numbers1[i]} -gt $largest ];then
    largest=${numbers1[i]}
    fi
    if [ ${numbers2[i]} -gt $largest ];then
    largest=${numbers2[i]}
    fi
done

echo "Largest number is of two arrays is $largest"