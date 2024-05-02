#!/bin/bash

echo "Please enter a number: "
read number


if [ $((number % 2)) -eq 0 ]
then
    echo "$number is even"
else
    echo "It's odd"
fi

