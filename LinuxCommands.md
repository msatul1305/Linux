On most Linux systems a program called bash (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, sh, written by Steve Bourne) acts as the shell program. Besides bash, there are other shell programs available for Linux systems. These include: ksh, tcsh and zsh.

What's a "Terminal?"
This is a program that opens a window and lets you interact with the shell. Some Linux distributions install several. These might include gnome-terminal, konsole, xterm, rxvt, kvt, nxterm, and eterm.

If the last character of your shell prompt is # rather than $, you are operating as the superuser. 

Format of any linux command: 
	command -options arguments 
	eg. ls -l /etc
	
File Permissions
A representation of the file's access permissions. 
- rw- --- --- = (1,3,3,3) = (type, file's_owner, file's_group, everybody_else)
The first character is the type of file. 
	"-" indicates a regular (ordinary) file. 
	"d" indicates a directory.
The second set of three characters represent the read, write, and execution rights of the file's owner. 
The next three represent the rights of the file's group, and the 
final three represent the rights granted to everybody else.
e.g. drwxr-xr-x  6 me me 1024 Oct 9 2019 web_page

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
    

ASCII text. ASCII (pronounced "As-Key") is short for American Standard Code for Information Interchange. This is a simple encoding scheme that was first used on Teletype machines to map keyboard characters to numbers.
Text is a simple one-to-one mapping of characters to numbers. It is very compact. Fifty characters of text translates to fifty bytes of data.
i.e. 1 character = 1 byte data = 8 bits data. that's why ASCII = 8 bits(0 to 2^7 or 127)
1. df -Th : No of Partitions/My Computer of Linux
2. cd - change directory, md - make directory
3. ls- list (ls -a: all files(show hidden files))
4. pwd- present working directory
5. man -manual
6. clear / ctrl+l: clear terminal
7. cat: read a file
8. mkdir: make directory
9. su -i :   change to root user
10. su - "username" : change current user
11. useradd 
12. ctrl+ d/logout/exit: logout
13. DON'T USE: rm -rvf /
14. touch : create a new file if the file is non-existing or update the timestamp if the file already exists
15. vi/vim for redhat and nano for debian: edit files
16. systemctl status/stop/start "sshd"- check status/start/stop of sshd service
17. wall - broadcast message to all logged-in users
18. In WWindows to Restart wireless network :ncpa.ctl
19. w: list of all logged-in users
20. ps: get my processes/machine number...
ps -aux
21. ifup ens33 and ifdown ens33 : to connect/disconnect system to network
22. wc: word count
23. free /free -h: get ram status
24. ssh vssut@10.208.34.9
25. command |ps wc -l : count no of things in a list	
26. top : view your system’s resource usage and see the processes that are taking up the most system resources. It displays a list of processes, with the ones using the most CPU .
27. VIM COMMANDS
     get out of vi : esc-> :q or :q!(forcefully quit)
     insert in vim : press i
      w: write 
      wq: save and exit
    :set nu : show line numbers (lines nos will be displayed)
    ?"text" : search a particular text in the file
    :%s/"oldtext"/"newtext" : search and replace all
28. head -n "10" "filename": display first 10 lines 
29. tail -n "10" "filename" : display last 10 lines
30. more/less "filename": read a file
31. head -n 50| tail -n 15 : display line 35 to 50  (1st find first 50 lines and then show last 15 lines of that first 50 line)
32. tar -zxvf "filename" - extract archive files (zxvf-> z:gzip,x:extract,v:verbose,f:bzip2)
unzip file.zip - extract the files from zip
33. cp "vss.txt" "/home/msatul1305/Desktop" -v : copy from current directory to new directory -v=>verbose(show copied acknowledgement)
34. "." : current directory
35. ".." : parent directory
36. cp -r : copy a folder (recursive)
37. rm : remove/delete file
38. mv : move-It renames if you move it to same dir(used to rename files)
39. du : disk utilisation (du -sh "foldername")
    -h: human readable form
    -> To get list of all users and their storage usage: du -s | sort -nr
40. /proc/cpuinfo (or) lscpu : get no of processors /cores
41. yum -y update: update  
42. kill "PID" :kill a process using its pid
43. pkill/killall "pname"- kill using process name
44. : Check if a program has used openmp directives
45. history : list of all used commands [History of commands used through the terminal] 
46. chmod 777 file/folder_name : give full permissions to the file for all 3 types of users [admin user and others]
    chmod -R 777 /foldername :  give full access to a folder and all its subfolders.
