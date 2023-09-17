#!/bin/bash

function home_space {
    # Only the superuser can get this information

if [ "$(id -u)" = "0" ]; then
    echo "<h2>Home directory space by user</h2>"
    echo "<pre>"
    echo "Bytes Directory"
        du -sh /home/* | sort -nr
    echo "</pre>"
else
    echo "Not root, exiting"
fi

}   # end of home_space

home_space
