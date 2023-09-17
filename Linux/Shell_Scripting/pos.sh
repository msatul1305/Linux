#!/bin/bash

#echo "Positional Parameters"
#echo '$0 = ' $0
#echo '$1 = ' $1
#echo '$2 = ' $2
#echo '$3 = ' $3

if [ $# -gt 0 ]; then
    echo "Your command line contains $# arguments"
else
    echo "Your command line contains no arguments"
fi