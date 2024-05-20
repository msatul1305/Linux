- Validating a Phone List With grep
  - for i in {1..10}; do echo "(${RANDOM:0:3}) ${RANDO
    M:0:3}-${RANDOM:0:4}" >> phonelist.txt; done
- validation to scan the file for invalid numbers and display the resulting list:
  - grep -Ev '^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$'
- Finding Ugly Filenames with find
  - find . -regex '.*[^-_./0-9a-zA-Z].*'
- Searching for Files with locate
  - locate --regex 'bin/(bz|gz|zip)'
