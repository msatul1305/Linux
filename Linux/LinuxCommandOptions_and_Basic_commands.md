- https://www.linuxcommand.org
- Linux command options, also known as command-line options or flags, 
- are used to modify the behavior of command-line programs in a Linux or Unix-like operating system. 
- These options are typically preceded by a hyphen (-)(Short Options) or double hyphen (--)(Long Options), 
- followed by a letter or a word, and 
- are used to provide additional information or control to a command.
- use ```man "cmd"``` or ```cmd --help``` to get usage info and list of available options for any cmd
- Short Options (Single Hyphen):
  - -a or --all: all
    - ls -a: show hidden files
    - chmod u+rwx,go-w file.txt
  - -b:
  - -c:
    - e.g. ls -CF
    - -c: multi-column output without sorting, arranges the file and directory names in columns to fit the terminal width, making the output more readable. It does not sort the entries alphabetically.
  - -d:
  - -e:
  - -f or --force: forcefully 
    - rm -f: remove without confirmation
    - e.g. ls -CF
      - -F: This option appends a character to the end of each entry to indicate its type:
        - / for directories
        - * for executable files 
        - @ for symbolic links 
        - | for FIFOs (named pipes)
        - = for sockets
  - -g: group
    - chmod u+rwx,go-w file.txt
  - -h: human-readable format
  - -i or --interactive: prompt before executing
    - cp -i or mv -i: prompt before overwriting files
    - grep -i or grep --ignore-case: Ignore the case while searching
      - e.g. grep -i "pattern" file.txt
  - -j:
  - -k:
  - -l or --long: long
    - ls -l: use a long listing format
  - -m:
  - -n or --number: 
    - cat -n file.txt: number all output lines.
  - -o: other
    - chmod u+rwx,go-w file.txt
  - -p or --parents
    - mkdir -p /path/to/new/dir: create parent directories if they don't exist
    - rmdir -p /path/to/empty/dir: remove parent dir if they become empty
  - -q:
  - -r or -R or --recursive: recursive
    - cp -r source_dir dest_dir
    - rm -r or rm -R
  - -s:
  - -t:
  - -u: user  or update
    - chmod u+rwx,go-w file.txt (as user)
    - cp -u *.html destination (as update)
      - it only copies files that either don't exist in the destination directory or 
      - have a newer modification timestamp than their counterparts in the destination directory. 
      - it performs an "update" copy, skipping files that are already up-to-date in the destination.
  - -v:
  - -w:
  - -x:
  - -y:
  - -z:
- Long Options (Double Hyphen)
  - --color: control colorized output
    - ls --color=auto
  - --help: get usage info and list of available options
    - ls --help
  - -name: 
    - find /path/to/search -name "*.txt": search files by name
  - -type
    - search file by type
  - -type d
    - d for directories
- Usage examples:
  1. ls - -l: List the files in the working directory in long format
  2. du - -h: size of bytes in human-readable format
  3. ls - -a: list all hidden files also along with normal files/folders.
- Combination of options:
  - eg. ls -ahl
  - or ls -l -a
- Capital vs small options
  - Linux command options are case-sensitive. 
    - This means the command treats that -A and -a as different options.
  - ls command often accepts options like -l (lowercase) and -L (uppercase) for different purposes:
    - -l: Long format listing. 
    - -L: Follow symbolic links.
  - grep command is case-sensitive when it comes to options. For example:
    - -i: Perform a case-insensitive search. 
    - -I: Interpret files without binary data as text.
- Wildcards
  - select filenames based on patterns of characters.
  - *: Matches any characters 
  - ?: Matches any single character
  - [characters]: Matches any character that is a member of the set characters. 
  - The set of characters may also be expressed as a POSIX character class:
    - [:alnum:]:	Alphanumeric characters
    - [:alpha:]:	Alphabetic characters
    - [:digit:]:	Numerals
    - [:upper:]:	Uppercase alphabetic characters
    - [:lower:]:	Lowercase alphabetic characters
  - [!characters]:	Matches any character that is not a member of the set characters
  - construct very sophisticated selection criteria for filenames:
    - *: All filenames 
    - g*: All filenames that begin with the character "g"
    - b*.txt: All filenames that begin with the character "b" and end with the characters ".txt"
    - Data???: Any filename that begins with the characters "Data" followed by exactly 3 more characters
    - [abc]*: Any filename that begins with "a" or "b" or "c" followed by any other characters
    - [[:upper:]]*: Any filename that begins with an uppercase letter. This is an example of a character class. 
    - BACKUP.[[:digit:]][[:digit:]]: Another example of character classes. This pattern matches any filename that begins with the characters "BACKUP." followed by exactly two numerals.
    - *[![:lower:]]: Any filename that does not end with a lowercase letter.
