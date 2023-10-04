1. df - Th: No of Partitions/My Computer of Linux
   - df = Disk Free/Disk Full
   - drive space
   - -T: type of file
   - -h: human readable
   - commonly used to check the overall disk space usage on a system
   - and to monitor the available space on different partitions or file systems.
2. cd - change directory, md - make directory
3. ls - list (ls -a: all files(show hidden files))
4. pwd - present working directory
5. man - manual
6. clear / ctrl+l: clear terminal
7. cat: read a file(Concatenate files)
   - reads one or more files and copies them to standard output
   - cat can accept more than one file as an argument, it can also be used to join files together
   - join together all files with name mpg.0* to movie.mpeg
     - cat movie.mpeg.0* > movie.mpeg
8. mkdir: make directory
9. su -i: change to root user
10. su - "username": change current user
11. sudo adduser mynewuser:
    - create a new user 
    - prompted to enter the new user's password and other information, such as their full name and additional details.
    - new user account will be created along with /home directory
    - To grant administrative privileges (sudo access) to the new user, add them to the sudo group.
      - sudo usermod -aG sudo newusername
    - switch to the new user account
      - su - newusername
12. ctrl+ d/logout/exit: logout
13. DON'T USE: rm -rvf /
14. touch: create a new file if the file is non-existing or update the timestamp if the file already exists
15. vi/vim for redhat and nano for debian: edit files
16. systemctl status/stop/start "sshd"- check status/start/stop of sshd service
17. wall - broadcast message to all logged-in users
18. In WWindows to Restart wireless network: ncpa.ctl
19. w: list of all logged-in users
20. ps:
    - Report a snapshot of current processes
    - get my processes/machine number... 
    - ps -aux
21. ifup ens33 and ifdown ens33: to connect/disconnect system to network
22. wc: word count
    - wc file.txt
      - output: 10  50 300 file.txt(i.e. number of lines, words, and bytes contained in files)
        - The first number represents the line count (10 lines).
        - The second number represents the word count (50 words).
        - The third number represents the character count (300 characters).
      - wc -l file.txt
        - Count only the lines in a file:
      - echo "This is a sample text." | wc
        - Count lines, words, and characters from standard input (typing directly into the terminal)
        - o/p: 1   5  23
23. free /free -h: get ram status
24. ssh vssut@10.208.34.9
25. command | ps wc -l: count no of things in a list	
26. top: 
    - View Processes Dynamically
    - view your system’s resource usage and see the processes that are taking up the most system resources. 
    - It displays a list of processes, with the ones using the most CPU.
27. VIM COMMANDS
    - get out of vi: esc->:q or:q!(forcefully quit)
    - insert in vim: press i
    - w: write 
    - wq: save and exit
    -:set nu: show line numbers (lines nos will be displayed)
    - ?"text": search a particular text in the file
    -:%s/"oldtext"/"newtext": search and replace all
28. head -n "10" "filename": display first 10 lines 
29. tail -n "10" "filename": display last 10 lines
30. more/less "filename": read a file
31. head -n 50 | tail -n 15: display line 35 to 50  
    - 1st find first 50 lines and then show last 15 lines of that first 50 lines
32. tar -zxvf "filename" - Tape-archiving utility
    - extract archive files (zxvf-> z:gzip,x:extract,v:verbose,f:bzip2)
    - unzip file.zip - extract the files from zip
    - tar tzvf name_of_file.tar.gz | less - View the contents of tar files
33. cp "vss.txt" "/home/msatul1305/Desktop" -v: copy from current directory to new directory -v=>verbose(show copied acknowledgement)
34. ".": current directory
35. "..": parent directory
36. cp -r: copy a folder (recursive)
37. rm: remove/delete file
    - rm *~: Delete all files in the current working directory that end with the character "~". 
      - Some applications create backup files using this naming scheme.
      - Using this command will clean them out of a directory.
38. mv: move-It renames if you move it to same dir(used to rename files)
39. du: disk utilisation (du -sh "foldername" - To show the total disk space usage of a specific directory without displaying subdirectory details)
    - -h: human readable form
    - -> To get list of all users and their storage usage: ```du -s | sort -nr```
      - -r: reversed
      - -n: numeric sort
    - Typical Usage: du is commonly used to identify large files or directories that are consuming a significant amount of disk space.
    - ```du -s /usr/share/* | head```
    - show the 10 largest consumers of space
      - ```du -s /usr/share/* | sort -nr | head```
    - sort its results by size using ls:
      - ls -l /usr/bin | sort -nrk 5 | head
