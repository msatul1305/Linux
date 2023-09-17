- [hello_world.sh](hello_world.sh)
  - The first line of the script is a special construct, called a ***shebang*** (#!/bin/bash),
    - given to the system indicating what program is to be used to interpret the script.
  - The second line is a comment. Bash ignores everything that appears after a "#" symbol. 
  - give the shell permission to execute our script
    - chmod 755 hello_world
  - run
    - ./hello_world.sh
- the shell maintains a list of directories where executable files (programs) are kept, 
- and only searches the directories on that list.
- This list of directories is called our path
  - echo $PATH
- add directories to the path
  - export PATH=$PATH:directory
- A better way would be to edit our .bash_profile file to include the above command. 
  - That way, it would be done automatically every time we log in.
- each user has a specific directory for the programs they personally use. 
  - This directory is called bin
- If we move or copy our script into our new bin directory, we'll be all set. Now we just have to type:
  - hello_world
  - and our script will run.
- ENV variables
  - startup -> env var for all users -> env var personal
  - startup files
    - Login shells
      - /etc/profile	A global configuration script that applies to all users.
      - ~/.bash_profile	A user's personal startup file. Can be used to extend or override settings in the global configuration script.
      - ~/.bash_login	If ~/.bash_profile is not found, bash attempts to read this script.
      - ~/.profile	If neither ~/.bash_profile nor ~/.bash_login is found, bash attempts to read this file. This is the default in Debian-based distributions, such as Ubuntu.
      - Non-login shell
        - /etc/bash.bashrc	A global configuration script that applies to all users.
        - ~/.bashrc	A user's personal startup file. Can be used to extend or override settings in the global configuration script.
- update .bashrc
  - vi .bashrc in home of current user e.g. /home/atul
  - edit file
  - quit
  - source .bashrc to get edited updates in current terminal
- Some Edits for .bashrc
  - alias today='date +"%A, %B %-d, %Y"'
  - alias l='ls -l'
- Shell Functions
  - [datetime.sh](datetime.sh)
      ```
      today() {
        echo -n "Today's date is: "
        date +"%A, %B %-d, %Y"
      }```
    %%   a literal %
    %a   locale's abbreviated weekday name (e.g., Sun)
    %A   locale's full weekday name (e.g., Sunday)
    %b   locale's abbreviated month name (e.g., Jan)
    %B   locale's full month name (e.g., January)
    %c   locale's date and time (e.g., Thu Mar  3 23:05:25 2005)
    %C   century; like %Y, except omit last two digits (e.g., 20)
    %d   day of month (e.g., 01)
    %D   date; same as %m/%d/%y
    %e   day of month, space padded; same as %_d
    %F   full date; same as %Y-%m-%d
    %g   last two digits of year of ISO week number (see %G)
    %G   year of ISO week number (see %V); normally useful only with %V
    %h   same as %b
    %H   hour (00..23)
    %I   hour (01..12)
    %j   day of year (001..366)
    %k   hour, space padded ( 0..23); same as %_H
    %l   hour, space padded ( 1..12); same as %_I
    %m   month (01..12)
    %M   minute (00..59)
    %n   a newline
    %N   nanoseconds (000000000..999999999)
    %p   locale's equivalent of either AM or PM; blank if not known
    %P   like %p, but lower case
    %q   quarter of year (1..4)
    %r   locale's 12-hour clock time (e.g., 11:11:04 PM)
    %R   24-hour hour and minute; same as %H:%M
    %s   seconds since 1970-01-01 00:00:00 UTC
    %S   second (00..60)
    %t   a tab
    %T   time; same as %H:%M:%S
    %u   day of week (1..7); 1 is Monday
    %U   week number of year, with Sunday as first day of week (00..53)
    %V   ISO week number, with Monday as first day of week (01..53)
    %w   day of week (0..6); 0 is Sunday
    %W   week number of year, with Monday as first day of week (00..53)
    %x   locale's date representation (e.g., 12/31/99)
    %X   locale's time representation (e.g., 23:13:48)
    %y   last two digits of year (00..99)
    %Y   year
    %z   +hhmm numeric time zone (e.g., -0400)
    %:z  +hh:mm numeric time zone (e.g., -04:00)
    %::z  +hh:mm:ss numeric time zone (e.g., -04:00:00)
    %:::z  numeric time zone with : to necessary precision (e.g., -04, +05:30)
    %Z   alphabetic time zone abbreviation (e.g., EDT)
- Creating variables
  - put a line in the script that contains the name of the variable followed immediately by an equal sign ("="). 
  - No spaces are allowed.
  - [var.sh](var.sh)
  - e.g. name='hello'
    - echo $name
- Variable naming rules
  - Names must start with a letter.
  - A name must not contain embedded spaces. Use underscores instead.
  - Punctuation marks are not permitted.
- Environment Variables
  - When we start our shell session, some variables are already set by the startup files we looked at earlier.
  - To see all the variables that are in the environment, use the printenv command.
  - e.g.
    - SHELL=/bin/bash
    - WSL2_GUI_APPS_ENABLED=1
    - WSL_DISTRO_NAME=Ubuntu-20.04
    - TERMINAL_EMULATOR=JetBrains-JediTerm
    - PWD=/home/atul/IdeaProjects/Linux/Linux/Shell_Scripting
    - HOME=/home/atul
    - LOGNAME=atul
    - USER=atul
    - PATH=/home/atul/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program
    - HOSTTYPE=x86_64
- Functions
  - they must appear before we attempt to use them.
  - the function body (the portions of the function between the { and } characters) must contain at least one valid command. 
  - e.g. [datetime.sh](datetime.sh)
- Flow Control
  - Decisions and actions
    - if
    - test
    - exit
  - if 
      ```
    if commands; then
      commands
      [elif commands; then
      commands...]
      [else
      commands]
      fi
    ```
  - Exit Status
    - Commands and scripts issue a value(int 0-255) to the system when they terminate, called an exit status.
    - indicates the success or failure of the command’s execution
    - zero indicates success, any other value indicates failure
    - command: ```echo $?```
    - [me@linuxbox ~]$ ls -d /usr/bin
      /usr/bin
      [me@linuxbox ~]$ echo $?
      0
      [me@linuxbox ~]$ ls -d /bin/usr
      ls: cannot access /bin/usr: No such file or directory
      [me@linuxbox ~]$ echo $?
      2
  - Test
    - used with if command to perform true/false decisions. 
    - If the given expression is true, test exits with a status of zero; 
    - otherwise it exits with a status of 1.
    - e.g. [check_bash_prof.sh](check_bash_prof.sh)
    - ```
      if [ -f .bash_profile ]; then
      echo "You have a .bash_profile. Things are fine."
      else
      echo "Yikes! You have no .bash_profile!"
      fi
      ```
      - here, -f is used to test if we have a file named bash_profile
      - use of [ expression ] form of the test command
      - the spaces between the "[" and the beginning of the expression are ***required*** and at the end also.
      - The semicolon allows us to put more than one command on a line and works as a command separator.
        - e.g. clear; ls
          - will clear the screen and execute the ls command.
        - Indentation is not necessary but advised for readability.
    - list of the conditions that test can evaluate
      - ```
        -d file	True if file is a directory.
        -e file	True if file exists.
        -f file	True if file exists and is a regular file.
        -L file	True if file is a symbolic link.
        -r file	True if file is a file readable by you.
        -w file	True if file is a file writable by you.
        -x file	True if file is a file executable by you.
        file1 -nt file2	True if file1 is newer than (according to modification time) file2.
        file1 -ot file2	True if file1 is older than file2.
        -z string	True if string is empty.
        -n string	True if string is not empty.
        string1 = string2	True if string1 equals string2.
        string1 != string2	True if string1 does not equal string2.
        ```
    - [check_home_space.sh](check_home_space.sh)
- Debug script
  - add "-x" to the first line of the script
    - #!/bin/bash -x
  - use the set command within the script to turn tracing on and off.
    - Use set -x to turn tracing on and set +x to turn tracing off.
      ```
      #!/bin/bash 
      number=1 
      set -x
      if [ $number = "1" ]; then
      echo "Number equals 1"
      else
      echo "Number does not equal 1"
      fi
      set +x
      ```
  - run script using bash -x script_name.sh
    - bash -x your_script.sh
  - output:
      + number=1
      + '[' 1 = 1 ']'
      + echo 'Number equals 1' 
      + Number equals 1
- Interactive Scripts(Input from user)
  - read
    - To get input from the keyboard
    - [example_read.sh](example_read.sh)
    - "-n" given to the echo command causes it to keep the cursor on the same line
    - "-t" option followed by a number of seconds provides an automatic timeout for the read command
    - -s option causes the user's typing not to be displayed. This is useful when we are asking the user to type in a password or other confidential information.
  - Switch case
    - [case.sh](case.sh)
    - The case command has the following form:
    ```
    case $word in
    patterns ) commands ;;
    esac
    ```
    - Patterns can be literal text or wildcards.
      - We can have multiple patterns separated by the "|" character.
      - [advance_case.sh](advance_case.sh)
  - Loops
    - while, until and for.
    - while
      - [while.sh](while.sh)
        - "-lt" = less than
        - -eq: Equal to
        - -ne: Not equal to
        - -gt: Greater than
        - -ge: Greater than or equal to
        - -lt: Less than
        - -le: Less than or equal to
    - until
      - The until command works exactly the same way, except the block of code is repeated as long as the specified command's exit status is false
      - [until.sh](until.sh)
      - [menu.sh](menu.sh)
- Arithmetic
  - [Arithmetic.sh](Arithmetic.sh)
- Positional Parameters
  - [me@linuxbox me]$ some_program word1 word2 word3
    - $0 would contain "some_program"
    - $1 would contain "word1"
    - $2 would contain "word2"
    - $3 would contain "word3"
    - [pos.sh](pos.sh)
- Command Line Options
  - [clo.sh](clo.sh)
  - shift is a shell builtin that operates on the positional parameters. 
  - Each time we invoke shift, it "shifts" all the positional parameters down by one. 
    - $2 becomes $1, $3 becomes $2, $4 becomes $3, and so on.
  - [shift.sh](shift.sh)
- Getting an Option's Argument
  - 