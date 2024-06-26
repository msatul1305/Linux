- Escape Codes Used in Shell Prompts
  - \a ASCII bell. This makes the computer beep when it is encountered.
  - \d Current date in day, month, date format. For example, “Mon May
    26.”
  - \h Hostname of the local machine minus the trailing domain name.
  - \H Full hostname.
  - \j Number of jobs running in the current shell session.
  - \l Name of the current terminal device.
  - \n A newline character.
  - \r A carriage return.
  - \s Name of the shell program.
  - \t Current time in 24-hour hours:minutes:seconds format.
  - \T Current time in 12-hour format.
  - \@ Current time in 12-hour AM/PM format.
  - \A Current time in 24-hour hours:minutes format.
  - \u Username of the current user.
  - \v Version number of the shell.
  - \V Version and release numbers of the shell.
  - \w Name of the current working directory.
  - \W Last part of the current working directory name.
  - \! History number of the current command.
  - \# Number of commands entered during this shell session.
  - \$ This displays a “$” character unless we have superuser privileges. 
    - In that case, it displays a “#” instead.
  - \[ Signals the start of a series of one or more non-printing characters. 
    - This is used to embed non-printing control characters that manipulate the terminal emulator in some way, such as moving the 
      - cursor or changing text colors.
  - \] Signals the end of a non-printing character sequence.


- Anatomy of a Prompt
  - [me@linuxbox ~]$ echo $PS1
    - [\u@\h \W]\$
  - PS1="\[\033[s\033[0;0H\033[0;41m\033[K\033[1;33m\t\033[0m\033[u\]
  - <\u@\h \W>\$ "
  - export PS1
