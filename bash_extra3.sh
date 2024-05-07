#!/bin/bash

echo -n "What's up? Enter a number: "

read number
number2

if [ $((number % 2)) -eq 0 ] 
then
    number2 -eq [ number / 2 ]
    echo "$number times 4 equals $number2"
else
    number2 -eq [ number / 2 ]
    echo "$number divided by 2 equals $number2"
fi

