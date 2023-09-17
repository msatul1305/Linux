#!/bin/bash

tomorow() {
  echo -n "Today's date is: "
  date +"%A, %B %-d, %Y"
}
tomorow
right_now="$(date +"%x %r %Z")"
#echo $right_now
rn=`date +"%x %r %Z"`
#echo $rn
