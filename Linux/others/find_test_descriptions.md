- Test Description
  - -cmin n Match files or directories whose content or attributes were
  last modified exactly n minutes ago. To specify less than n
  minutes ago, use -n, and to specify more than n minutes
  ago, use +n.
  - -cnewer file Match files or directories whose contents or attributes were
  last modified more recently than those of file.
  - -ctime n Match files or directories whose contents or attributes were
  last modified n*24 hours ago.
  - -empty Match empty files and directories.
  - -group name Match file or directories belonging to group. group may
  be expressed either as a group name or as a numeric group
  ID.
  - -iname pattern Like the -name test but case-insensitive.
  - -inum n Match files with inode number n. This is helpful for finding
  all the hard links to a particular inode.
  - -mmin n Match files or directories whose contents were last
  modified n minutes ago.
  - -mtime n Match files or directories whose contents were last
  modified n*24 hours ago.
  - -name pattern Match files and directories with the specified wildcard
  pattern.
  - -newer file Match files and directories whose contents were modified
  more recently than the specified file. This is useful when
  writing shell scripts that perform file backups. Each time
  you make a backup, update a file (such as a log) and then
  use find to determine which files have changed since the
  last update.
  - -nouser Match file and directories that do not belong to a valid user.
  This can be used to find files belonging to deleted accounts
  or to detect activity by attackers.
  - -nogroup Match files and directories that do not belong to a valid
  group.
  - -perm mode Match files or directories that have permissions set to the
  specified mode. mode can be expressed by either octal or
  symbolic notation.
  - -samefile name Similar to the -inum test. Match files that share the same
  inode number as file name.
  - -size n Match files of size n.
  - -type c Match files of type c.
  - -user name Match files or directories belonging to user name. The user
  may be expressed by a username or by a numeric user ID.
  This is not a complete list. The find man page has all the details.
- FIND LOGICAL OPERATORS:
  - Operator Description
    - -and Match if the tests on both sides of the operator are true.
    This can be shortened to -a. Note that when no operator is
    present, -and is implied by default.
    - -or Match if a test on either side of the operator is true. This
    can be shortened to -o.
    - -not Match if the test following the operator is false. This can be
    abbreviated with an exclamation point (!).
    - ( ) Groups tests and operators together to form larger
    expressions. This is used to control the precedence of the
    logical evaluations. By default, find evaluates from left to
    right. It is often necessary to override the default evaluation
    order to obtain the desired result. Even if not needed, it is
    helpful sometimes to include the grouping characters to
    improve the readability of the command. Note that since
    the parentheses have special meaning to the shell, they
    must be quoted when using them on the command line to
    allow them to be passed as arguments to find. Usually the
    backslash character is used to escape them.
- expr1 -operator expr2 
  - In all cases, expr1 will always be performed; however, the operator will determine whether expr2 is performed. Table 17-5 outlines how it works.
    - Table 17-5: find AND/OR Logic
    - Results of expr1 Operator expr2 is...
      - True -and Always performed
      - False -and Never performed
      - True -or Never performed
      - False -or Always performed
- Predefined find Actions
  - Action Description
    - -delete Delete the currently matching file.
    - -ls Perform the equivalent of ls -dils on the matching file.
      Output is sent to standard output.
    - -print Output the full pathname of the matching file to standard
      output. This is the default action if no other action is
      specified.
    - -quit Quit once a match has been made.
