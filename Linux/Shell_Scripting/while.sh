#!/bin/bash

number=10
while [ "$number" -lt 10 ]; do
    echo "Number = $number"
    number=$((number + 1))
done

#number=20
#while [ "$number" -gt 10 ]; do
#    echo "Number = $number"
#    number=$((number - 1))
#done

#while [ "$number" -eq 10 ]; do
#    echo "Number = $number"
#    number=$((number + 1))
#done
