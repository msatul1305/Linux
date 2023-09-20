- On most Linux systems a program called bash 
  - which stands for Bourne Again SHell, 
  - an enhanced version of the original Unix shell program, sh, written by Steve Bourne) 
  - acts as the shell program.
- Besides bash, there are other shell programs available for Linux systems.
  - These include: ksh, tcsh and zsh.
- What's a "Terminal?"
  - This is a program that opens a window and lets you interact with the shell.
  - Some Linux distributions install several.
    - These might include gnome-terminal, konsole, xterm, rxvt, kvt, nxterm, and eterm.
- If the last character of your shell prompt is # rather than $, you are operating as the superuser.
- Format of any linux command:
    - command -options arguments
        - eg. ls -l /etc
- File Permissions
  - A representation of the file's access permissions.
  - rw- --- --- = (1,3,3,3) = (type, file's_owner, file's_group, everybody_else)
  - The first character is the type of file.
      - "-" indicates a regular (ordinary) file.
      - "d" indicates a directory.
  - The second set of three characters represent the read, write, and execution rights of the file's owner.
  - The next three represent the rights of the file's group, and
  - the final three represent the rights granted to everybody else.
  - e.g. drwxr-xr-x  6 me me 1024 Oct 9 2019 web_page

-rw-------   1 me       me            576 Apr 17  2019 weather.txt
drwxr-xr-x   6 me       me           1024 Oct  9  2019 web_page
-rw-rw-r--   1 me       me         276480 Feb 11 20:41 web_site.tar
-rw-------   1 me       me           5743 Dec 16  2018 xmas_file.txt

----------     -------  -------  -------- ------------ -------------
    |             |        |         |         |             |
    |             |        |         |         |         File Name
    |             |        |         |         |
    |             |        |         |         +---  Modification Time
    |             |        |         |
    |             |        |         +-------------   Size (in bytes)
    |             |        |
    |             |        +-----------------------        Group
    |             |
    |             +--------------------------------        Owner
    |
    +----------------------------------------------   File Permissions

- ASCII text. ASCII (pronounced "As-Key") is short for American Standard Code for Information Interchange.
    - This is a simple encoding scheme that was first used on Teletype machines to map keyboard characters to numbers.
    - Text is a simple one-to-one mapping of characters to numbers.
    - It is very compact. Fifty characters of text translates to fifty bytes of data.
    - i.e. 1 character = 1 byte data = 8 bits data. that's why ASCII = 8 bits(0 to 2^7 or 127)
- Permissions
  - chmod - modify file access rights
  - su - temporarily become the superuser
  - sudo - temporarily become the superuser
  - chown - change file ownership
    - sudo chown you some_file
  - chgrp - change a file or dir's group ownership
    - chgrp new_group some_file
- rwx rwx rwx = 111 111 111
- rw- rw- rw- = 110 110 110 
- rwx --- --- = 111 000 000 
- rwx = 111 in binary = 7 
- rw- = 110 in binary = 6 
- r-x = 101 in binary = 5 
- r-- = 100 in binary = 4
- common settings
  - 777	(rwxrwxrwx) No restrictions on permissions. Anybody may do anything. Generally not a desirable setting.
  - 755	(rwxr-xr-x) The file's owner may read, write, and execute the file. All others may read and execute the file. This setting is common for programs that are used by all users. 
  - 700	(rwx------) The file's owner may read, write, and execute the file. Nobody else has any rights. This setting is useful for programs that only the owner may use and must be kept private from others. 
  - 666	(rw-rw-rw-) All users may read and write the file. 
  - 644	(rw-r--r--) The owner may read and write a file, while all others may only read the file. A common setting for data files that everybody may read, but only the owner may change.
  - 600	(rw-------) The owner may read and write a file. All others have no rights. A common setting for data files that the owner wants to keep private.
- Becoming the Superuser for a Short While
  - su
  - To exit the superuser session, type exit.
  - In most modern distributions, sudo command us used instead
  - e.g. sudo some_command
  - open root shell:
    - sudo -i
- Job Control
  - ps - list the processes running on the system
  - kill - send a signal to one or more processes (usually to "kill" a process)
  - jobs - an alternate way of listing your own processes
  - bg - put a process in the background
  - fg - put a process in the foreground
- Run GUI processes from terminal
  - xload
  - gedit
  - Putting a Program into the Background(and return terminal to us)
    - xload &
    - or
      - xload 
      - ctrl + z: terminal is returned but process will be suspended and program's window is frozen.
        - i.e. The process still exists, but is idle
      - bg: resumes the process in the background
  - Listing Running Processes
    - jobs: list of the processes we have launched.
    - ps: all processes
  - Killing a process
    - xload &
    - jobs
    - kill %1
    - or
      - xload &
      - ps
      - kill 'id'
    - kill command is used to "kill" processes; its real purpose is to send signals to processes.
    - list of signals to processes:
      - kill -l
    - e.g.
      - 1: SIGHUP - Hang up signal. Programs can listen for this signal and act upon it. This signal is sent to processes running in a terminal when you close the terminal.
      - 2: SIGINT - Interrupt signal. This signal is given to processes to interrupt them. Programs can process this signal and act upon it. We can also issue this signal directly by typing Ctrl-c in the terminal window where the program is running.
      - 15: SIGTERM	- Termination signal. This signal is given to processes to terminate them. Again, programs can process this signal and act upon it. This is the default signal sent by the kill command if no signal is specified.
      - 9: SIGKILL - Kill signal. This signal causes the immediate termination of the process by the Linux kernel. Programs cannot listen for this signal.
    - kill -SIGTERM 'pid'
    - kill -SIGKILL 'pid'
- 