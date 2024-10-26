#!/bin/bash

for i in {1..40}; do
    filename="part${i}.txt"
    if [ ! -f "$filename" ]; then
        touch "$filename"
        echo "$filename has been created."
    else
        echo "$filename already exists."
    fi
done
