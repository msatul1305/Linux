#!/bin/bash
if [ -f .bash_profile ]; then
  echo "You have a .bash_profile. Things are fine."
else
  echo "Yikes! You have no .bash_profile!"
fi