47. which :
48. watch :
49. history -c : clears the history of commands
50. sudo apt-get install "program name"/ sudo apt install "program, name"- install applications
51. sudo remove "programName" - Uninstall a program
52. tail -f /var/log/messages (or) sudo fdisk -l->get the list of devices mounted
53. sudo umount /mnt/"devicename"  ->unmount the device
54. write "username" "pts/ptsno" 
"Message"	-> send message to a specific user
get pts and ptsno from who command
Go back to terminal keeping vim in background: ctrl+z
type "fg" to go back to vim 
55. nproc - No of CPUs in the System
56. a. find/ locate . -name *ones* - find all files containing "ones" in the name in pwd(.). 
    b. find -name "*.cpp": find files with extension as .cpp.
57. diff - Compares the 2 text files and shows the difference between them.
58. curl - is a toll to retrieve information and files from Uniform Resource Locators or internet addresses.
59. chown - allows to change the owner and group owner of a file.
60. groups - tells us which group a user is member of.
    Install .deb files
61. You can install it using sudo dpkg -i /path/to/deb/file followed by sudo apt-get install -f.
    OR
62. You can install it using sudo apt install ./name.deb (or sudo apt install /path/to/package/name.deb).
using graphics.h library to run computer graphics programs
63. gcc demo.c -o demo -lgraph
    ./demo
SCP- secure copy protocol
64. Copy file from local to Server: scp crc.pdf cse0031@172.27.0.27:~
65. Copy folder from server to local : scp -r user@your.server.example.com:/path/to/foo /home/user/Desktop/

66. go home from anywhere in the terminal
    cd ~ or simply "cd"
    Got to home folder of a user: cd ~"user-name"
67. anaconda-navigator : Opens anaconda
68. install .run file: cd /home/user/Downloads
    sudo chmod +x some-app.run
    sudo ./some-app.run
69. xampp - sudo /opt/lampp/lampp start
    stop
    restart
70. using dictionary dictd :  dict -d wn "dictionary"
71. alias : create an alias to make easier the use of complexes commands. Example of use: alias "name_of_alias":"command"
72. activate virtual environment to use tensorflow : source ./venv/bin/activate
73. Open VS code in current folder : code .
74. uname : know the UNIX machine name
    uname -a: all info about unix machine
75. create soft link between 2 files (-s => soft link): ln -s "oldfiletobelinkedto" "newlinkfilenametobelinkedfrom"
76. check all soft-links (ll => long list): ll -i
77. Update soft-link: ln -nfs "oldfiletobelinkedto" "newlinkfilenametobelinkedfrom"
    eg. ln -nfs /home/botservice.2.1.0.py Botservice.prod.py
78. id: gives the user and group names of current user(UID or group id) in the server.
79. file "filename.ext": to know the type of content in a file e.g. hello.cpp: ASCII text
80. get ip from host: hostname -i
81. get hostname from ip: nslookup "ip"
82. Steps to create a permanent Bash alias:
    a. vi ~/.bash_aliases
    b. append at last: alias new_alias='sudo yum update'
    c. source ~/.bash_aliases
83. How to execute a script in a different directory than the current one?:
    /home/user/scripts/someScript.sh
84. download a file from its URL: wget "URL"
85. search for a pattern in a file and copy output contents to a new file: grep "your_pattern" source.txt > destination.txt
86. append content of a file into another file linux: cat source.txt >> destination.txt

Using GUI Linux remote access: ssh -X user@ip

app commands:
1. xterm
2. libreoffice file.odt
3. evince file.pdf / xdg-open file2open.pdf / gvfs-open file2open.pdf- pdf reader
4. eog file.png - Image Reader
5. virtualbox
6. gedit - text_editor
7. Firefox
The way to "double-click" on a file from the command line is xdg-open. 

############ For Python 3 ############
# create virtual environment
mkvirtualenv facecourse-py3 -p python3
workon facecourse-py3


Copy a whole website : You may need to mirror the website completely, but be aware that some links may really dead. You can use HTTrack or wget:

wget -r http://winapp.com # or whatever
With HTTrack, first install it:

sudo apt-get install httrack
now run it just 1 external link:

httrack --ext-depth=1 http://winapp.com


Less command:
less is a program that lets us view text files. This is very handy since many of the files used to control and configure Linux are human-readable.
e.g. less text_file
Controlling less
Once started, less will display the text file one page at a time. We can use the Page Up and Page Down keys to move through the text file. To exit less, we type "q". Here are some commands that less will accept:

Keyboard commands for the less program
Command	Action
Page Up or b	Scroll back one-page
Page Down or space	Scroll forward one page
G	Go to the end of the text file
1G	Go to the beginning of the text file
/characters	Search forward in the text file for an occurrence of the specified characters
n	Repeat the previous search
h	Display a complete list less commands and options
q	Quit


CUDA:
module list
which nvcc
watch nvidia-smi
nvcc "file_name.cu" -o "output_file_name"