40. /proc/cpuinfo (or) lscpu: get no of processors /cores
41. yum -y update: update  
42. kill "PID": kill a process using its pid
43. pkill/killall "pname"- kill using process name
44. Check if a program has used openmp directives
45. history: list of all used commands [History of commands used through the terminal] 
46. chmod 777 file/folder_name: give full permissions to the file for all 3 types of users [admin user and others]
    chmod -R 777 /foldername:  give full access to a folder and all its subfolders.
47. which: Display which executable program will be executed(Executable's Location)
    - useful when more than one version of an executable program installed
    - which python
      - /usr/bin/python3
    -  which ls
      - /usr/bin/ls
48. watch:
49. history -c: clears the history of commands
50. sudo apt-get install "program name"/ sudo apt install "program, name"- install applications
51. sudo remove "programName" - Uninstall a program
52. ```tail -f /var/log/messages (or) sudo fdisk -```: get the list of devices mounted
53. write "username" "pts/ptsno"
    - "Message"	-> send a message to a specific user
    - get pts and ptsno from ```who``` command 
    - Go back to terminal keeping vim in a background: ctrl+z
    - type "fg" to go back to vim
54. nproc - No of CPUs in the System
55. Locate
    - Find Files the Easy Way
    - performs a rapid database search of pathname, and then outputs every name that matches a given substring.
    - find all the programs with names that begin with zip
      - Since we are looking for programs, we can assume that the name of the directory containing the programs would end with bin/.
        - ```locate bin/zip```
        - ```locate zip | grep bin```
      - locate database is created by another program named updatedb
      - it is run periodically as a cron job once a day
      - very recent files do not show up when using locate
56. Find
    - Find Files the Hard Way
    - find program searches a given directory (and its subdirectories) for files based on a variety of attributes.
    - produce a listing of our home directory
      - ```find ~```
    - list of directories from our search(d - search to directories)
      - ```find ~ -type d```
    - search to regular files
      - ```find ~ -type f```
    - search by file size and filename
      - ```find ~ -type f -name "*.JPG" -size +1M```
    - find all files containing "ones" in the name in pwd(.):
      - ```find . -name *ones*```
    - find files with an extension as .cpp:
      - ```find -name "*.cpp"```
    - files with permissions that are not 0600 and the directories with permissions that are not 0700.
      - find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)
    - ```
      File Type Description
      b Block special device file
      c Character special device file
      d Directory
      f Regular file
      l Symbolic link
      
      Character Unit
      b 512-byte blocks. This is the default if no unit is specified.
      c Bytes.
      w 2-byte words.
      k Kilobytes (units of 1024 bytes).
      M Megabytes (units of 1048576 bytes).
      G Gigabytes (units of 1073741824 bytes).
      ```
      - [find_test_descriptions.md](Linux/find_test_descriptions.md)
      - delete files that have the file extension .bak
        - find ~ -type f -name '*.bak' -delete
        - check first
          - find ~ -type f -and -name '*.bak' -and -print
57. diff - Compares the 2 text files and shows the difference between them.
58. curl - is a toll to retrieve information and files from Uniform Resource Locators or internet addresses.
59. chown - allows changing the owner and group owner of a file.
    - e.g. sudo chown tony: ~tony/myfile.txt
60. groups - tells us which group a user is member of.
    Install .deb files
61. You can install it using sudo dpkg -i /path/to/deb/file followed by sudo apt-get install -f.
    OR
62. You can install it using sudo apt install ./name.deb (or sudo apt install /path/to/package/name.deb).
using graphics.h library to run computer graphics programs
63. gcc demo.c -o demo -lgraph
    ./demo
64. SCP- secure copy protocol
65. Copy file from local to Server: scp crc.pdf cse0031@172.27.0.27:~
66. Copy folder from server to local: scp -r user@your.server.example.com:/path/to/foo /home/user/Desktop/
67. go home from anywhere in the terminal
    - cd ~ or simply "cd"
    - Got to home folder of a user: cd ~"user-name"
68. anaconda-navigator: Opens anaconda
69. install .run file: cd /home/user/Downloads
    sudo chmod +x some-app.run
    sudo ./some-app.run
