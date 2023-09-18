#!/bin/bash

#for variable in words; do
#    echo "hello"
#done

#word1="1"
#word2="2"
#word3="3"
#for i in $word1 $word2 $word3; do
#    echo "$i"
#done

count=0
for i in $(cat ~/.bashrc); do
    count=$((count + 1))
    echo "Word $count ($i) contains $(echo -n $i | wc -c) characters"
done
