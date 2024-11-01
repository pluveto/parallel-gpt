#!/bin/bash

start=$1
end=$2

if [ -z "$start" ]; then
    echo "Please provide the starting index."
    exit 1
fi
if [ -z "$end" ]; then
    echo "Please provide the ending index."
    exit 1
fi

for i in $(seq $start $end); do
    filename="part${i}.txt"
    if [ ! -f "$filename" ]; then
        touch "$filename"
        echo "$filename has been created."
    else
        echo "$filename already exists."
    fi
done
