#!/usr/bin/awk -f

# Print a directory report

BEGIN {
    print "Directory Report"
    print "================"
}

NF > 9 {
    print $9, "is a symbolic link to", $NF
}

END {
    print "============="
    print "End Of Report"
}
