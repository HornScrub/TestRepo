#!/bin/bash

echo "Enter height: "
read height

echo "Enter width: "
read width

for (( i = 1;  i < height; i++ ))
do
    for (( j = 1; j < width; j++ ))
    do
        echo -n "#"
    done
    echo "\n"
done

