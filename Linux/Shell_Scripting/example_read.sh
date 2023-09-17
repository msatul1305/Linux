#!/bin/bash
#
#echo -n "Enter some text > "
#read text
#echo "You entered: $text"

#read -p "Enter some text > " text
#echo "You entered: $text"

echo -n "Hurry up and type something! > "
if read -t 3 response; then
    echo "Great, you made it in time!"
else
    echo "Sorry, you are too slow!"
fi