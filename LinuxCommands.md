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
7. cat: read a file
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
20. ps: get my processes/machine number... 
    - ps -aux
21. ifup ens33 and ifdown ens33: to connect/disconnect system to network
22. wc: word count
    - wc file.txt
      - output: 10  50 300 file.txt
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
26. top: view your system’s resource usage and see the processes that are taking up the most system resources. It displays a list of processes, with the ones using the most CPU .
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
31. head -n 50 | tail -n 15: display line 35 to 50  (1st find first 50 lines and then show last 15 lines of that first 50 line)
32. tar -zxvf "filename" - extract archive files (zxvf-> z:gzip,x:extract,v:verbose,f:bzip2)
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
47. which:
48. watch:
49. history -c: clears the history of commands
50. sudo apt-get install "program name"/ sudo apt install "program, name"- install applications
51. sudo remove "programName" - Uninstall a program
52. tail -f /var/log/messages (or) sudo fdisk -l->get the list of devices mounted
53. sudo umount /mnt/"devicename" ->unmount the device
54. write "username" "pts/ptsno"
    - "Message"	-> send message to a specific user
    - get pts and ptsno from who command 
    - Go back to terminal keeping vim in background: ctrl+z
    - type "fg" to go back to vim 
55. nproc - No of CPUs in the System
56. a. find/ locate . -name *ones* - find all files containing "ones" in the name in pwd(.). 
    b. find -name "*.cpp": find files with an extension as .cpp.
57. diff - Compares the 2 text files and shows the difference between them.
58. curl - is a toll to retrieve information and files from Uniform Resource Locators or internet addresses.
59. chown - allows changing the owner and group owner of a file.
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
72. alias: create an alias to make easier the use of complexes commands. Example of use: alias "name_of_alias":"command"
73. activate virtual environment to use tensorflow: source ./venv/bin/activate
74. Open VS code in current folder: code .
75. uname: know the UNIX machine name
    - uname -a: all info about unix machine
    - o/p: Linux MSI 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
76. create soft link between 2 files (-s => soft link): ln -s "oldfiletobelinkedto" "newlinkfilenametobelinkedfrom"
77. check all soft-links (ll => long list): ll -i
78. Update soft-link: ln -nfs "oldfiletobelinkedto" "newlinkfilenametobelinkedfrom"
    - eg. ln -nfs /home/botservice.2.1.0.py Botservice.prod.py
79. id: gives the user and group names of current user(UID or group id) in the server.
80. file "filename.ext": to know the type of content in a file 
    - e.g. file hello.cpp: ASCII text
      - file pic.jpg
        - picture.jpg: JPEG image data, JFIF standard 1.01
81. get ip from host: hostname -i
82. get hostname from ip: nslookup "ip"
83. Steps to create a permanent Bash alias:
    a. vi ~/.bash_aliases
    b. append at last: alias new_alias='sudo yum update'
    c. source ~/.bash_aliases
84. How to execute a script in a different directory than the current one?:
    /home/user/scripts/someScript.sh
85. download a file from its URL: wget "URL"
86. search for a pattern in a file and copy output contents to a new file: grep "your_pattern" source.txt > destination.txt
87. append content of a file into another file linux: cat source.txt >> destination.txt
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
103. 