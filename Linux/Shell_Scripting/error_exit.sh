# An error exit function

error_exit()
{
  echo "$1" 1>&2
  exit 1
}

# Using error_exit

if cd "Atul"; then
  rm ./*
else
  error_exit "Cannot change directory! Aborting."
fi
