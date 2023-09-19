- AWK
  - http://linuxcommand.org/lc3_adv_awk.php
  - developed in the late 1970’s at Bell Telephone Laboratories by Alfred Aho, Peter Weinberger, and Brian Kernighan. 
  - The name “AWK” comes from the last names of the three authors. 
  - a standard program found in almost every Linux distribution. 
  -  $0 signifies the entire record.
- Variable $1 is the first field(column), $2 is the second field, and so on.
- e.g. 
  - ls -l /usr/bin | awk '{print $0}'
  - ls -l /usr/bin | awk 'NF > 9 {print $0}'
    - print lines with more than 9 fields
    - list of symbolic links in /usr/bin since those directory listings contain more than 9 fields and files with spaces
  - [awk_example.sh](awk_example.sh)
  - /regular-expression/
    ```
      ls -l /usr/bin | awk '
      $1 ~ /^-/ {t["Regular Files"]++}
      $1 ~ /^d/ {t["Directories"]++}
      $1 ~ /^l/ {t["Symbolic Links"]++}
      END {for (i in t) print i ":\t" t[i]}
    ```
  - basic syntax of the awk command:
    - awk 'pattern { action }' input-file
  - Examples
    - Printing Columns from a Text File:
      - awk '{ print $2 }' data.txt
    - Filtering Data Based on a Condition:
      - awk '$3 > 50 { print $1, $3 }' data.txt 
    - Calculating Sum or Average:
      - awk '{ sum += $2 } END { print "Total:", sum, "Average:", sum/NR }' data.txt
    - Changing Field Separators:
      - awk -F',' '{ print $1 }' data.csv
    - Using BEGIN and END Blocks:
      - awk 'BEGIN { print "Header" } { print $0 } END { print "Footer" }' data.txt
    - Counting Lines Matching a Pattern:
      - awk '/pattern/ { count++ } END { print "Count:", count }' data.txt
    - Formatting and Reordering Columns:
      - awk '{ print $2, $1 }' data.txt
    ~ ChatGPT
