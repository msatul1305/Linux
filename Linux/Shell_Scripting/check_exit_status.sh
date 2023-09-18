# Check the exit status

#cd "Atul"
#if [ "$?" = "0" ]; then
#  rm *
#else
#  echo "Cannot change directory!" 1>&2
#  exit 1
#fi

if cd "Atul"; then
  rm ./*
else
  echo "Could not change directory! Aborting." 1>&2
  exit 1
fi
