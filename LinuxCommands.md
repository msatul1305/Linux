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
    - -> To get list of all users and their storage usage: du -s | sort -nr
      - -r: reversed
      - -n: numeric sort
    - Typical Usage: du is commonly used to identify large files or directories that are consuming a significant amount of disk space.
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
55. a. find/ locate . -name *ones* - find all files containing "ones" in the name in pwd(.). 
    b. find -name "*.cpp": find files with an extension as .cpp.
56. diff - Compares the 2 text files and shows the difference between them.
57. curl - is a toll to retrieve information and files from Uniform Resource Locators or internet addresses.
58. chown - allows changing the owner and group owner of a file.
    - e.g. sudo chown tony: ~tony/myfile.txt
59. groups - tells us which group a user is member of.
    Install .deb files
60. You can install it using sudo dpkg -i /path/to/deb/file followed by sudo apt-get install -f.
    OR
61. You can install it using sudo apt install ./name.deb (or sudo apt install /path/to/package/name.deb).
using graphics.h library to run computer graphics programs
62. gcc demo.c -o demo -lgraph
    ./demo
63. SCP- secure copy protocol
64. Copy file from local to Server: scp crc.pdf cse0031@172.27.0.27:~
65. Copy folder from server to local: scp -r user@your.server.example.com:/path/to/foo /home/user/Desktop/
66. go home from anywhere in the terminal
    - cd ~ or simply "cd"
    - Got to home folder of a user: cd ~"user-name"
67. anaconda-navigator: Opens anaconda
68. install .run file: cd /home/user/Downloads
    sudo chmod +x some-app.run
    sudo ./some-app.run
69. xampp - sudo /opt/lampp/lampp start
    - stop
    - restart
70. using dictionary dictd: dict -d wn "dictionary"
71. alias: create an alias to make easier the use of complexes commands.
    - Example 
      - ```alias "name_of_alias":"command"```
      - alias foo='cd /usr; ls; cd -'
    - aliases vanish when our shell session ends.
    - keep in bashrc to make permanent
72. unalias:
    - To remove an alias
    - unalias foo
73. activate virtual environment to use tensorflow: source ./venv/bin/activate
74. Open VS code in current folder: code .
75. uname: know the UNIX machine name
    - uname -a: all info about unix machine
    - o/p: Linux MSI 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
76. create soft link between 2 files (-s => soft link): ln -s "oldfiletobelinkedto" "newlinkfilenametobelinkedfrom"
77. check all soft-links (ll => long list): ll -i
78. Update soft-link: ln -nfs "target" "linkname"
    - e.g. ln -nfs /home/botservice.2.1.0.py Botservice.prod.py
79. ```id```: 
    - gives the user and group names of current user(UID or group id) in the server.
80. file "filename.ext": to know the type of content in a file
    - e.g. file hello.cpp: ASCII text
      - file pic.jpg
        - picture.jpg: JPEG image data, JFIF standard 1.01
81. hostname -i: get ip from host
82. nslookup "ip": get hostname from ip
83. Steps to create a permanent Bash alias:
    a. vi ~/.bash_aliases
    b. append at last: alias new_alias='sudo yum update'
    c. source ~/.bash_aliases
84. How to execute a script in a different directory than the current one?:
    /home/user/scripts/someScript.sh
85. wget "URL": download a file from its URL
86. ```grep "your_pattern" source.txt > destination.txt```
    - search for a pattern in a file and copy output contents to a new file
    - Syntax: ```grep pattern [file...]```
    - options for grep
      - -i: ignore case
      - -v: print only those lines that do not match the pattern
      - -n: Display line numbers for matching lines.
      - -c: Count the number of matches instead of displaying the matching lines.
      - -e: Specify multiple patterns to search for.
    - Search for a pattern in multiple files:
      - ```grep "pattern" file1.txt file2.txt file3.txt```
    - Search for a pattern in all text files within a directory recursively:
      - ```grep -r "pattern" /path/to/directory```
    - Using regular expressions:
      - ```grep "^[0-9]" file.txt  # Search for lines starting with a number```
    - grep using pipe 
      - ls | grep hello
87. cat source.txt >> destination.txt: append content of a file into another file linux
88. Using GUI Linux remote access: ssh -X user@ip
89. app commands:
    1. xterm
    2. libreoffice file.odt
    3. evince file.pdf / xdg-open file2open.pdf / gvfs-open file2open.pdf- pdf reader
    4. eog file.png - Image Reader
    5. virtualbox
    6. gedit - text_editor
    7. Firefox
    The way to "double-click" on a file from the command line is xdg-open.
90. For Python 3 
    - create virtual environment
        - mkvirtualenv facecourse-py3 -p python3
        - workon facecourse-py3
91. Copy a whole website: 
    - You may need to mirror the website completely, but be aware that some links may really dead. 
    - You can use HTTrack or wget:
      - wget -r http://winapp.com # or whatever 
      - With HTTrack, first install it:
        - sudo apt-get install httrack 
        - now run it just 1 external link:
          - httrack --ext-depth=1 http://winapp.com
92. Less command:
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
93. CUDA:
    - module list 
    - which nvcc
    - watch nvidia-smi
    - nvcc "file_name.cu" -o "output_file_name"
94. cat /etc/group: display all the groups associated with the system
95. pstree: display all processes in a tree format
96. ssh-copy-id username@192.168.1.23: Set up passwordless SSH access to a remote host using an available key pair
97. uptime:  facts about the system, 
    - including the length of time the system has been "up" (running) since its last re-boot,
    - the number of users and recent system load. 
    - o/p: 14:38:32 up  1:13,  0 users,  load average: 2.54, 1.12, 0.65