70. xampp - sudo /opt/lampp/lampp start
    - stop
    - restart
71. using dictionary dictd: dict -d wn "dictionary"
72. alias: create an alias to make easier the use of complexes commands.
    - Example 
      - ```alias "name_of_alias":"command"```
      - alias foo='cd /usr; ls; cd -'
    - aliases vanish when our shell session ends.
    - keep in bashrc to make permanent
73. unalias:
    - To remove an alias
    - unalias foo
74. activate virtual environment to use tensorflow: source ./venv/bin/activate
75. Open VS code in current folder: code .
76. uname: know the UNIX machine name
    - uname -a: all info about unix machine
    - o/p: Linux MSI 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
77. create soft link between 2 files (-s => soft link): ln -s "oldfiletobelinkedto" "newlinkfilenametobelinkedfrom"
78. check all soft-links (ll => long list): ll -i
79. Update soft-link: ln -nfs "target" "linkname"
    - e.g. ln -nfs /home/botservice.2.1.0.py Botservice.prod.py
80. ```id```: 
    - gives the user and group names of current user(UID or group id) in the server.
81. file "filename.ext": to know the type of content in a file
    - e.g. file hello.cpp: ASCII text
      - file pic.jpg
        - picture.jpg: JPEG image data, JFIF standard 1.01
82. hostname -i: get ip from host
83. nslookup "ip": get hostname from ip
84. Steps to create a permanent Bash alias:
    a. vi ~/.bash_aliases
    b. append at last: alias new_alias='sudo yum update'
    c. source ~/.bash_aliases
85. How to execute a script in a different directory than the current one?:
    /home/user/scripts/someScript.sh
86. wget "URL": download a file from its URL
87. ```grep "your_pattern" source.txt > destination.txt```
    - search for a pattern in a file and copy output contents to a new file
    - Syntax: ```grep pattern [file...]``` or ```grep [options] regex [file...]```
    - options for grep
      - -i or --ignore-case: ignore case
      - -v or --invert-match: print only those lines that do not match the pattern
      - -n: Display line numbers for matching lines.
      - -c or --count: Count the number of matches instead of displaying the matching lines.
      - -e: Specify multiple patterns to search for.
      - -l or --files-with-matches: name of each file that contains a match instead of the lines themselves.
      - -L or --files-without-match: names of files that do not contain matches.
      - -h or --no-filename: For multi-file searches, suppress the output of filenames.
    - Search for a pattern in multiple files:
      - ```grep "pattern" file1.txt file2.txt file3.txt```
    - Search for a pattern in all text files within a directory recursively:
      - ```grep -r "pattern" /path/to/directory```
    - Using regular expressions:
      - ```grep "^[0-9]" file.txt  # Search for lines starting with a number```
    - grep using pipe 
      - ls | grep hello
    - Anchors in grep
      - caret sign (^): beginning of the line
      - dollar sign ($): end of the line
      - e.g.
        - grep -h '^zip' dirlist*.txt
        - grep -h 'zip$' dirlist*.txt
    - five-letter word whose third letter is ‘j’ and last letter is ‘r’:
      - grep -i '^..j.r$' /usr/share/dict/words
    - find every file in our lists beginning with an uppercase letter:
      - grep -h '^[A-Z]' dirlist*.txt
    - all filenames starting with letters and numbers
      - grep -h '^[A-Za-z0-9]' dirlist*.txt
    - match every filename containing a dash, or an uppercase A or an uppercase Z:
      - grep -h '[-AZ]' dirlist*.txt
    - echo "AAA" | grep -E 'AAA|BBB|CCC'
      - AAA
    - filenames in our lists that start with either bz, gz, or zip
      - grep -Eh '^(bz|gz|zip)' dirlist*.txt
    - filename that begins with bz or contains gz or contains zip:
      - grep -Eh '^bz|gz|zip' dirlist*.txt
    - Quantifiers
      - ? - Match an Element Zero or One Time
      - * - Match an Element Zero or More Times
      - + - Match an Element One or More Times
      - { } - Match an Element a Specific Number of Times
        - {n} Match the preceding element if it occurs exactly n times.
        - {n,m} Match the preceding element if it occurs at least n times but no more than m times.
        - {n,} Match the preceding element if it occurs n or more times.
        - {,m} Match the preceding element if it occurs no more than m times.
