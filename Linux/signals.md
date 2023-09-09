| Signal Name | Signal Number | Usage                                                |
|-------------|---------------|------------------------------------------------------|
| SIGHUP      | 1             | Configuration reload or restart request             |
| SIGINT      | 2             | Terminate gracefully (Ctrl+C in terminal)           |
| SIGQUIT     | 3             | Terminate with core dump for debugging              |
| SIGILL      | 4             | Illegal instruction                                 |
| SIGTRAP     | 5             | Trace/breakpoint trap (debugging)                   |
| SIGABRT     | 6             | Abort (internal error)                              |
| SIGBUS      | 7             | Bus error (invalid memory access)                   |
| SIGFPE      | 8             | Floating-point exception                            |
| SIGKILL     | 9             | Forced termination (uninterruptible)                |
| SIGUSR1     | 10            | User-defined signal 1                               |
| SIGSEGV     | 11            | Segmentation fault (invalid memory access)          |
| SIGUSR2     | 12            | User-defined signal 2                               |
| SIGPIPE     | 13            | Broken pipe (write to pipe with no reader)          |
| SIGALRM     | 14            | Alarm clock (timer expiration)                      |
| SIGTERM     | 15            | Terminate gracefully                                 |
| SIGCHLD     | 17            | Child process status change (child exited)          |
| SIGCONT     | 18            | Continue (resume paused process)                    |
| SIGSTOP     | 19            | Stop (pause process, can be resumed)                |
| SIGTSTP     | 20            | Terminal stop (suspend process, Ctrl+Z)             |
| SIGTTIN     | 21            | Background read from control terminal               |
| SIGTTOU     | 22            | Background write to control terminal                |
| SIGURG      | 23            | Urgent condition on socket                          |
| SIGXCPU     | 24            | CPU time limit exceeded                             |
| SIGXFSZ     | 25            | File size limit exceeded                            |
| SIGVTALRM   | 26            | Virtual timer expiration                            |
| SIGPROF     | 27            | Profiling timer expiration                          |
| SIGWINCH    | 28            | Window size change (terminal resized)              |
| SIGIO       | 29            | I/O is possible on a descriptor (socket, file, etc) |
| SIGPWR      | 30            | Power failure or restart                           |
| SIGSYS      | 31            | Bad system call                                     |