98. date: Sat Sep 16 14:37:38 IST 2023
99. time: used to measure the execution time of a command or a shell script
    - It provides information about how long a process takes to run,
    - including the real time, user CPU time, and system CPU time.
    real    0m0.000s
    user    0m0.000s
    sys     0m0.000s
    - e.g. time ls
      - time ./scrip.sh
100. today: Saturday, September 16, 2023
101. sudo du -s /home/* | sort -nr: space each user is using in their home dir
102. cal: open calendar
103. type: Indicates how a command name is interpreted
     - e.g. 
       - type type
         - type is a shell builtin
       - type ls
         - ls is aliased to `ls --color=auto'
       - type pwd
         - pwd is a shell builtin
104. apropos: Display a list of appropriate commands
     - search the list of man pages for possible matches based on a search term.
     -  apropos python  
        >pdb3 (1)             - the Python debugger  
        pdb3.8 (1)           - the Python debugger  
        pip (1)              - A tool for installing and managing Python packages  
        python3.8-config (1) - output build options for python C/C++ extensions or embedding  
        python3 (1)          - an interpreted, interactive, object-oriented programming language  
105. info: Display a command's info entry
     - alternative to man pages for programs, called “info.”
     - e.g. info pwd
106. whatis: Display one-line manual page descriptions
     - whatis pwd
       - pwd (1) - print name of current/working directory
     - whatis python3
       - python3 (1) - an interpreted, interactive, object-oriented programming language
107. sort:
     - put output in sorted order
     - e.g. ls /bin /usr/bin | sort | less
108. uniq: 
     - used in conjunction with sort
     - accepts a sorted list of data from either standard input or a single filename argument 
     - by default, removes any duplicates from the list
     - e.g. ls /bin /usr/bin | sort | uniq | less
     - see the list of duplicates instead
       - add the “-d” option to uniq
       - ls /bin /usr/bin | sort | uniq -d | less
109. tee: Read from standard input and write to standard output and files
     - creates a “tee” fitting on our pipe
     - i.e. reads standard input and copies it to both standard output (allowing the data to continue down the pipeline) and to one or more files.
     - e.g. ls /usr/bin | tee ls.txt | grep zip
110. tail -f file: 
     - view files in real time
     - watching the progress of log files as they are being written
     - This continues until we press Ctrl-c.
111. umask
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
112. chgrp
     - Change a file's group ownership
     - chgrp mygroup myfile.txt
113. passwd:
     - Change a user's password
114. exit: 
     - logout and close shell
115. shutdown [options] [time] [message]
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
116. reboot: restart the computer or system
117. bg: Place a job in the background
118. fg: Place a job in the foreground
119. vmstat:
     - Outputs a snapshot of system resource usage including, memory, swap, and disk I/O. 
     - To see a continuous display, follow the command with a time delay (in seconds) for updates. 
     - example: vmstat 5. Terminate the output with Ctrl-c.
120. xload: A graphical program that draws a graph showing system load over time.
121. tload: Similar to the xload program but draws the graph in the terminal.
122. mount: Mount a file system
     - Entering the command without arguments will display a list of the file systems currently mounted
     - mount -t iso9660 /dev/sdc /mnt/cdrom
123. sudo umount /mnt/"devicename" -> unmount the device
     - umount /dev/sdc
124. fsck: (file system check)
     - Check and repair a file system
     - sudo fsck /dev/sdb1
125. fdisk: Manipulate disk partition table
126. mkfs: (make file system)
     - Create a file system
     - sudo mkfs -t ext4 /dev/sdb1
     - sudo mkfs -t vfat /dev/sdb1
127. dd: (data definition) - could be (destroy disk) if not used properly
     - Convert and copy a file
     - copies blocks of data from one place to another
     - Moving Data Directly to and from Devices
     - dd if=input_file of=output_file [bs=block_size [count=blocks]] 
     - copy the first drive to the second
       - dd if=/dev/sdb of=/dev/sdc
128. genisoimage (mkisofs) – Create an ISO 9660 image file
129. wodim (cdrecord): Write data to optical storage media 
130. md5sum: Calculate an MD5 checksum 
131. ping – Send an ICMP ECHO_REQUEST to network hosts
     - allows the network connection to be verified
     - ```ping google.com```
132. traceroute – Print the route packets trace to a network host
     - i.e. lists all the “hops” network traffic takes to get from the local system to a specified host.
     - ```traceroute google.com```
     - ```sudo traceroute -TI google.com```:  see all network hops without *
133. ip – Show / manipulate routing, devices, policy routing and tunnels
134. netstat – Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
135. ftp – Internet file transfer program
136. wget – Non-interactive network downloader
137. ssh – OpenSSH SSH client (remote login program)
138. xargs – Build and execute command lines from standard input
139. stat – Display file or file system status
140. gzip: Compress or expand files
141. bzip2: A block sorting file compressor
142. zip: Package and compress files
143. rsync: Remote file and directory synchronization
144. cut: Remove sections from each line of files
145. paste: Merge lines of files
146. join: Join lines of two files on a common field
147. comm: Compare two sorted files line by line
148. diff: Compare files line by line
149. patch: Apply a diff file to an original
150. tr: Translate or delete characters
151. sed: Stream editor for filtering and transforming text
152. aspell: Interactive spell checker
153. nl – Number lines
154. fold – Wrap each line to a specified length
155. fmt – A simple text formatter
156. pr – Prepare text for printing
157. printf – Format and print data
158. groff – A document formatting system
159. pr – Convert text files for printing 
160. lpr – Print files 
161. a2ps – Format files for printing on a PostScript printer
162. lpstat – Show printer status information
163. lpq – Show printer queue status
164. lprm – Cancel print jobs
165. 