88. cat source.txt >> destination.txt: append content of a file into another file linux
89. Using GUI Linux remote access: ssh -X user@ip
90. app commands:
    1. xterm
    2. libreoffice file.odt
    3. evince file.pdf / xdg-open file2open.pdf / gvfs-open file2open.pdf- pdf reader
    4. eog file.png - Image Reader
    5. virtualbox
    6. gedit - text_editor
    7. Firefox
    The way to "double-click" on a file from the command line is xdg-open.
91. For Python 3 
    - create virtual environment
        - mkvirtualenv facecourse-py3 -p python3
        - workon facecourse-py3
92. Copy a whole website: 
    - You may need to mirror the website completely, but be aware that some links may really dead. 
    - You can use HTTrack or wget:
      - wget -r http://winapp.com # or whatever 
      - With HTTrack, first install it:
        - sudo apt-get install httrack 
        - now run it just 1 external link:
          - httrack --ext-depth=1 http://winapp.com
93. Less command:
    - less is a program that lets us view text files. This is very handy since many of the files used to control and configure Linux are human-readable. 
    - e.g. less text_file 
    - Controlling less 
      - Once started, less will display the text file one page at a time. 
      - We can use the Page Up and Page Down keys to move through the text file. 
      - To exit less, we type "q" 
      - Here are some commands that less will accept:
      - Keyboard commands for the less program 
        - Command	Action 
          - Page Up or b	Scroll back one-page 
          - Page Down or space	Scroll forward one page 
          - G	Go to the end of the text file 
          - 1G	Go to the beginning of the text file 
          - /characters	Search forward in the text file for an occurrence of the specified characters 
          - n	Repeat the previous search 
          - h	Display a complete list less commands and options 
          - q	Quit
94. CUDA:
    - module list 
    - which nvcc
    - watch nvidia-smi
    - nvcc "file_name.cu" -o "output_file_name"
95. cat /etc/group: display all the groups associated with the system
96. pstree: display all processes in a tree format
97. ssh-copy-id username@192.168.1.23: Set up passwordless SSH access to a remote host using an available key pair
98. uptime:  facts about the system, 
    - including the length of time the system has been "up" (running) since its last re-boot,
    - the number of users and recent system load. 
    - o/p: 14:38:32 up  1:13,  0 users,  load average: 2.54, 1.12, 0.65
    - o/p format - current_time up time_since_running
99. date: Sat Sep 16 14:37:38 IST 2023
100. time: used to measure the execution time of a command or a shell script
     - It provides information about how long a process takes to run,
     - including the real time, user CPU time, and system CPU time.
     real    0m0.000s
     user    0m0.000s
     sys     0m0.000s
     - e.g. time ls
       - time ./scrip.sh
