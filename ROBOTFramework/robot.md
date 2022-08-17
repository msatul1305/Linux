***Robot Framework***
- Generic open source automation framework for:
1. Acceptance Testing - To test the capability of a system.
2. ATTD - Acceptance Test driven development - Development methodology based on communication between business, customers, developers and testers - creating of acceptance tests before development of actual functionality
3. RPA - Robotic Process Automation -> Reducing human efforts for machines that uses ML and AI. Handles high level repeatable tasks.

-> Uses Keyword driven testing approach.


***Architecture***
When Robot Framework is started, it processes the data, executes the test cases and generates logs and reports.

***Standard Libraries***
1. Builtin libraries: eg.Should be equal, should contain, convert to integer, Logs, run, leap keyword, set variable.
2. Collections: eg. pen to list, get from dictionary, list should be equal, dictionary should be contained value.
3. DateTime: eg. get current date, convert time, subtract time from date, add time from time
4. Dialogs: used for Pausing the test execution and getting input from users
5. OperatingSystem: run, create and remove directories, files should exist, directory should be empty, set environment variable. 
6. Process: popen class, run processes in a system, wait for process completion, start process, wait for process, terminate process, terminate all processes.
7. Remote: 
8. Screenshot: take ss
9. String: replace string using regX, split 2 lines, should be string
10. telnet: telnet connections
11. XML framework

***Built-in Tools***
1. Testdoc
2. Tidy
3. Rebot
4. Libdoc

***Test Cases***
1. Data Driven tests
2. Work flow tests
3. High level tests


Test case tables:
1st column: test names
2nd column: Keyword names/ setting variables from keyword return values
***Setting names: square brackets around them - to distinguish them from keywords***
***There should be nothing between table headers and 1st test***
Test cases can also have their own settings


Some available settings:
[documentation] - specifying test case documentation
[tags] - used for tagging test cases
[setup]
[teardown]
[template]
[timeout] - set test case timeout