- Get command help
  - type - Display information about the command type
    - e.g. type type
      - type is a shell builtin
    - type ls
      - ls is aliased to `ls --color=auto'
    - type cp
      - cp is /bin/cp
  - which - Locate a command - To determine the exact location of a given executable 
    - useful if there is more than one version of an executable program installed on a system
    - e.g. which ls
      - /bin/ls
  - help - Display reference page for shell builtin
  - man - Display an on-line command reference
- I/O Redirection
  - redirect the output of many commands to files, devices, and even to the input of other commands.
  - Standard Output to file(file is overwritten eveytime)
    - ls > file_list.txt
  - to append new results to the file instead
    - ls >> file_list.txt
  - Standard Input
    - accept input from a facility called standard input
    - redirect standard input from a file instead of the keyboard
      - sort < file_list.txt
    - redirect standard output to another file like this:
      - sort < file_list.txt > sorted_file_list.txt
  - Pipelines or Pipe (|):
    - connect multiple commands together
    - the standard output of one command is fed into the standard input of another.
    - e.g. ls -l | less
      - less can make any command have scrolling output
    - ls -lt | head	
      - Displays the 10 newest files in the current directory.
    - du | sort -nr	
      - Displays a list of directories and how much space they consume, sorted from the largest to the smallest.
    - find . -type f -print | wc -l	
      - Displays the total number of files in the current working directory and all of its subdirectories.
    - Filters in pipe
      - take standard input and perform an operation upon it and send the results to standard output. 
      - common filters:
        - sort	Sorts standard input then outputs the sorted result on standard output. 
        - uniq	Given a sorted stream of data from standard input, it removes duplicate lines of data (i.e., it makes sure that every line is unique). 
        - grep	Examines each line of data it receives from standard input and outputs every line that contains a specified pattern of characters. 
        - fmt	Reads text from standard input, then outputs formatted text on standard output. 
        - pr	Takes text input from standard input and splits the data into pages with page breaks, headers and footers in preparation for printing. 
        - head	Outputs the first few lines of its input. Useful for getting the header of a file. 
        - tail	Outputs the last few lines of its input. Useful for things like getting the most recent entries from a log file. 
        - tr	Translates characters. Can be used to perform tasks such as upper/lowercase conversions or changing line termination characters from one type to another (for example, converting DOS text files into Unix style text files). 
        - sed	Stream editor. Can perform more sophisticated text translations than tr. 
        - awk	An entire programming language designed for constructing filters. Extremely powerful.
- Expansion
  - echo hello world
    - hello world
  - pathname expansion
    - echo *
      - prints all files and folders in pwd
    - echo D*
      - print all files and folder in pwd starting with D
    - echo *s
      - print all files and folder in pwd ending with s
    - echo [[:upper:]]*
      - starts with uppercase
    - echo ~
      - path of home dir
    - Arithmetic expansion
      - echo 2+2
        - 2+2
      - echo $((2+2))
        - 4
        - Arithmetic expansion uses the form:
          - $((expression))
        - Arithmetic expansion only supports integers (whole numbers, no decimals)
        - echo $(($((5**2)) * 3))
        - Single parentheses may be used to group multiple subexpressions.
          - echo $(((5**2) * 3))
    - Brace Expansion
      - echo Front-{A,B,C}-Back
        - Front-A-Back Front-B-Back Front-C-Back
      - echo Number_{1..5}
        - Number_1 Number_2 Number_3 Number_4 Number_5
      - echo {Z..A}
        - Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
      - echo a{A{1,2},B{3,4}}b
        - aA1b aA2b aB3b aB4b
      - mkdir {2017..2019}-{01..12}
        - create 12*3 dir from 2017-01 to 2019-12
    - Parameter Expansion
      - echo $USER
        - atul
      - list of all variables
        - printenv | less
    - Command Substitution
      - use the output of a command as an expansion:
        - echo $(ls)
        - ls -l $(which cp)
        - file $(ls /usr/bin/* | grep bin/zip)
    - Quoting
      - echo this is a     test 
        - this is a test
      - echo The total is $100.00
        - The total is 00.00
        - substituted an empty string for the value of “$1” because it was an undefined variable
      - Double Quotes
        - If we place text inside double quotes, all the special characters used by the shell lose their special meaning 
        - and are treated as ordinary characters. 
        - The exceptions are “$”, “\” (backslash), and “`” (back-quote).
        - e.g. ls -l "two words.txt"
        - echo "$(cal)"
          - prints calendar
        - echo "this is a     test"
          - this is a     test
      - Single Quotes
        - suppress all expansions
        - echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER 
          - text /home/me/ls-output.txt a b foo 4 me
        - echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"
          - text ~/*.txt {a,b} foo 4 me
        - echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER' 
          - text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
      - Escaping Characters
        - quote a single character
        - done inside double quotes to selectively prevent an expansion
        - using backslash
        - echo "The balance for user $USER is: \$5.00"
          - The balance for user me is: $5.00
        - To allow a backslash character to appear, escape it by typing “\\”.
        - Using the backslash in this way allows us to embed newlines in our command
          - ls -l \
            --reverse \
            --human-readable \
            --full-time
        - echo -e "Inserting several blank lines\n\n\n"
        - echo -e "\aMy computer went \"beep\"."