101. today: Saturday, September 16, 2023
102. sudo du -s /home/* | sort -nr: space each user is using in their home dir
103. cal: open calendar
104. type: Indicates how a command name is interpreted
     - e.g. 
       - type type
         - type is a shell builtin
       - type ls
         - ls is aliased to `ls --color=auto'
       - type pwd
         - pwd is a shell builtin
105. apropos: Display a list of appropriate commands
     - search the list of man pages for possible matches based on a search term.
     -  apropos python  
        >pdb3 (1)             - the Python debugger  
        pdb3.8 (1)           - the Python debugger  
        pip (1)              - A tool for installing and managing Python packages  
        python3.8-config (1) - output build options for python C/C++ extensions or embedding  
        python3 (1)          - an interpreted, interactive, object-oriented programming language  
106. info: Display a command's info entry
     - alternative to man pages for programs, called “info.”
     - e.g. info pwd
107. whatis: Display one-line manual page descriptions
     - whatis pwd
       - pwd (1) - print name of current/working directory
     - whatis python3
       - python3 (1) - an interpreted, interactive, object-oriented programming language
108. sort:
     - put output in sorted order
     - e.g. ls /bin /usr/bin | sort | less
     - can accept multiple files on the command line as arguments, and merge multiple files into a single sorted whole
       - sort file1.txt file2.txt file3.txt > final_sorted_list.txt
       - [sort_options.md](Linux/sort_options.md)
109. uniq: 
     - used in conjunction with sort
     - accepts a sorted list of data from either standard input or a single filename argument 
     - by default, removes any duplicates from the list
     - e.g. ```ls /bin /usr/bin | sort | uniq | less```
     - see the list of duplicates instead
       - add the “-d” option to uniq
       - ```ls /bin /usr/bin | sort | uniq -d | less```
     - report the number of duplicates found in our text file, using the -c option:
       - sort foo.txt | uniq -c
     - [uniq_options.md](Linux/uniq_options.md)
110. tee: Read from standard input and write to standard output and files
     - creates a “tee” fitting on our pipe
     - i.e. reads standard input and copies it to both standard output (allowing the data to continue down the pipeline) and to one or more files.
     - e.g. ls /usr/bin | tee ls.txt | grep zip
111. tail -f file: 
     - view files in real time
     - watching the progress of log files as they are being written
     - This continues until we press Ctrl-c.
112. umask
     - Set Default Permissions= 0002 or 0022 by default
     - The umask value consists of four digits, where each digit represents the permissions to be removed for a specific category of users
     - e.g. umask 0000 - world writable - doesn't remove any permissions,
     - umask 077 - newly created files have permissions 600 (rw-------), and directories have permissions 700 (rwx------).
     - umask 022 - files have permissions 644 (rw-r--r--), and directories have permissions 755 (rwxr-xr-x).
     - Each digit in the umask value corresponds to a set of permissions:
       - 4 corresponds to read permission (r)
       - 2 corresponds to write permission (w)
       - 1 corresponds to execute permission (x)
     - To calculate the effective permissions, you subtract the umask value from the default permissions (usually 666 for files and 777 for directories) to determine the permissions that will be assigned to new files and directories.
113. chgrp
     - Change a file's group ownership
     - chgrp mygroup myfile.txt
114. passwd:
     - Change a user's password
115. exit: 
     - logout and close shell
116. shutdown [options] [time] [message]
     - Commonly used options with the shutdown command include:
       - -r: Reboot the system after shutdown.
       - -h: Halt (power off) the system after shutdown. 
       - -c: Cancel a pending shutdown or restart. 
       - -k: Send a warning message to users without actually shutting down or restarting the system.
    - Immediate Shutdown:
       - shutdown -h now
     - Immediate Reboot:
       - shutdown -r now
     - Scheduled Shutdown in 10 mins:
       - shutdown -h +10
     - Cancel a Pending Shutdown:
       - shutdown -c
     - Shutdown with a Message:
       - shutdown -h now "System will be going down for maintenance in 5 minutes."
117. reboot: restart the computer or system
118. bg: Place a job in the background
119. fg: Place a job in the foreground
120. vmstat:
     - Outputs a snapshot of system resource usage including, memory, swap, and disk I/O. 
     - To see a continuous display, follow the command with a time delay (in seconds) for updates. 
     - example: vmstat 5. Terminate the output with Ctrl-c.
121. xload: A graphical program that draws a graph showing system load over time.
122. tload: Similar to the xload program but draws the graph in the terminal.
123. mount: Mount a file system
     - Entering the command without arguments will display a list of the file systems currently mounted
     - mount -t iso9660 /dev/sdc /mnt/cdrom
124. sudo umount /mnt/"devicename" -> unmount the device
     - umount /dev/sdc
125. fsck: (file system check)
     - Check and repair a file system
     - sudo fsck /dev/sdb1
126. fdisk: Manipulate disk partition table
127. mkfs: (make file system)
     - Create a file system
     - sudo mkfs -t ext4 /dev/sdb1
     - sudo mkfs -t vfat /dev/sdb1
128. dd: (data definition) - could be (destroy disk) if not used properly
     - Convert and copy a file
     - copies blocks of data from one place to another
     - Moving Data Directly to and from Devices
     - dd if=input_file of=output_file [bs=block_size [count=blocks]] 
     - copy the first drive to the second
       - dd if=/dev/sdb of=/dev/sdc
129. genisoimage (mkisofs) – Create an ISO 9660 image file
130. wodim (cdrecord): Write data to optical storage media 
131. md5sum: Calculate an MD5 checksum 
132. ping – Send a special network packet called ICMP ECHO_REQUEST to network hosts
     - Most network devices receiving this packet will reply to it,
     - which allows the network connection to be verified
     - ```ping google.com```
     - ctrl + c prints performance statistics
     - A properly performing network will exhibit 0 percent packet loss.
133. traceroute – Print the route packets trace to a network host
     - i.e. lists all the “hops” network traffic takes to get from the local system to a specified host.
     - ```traceroute google.com```
     - ```sudo traceroute -TI google.com```:  see all network hops without *
     - For routers that do not provide identifying information (because of router configuration, network congestion, firewalls, etc.) 
       - we see asterisks as in the line for hop
134. ip – Show / manipulate routing, devices, policy routing and tunnels
     - ip a
135. netstat – Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
     - e.g. netstat -ie
     - netstat -r
       - -r option will display the kernel’s network routing table
       - This shows how the network is configured to send packets from network to network.
136. ftp – Internet file transfer program(File Transfer Protocol)
     - used to download files over the Internet.
     - FTP (in its original form) is not secure because it sends account names and passwords in cleartext.
     - ```lftp```: better ftp
       - by Alexander Lukyanov
       - features including multiple protocol support (including HTTP), 
         - automatic retry on failed downloads, background processes, tab completion of path names etc.
137. wget – Non-interactive network downloader
     - command-line program for file downloading
     - downloading content from both web and FTP sites.
     - e.g. wget http://linuxcommand.org/index.php
138. rlogin: Unsecure Communication with Remote Hosts
     - log in to remote hosts
     - transmits all their communications (including login names and passwords) in cleartext.
139. telnet: Unsecure Communication with Remote Hosts
     - log in to remote hosts
     - transmits all their communications (including login names and passwords) in cleartext.
     - ```telnet ip port```
     - e.g. telnet 192.168.1.2 22
140. ssh – Secure Communication with Remote Hosts
     - OpenSSH SSH client (remote login program) from the OpenBSD project
     - encrypts all of the communications between the local and remote hosts
     - authenticates that the remote host is who it says it is (thus preventing so-called man-in-the-middle attacks).
     - default port 22
     - e.g. ```ssh username@ip or user@hostname```
     - perform ls on the remote system and redirect the output to a file on local system:
       - ssh remote-sys 'ls *' > dirlist.txt
     - perform ls on the remote system and redirect the output to a file on remote host:
       - ssh remote-sys 'ls * > dirlist.txt'
     - SSH using GUI
       - ssh -X remote-sys or ssh -Y remote-sys
       - xload (to see a GUI)
     - SSH Client for Windows
       - PuTTY by Simon Tatham and team
         - http://www.chiark.greenend.org.uk/~sgtatham/putty/
       - Tectia
141. scp: (secure copy)
     - copy files across the network
     - copy a file named document.txt to local
       - scp username@host:document.txt .
142. sftp: (secure replacement for ftp)
     - uses an SSH encrypted tunnel
     - does not require an FTP server to be running on the remote host
     ``` 
        sftp remote-sys
        sftp> ls
        sftp> lcd Desktop
        sftp> get ubuntu-8.04-desktop-i386.iso
        sftp> bye
     ```
143. xargs – Build and execute command lines from standard input
144. stat – Display file or file system status
     - stat /home/atul
       ```
           File: /home/atul/
           Size: 4096            Blocks: 8          IO Block: 4096   directory
           Device: 820h/2080d      Inode: 670         Links: 38
           Access: (0777/drwxrwxrwx)  Uid: ( 1000/    atul)   Gid: ( 1000/    atul)
           Access: 2023-09-27 19:57:24.807281358 +0530
           Modify: 2023-09-27 10:46:59.523082824 +0530
           Change: 2023-09-27 10:46:59.523082824 +0530
       ```
145. gzip: Compress or expand files
     - compress one or more files
     - replaces the original file with a compressed version of the original.
     - ```gzip foo.txt```
       - o/p: foo.txt.gz
       - [gzip_options.md](Linux/gzip_options.md)
146. gunzip:
     - restore compressed files to their original, uncompressed form
       - ```gunzip foo.txt```
       - or ```gunzip foo.txt.gz```
     - view the contents of a compressed text file, without decompressing
         - ```gunzip -c foo.txt | less```
         - or ```zcat foo.txt.gz | less```
147. bzip2: A block sorting file compressor
     - by Julian Seward
     - similar to gzip but uses a different compression algorithm that achieves higher levels of compression at the cost of compression speed.
     - bzip2 foo.txt
       - o/p: foo.txt.bz2
148. tar: 
     - tool for archiving files
     - syntax: ```tar mode[options] pathname...```
     - ```
       tar Modes
       Mode Description
       c Create an archive from a list of files and/or directories.
       x Extract an archive.
       r Append specified pathnames to the end of an archive.
       t List the contents of an archive.
       ```
     - de-archive tar files:
       - ```tar xf ../playground.tar```
149. zip: Package and compress files
     - both a compression tool and an archiver
     - syntax: ```zip options zipfile file...```
     - e.g. ```zip -r playground.zip playground```
       - -r option for recursion
     - Extracting the contents of a zip file
       - ```unzip ../playground.zip```
150. rsync: Remote file and directory synchronization
     - Synchronizing Files and Directories
       - backup copy of a system involves keeping one or more directories synchronized with another directory (or directories) 
       - located on either on the local system or a remote system.
     - rsync synchronize both local and remote directories by using the rsync remote-update protocol,
       - which allows rsync to quickly detect the differences between two directories and perform
       - the minimum amount of copying required to bring them into sync.
     - syntax: ```rsync options source destination```
     - e.g. ```rsync -av playground foo```
       - -a option (for archiving causes recursion and preservation of file attributes)
       - -v option (verbose output)
151. cut: Remove sections from each line of files
     - extract a section of text from a line and output the extracted section to standard output.
     - cut Selection Options
       - Option Long Option Description
         - -c list --characters=list Extract the portion of the line defined by list. The list may consist of one or more comma-separated numerical ranges.
         - -f list --fields=list Extract one or more fields from the line as defined by list. The list may contain one or more fields or field ranges separated by commas.
         - -d delim --delimeter=delim When -f is specified, use delim as the field delimiting character. By default, fields must be separated by a single tab character.
         - --complement Extract the entire line of text, except for those portions specified by -c and/or -f.
       - e.g. 
         - get 3rd column from a file having tabs delimited columns
           - cut -f 3 distros.txt
         - different field delimiter rather than the tab character(if ':' is delimiter)
           - cut -d ':' -f 1 /etc/passwd | head
152. paste: Merge lines of files
     - adds one or more columns of text to a file
     - read multiple files and combine the fields found in each file into a single stream on standard output
     - e.g. 
       - paste a file containing single column to another with multiple:
         - ```paste distros-dates.txt distros-versions.txt```
153. join: Join lines of two files on a common field
     - joins data from multiple files based on a shared key field.(primary key)
     - ```join distros-key-names.txt distros-key-vernums.txt | head```
154. comm: Compare two sorted files line by line
     - ```comm file1.txt file2.txt```
     - produces three columns of output.
       - first column contains lines unique to the first file argument
       - second column contains the lines unique to the second file argument, 
       - and the third column contains the lines shared by both files.
     - supports options in the form -n, where n is either 1, 2, or 3.
       - to specify which columns to suppress.
         - ```comm -12 file1.txt file2.txt```
155. diff: Compare files line by line
     - more complex tool, supporting many output formats and the ability to process large collections of text files at once
     - ```diff file1.txt file2.txt```
     - diff Change Commands
       - Change Description
       - r1ar2 Append the lines at the position r2 in the second file to the position
       - r1 in the first file.
       - r1cr2 Change (replace) the lines at position r1 with the lines at the position r2 in the second file.
       - r1dr2 Delete the lines in the first file at position r1, which would have appeared at range r2 in the second file
     - context format (the -c option)
       - diff -c file1.txt file2.txt
       - Context Format Change Indicators
         - Indicator Meaning
         - blank: A line shown for context. It does not indicate a difference between the two files.
         - -: A line deleted. This line will appear in the first file but not in the
           second file.
         - +: A line added. This line will appear in the second file but not in the
           first file.
         - !: A line changed. The two versions of the line will be displayed, each
           in its respective section of the change group.
     - unified format(-u option)
       - diff -u file1.txt file2.txt
       - diff Unified Format Change Indicators
       - Character Meaning
         - blank: This line is shared by both files.
         - -: This line was removed from the first file.
         - +: This line was added to the first file.
156. patch: Apply a diff file to an original
     - apply changes to text files
     - accepts output from diff and is generally used to convert older version files into newer versions
     - ```diff -Naur file1.txt file2.txt > patchfile.txt```
     - ```patch < diff_file```
157. tr: Translate or delete characters
     - echo "lowercase letters" | tr a-z A-Z
       - O/P: LOWERCASE LETTERS
     - echo "lowercase letters" | tr [:lower:] A
       - AAAAAAAAA AAAAAAA
     - allows characters to simply be deleted from the input stream.
       - tr -d '\r' < dos_file > unix_file
     - “squeeze” (delete) repeated instances of a character
       - echo "aaabbbccc" | tr -s ab
         - abccc
       - repeating characters must be adjoining. If they are not, the squeezing will have no effect. 
       - echo "abcabcabc" | tr -s ab
         - abcabcabc
158. sed: (Stream editor) for filtering and transforming text
     - echo "front" | sed 's/front/back/'
       - output: “back” 
     - echo "front" | sed 's_front_back_'
       - back
     - echo "front" | sed '1s/front/back/'
       - back
     - echo "aaabbbccc" | sed 's/b/B/'
       - aaaBbbccc
     - echo "aaabbbccc" | sed 's/b/B/g'
       - aaaBBBccc
159. aspell: Interactive spell checker
     - interactive spelling checker
     - successor to an earlier program named ispell
     - ability to intelligently check various types of text files, including HTML documents, C/C++ programs, email messages etc.
     - e.g. ```aspell check textfile```
160. split: split files into pieces
161. csplit: split files into pieces based on context 
162. sdiff (side-by-side merge of file differences).
163. nl – Number lines
     - ```nl distros.txt | head```
164. fold – Wrap each line to a specified length
     - ```echo "The quick brown fox jumped over the lazy dog." | fold -w 12```
     - ```echo "The quick brown fox jumped over the lazy dog." | fold -w 12 -s```
165. fmt – A simple text formatter
     - fills and joins lines in text while preserving blank lines and indentation.
     - ```fmt -w 50 fmt-info.txt | head```
     - ```fmt -cw 50 fmt-info.txt | head```
     - ```fmt -w 50 -p '# ' fmt-code.txt```
166. pr – Prepare text for printing
     - ```pr -l 15 -w 65 distros.txt```
167. printf – Format and print data
     - ```printf "I formatted the string: %s\n" foo```
     - ```printf "I formatted '%s' as a string.\n" foo```
     - ```printf "%d, %f, %o, %s, %x, %X\n" 380 380 380 380 380 380```
       - 380, 380.000000, 574, 380, 17c, 17C
     - ```printf "%s\t%s\t%s\n" str1 str2 str3```
     - ```printf "Line: %05d %15.3f Result: %+15d\n" 1071 3.14156295 32589```
168. groff – A document-formatting system
     - zcat /usr/share/man/man1/ls.1.gz | groff -mandoc -T ascii | head
169. ps2pdf:
     - convert the Post-Script file into a Portal Document Format (PDF)
     - ```ps2pdf ~/Desktop/foo/ps ~Desktop/ls.pdf```
170. pr – Convert text files for printing
     - e.g. ```ls /usr/bin | pr -3 -w 65 | head```
171. lpr/lp: Print files
     - ```ls /usr/bin | pr -3 | lpr```
     - report would be sent to the system’s default printer
     - To send the file to a different printer:
       - ```lpr -P printer_name```
     - printing 12 CPI and 8 LPI with a left margin of one half inch.
       - ls /usr/bin | pr -4 -w 90 -l 88 | lp -o page-left=36 -o cpi=12 -o lpi=8
172. a2ps – Format files for printing on a PostScript printer
     - ASCII to PostScript(now, Anything to PostScript)
     - prepare text files for printing on PostScript printers.
     - ls /usr/bin | pr -3 -t | a2ps -o ~/Desktop/ls.ps -L 66
173. lpstat -a: Show printer status information
     - see a list of printers known to the system
     - lpstat -s
       - detailed description of the print system configuration
174. ```lpq``` – Show printer queue status
     - see the status of a printer queue
     - view the status of the queue and the print jobs it contains
175. lprm – Cancel print jobs
     - ```cancel 603```
176. display ***hardware device profile*** on your Linux system:
     - lscpu
       - information about the CPU (Central Processing Unit) and its characteristics.
     - lsusb
       - lists USB devices connected to the system.
     - lspci
       - lists PCI devices, including graphics cards, network adapters, etc.
     - lsblk
       - information about block devices such as hard drives and partitions.
     - free -h
       - Displays memory (RAM) usage and availability.
     - df -h
       - Shows disk space usage and availability.
     - inxi -Fxz
       - comprehensive system information.
     - hwinfo
       - comprehensive hardware information
     - sudo dmidecode
       - detailed information about the system's hardware components from the DMI (Desktop Management Interface) tables.
