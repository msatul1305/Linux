***Robot Framework***
Edureka -> https://www.youtube.com/watch?v=d-KWz7euLlc
- Generic open source automation framework for:
1. ***Acceptance Testing*** - To test the capability of a system. -> Normally done by users.
2. ***ATTD - Acceptance Test driven development*** - Development methodology based on communication between business, customers, developers and testers - creating of acceptance tests before development of actual functionality
3. ***RPA - Robotic Process Automation*** -> Reducing human efforts for machines that uses ML and AI. Handles high level repeatable tasks.

-> Uses ***Keyword driven testing*** approach.


***Architecture***
When Robot Framework is started, it processes the data, executes the test cases and generates logs and reports.

***Standard Libraries***
1. ***Builtin libraries***: eg.Should be equal, should contain, convert to integer, Logs, run, leap keyword, set variable.
2. ***Collections***: eg. pen to list, get from dictionary, list should be equal, dictionary should be contained value.
3. ***DateTime***: eg. get current date, convert time, subtract time from date, add time from time
4. ***Dialogs***: used for Pausing the test execution and getting input from users
5. ***OperatingSystem***: run, create and remove directories, files should exist, directory should be empty, set environment variable. 
6. ***Process***: popen class, run processes in a system, wait for process completion, start process, wait for process, terminate process, terminate all processes.
7. ***Remote***: 
8. ***Screenshot***: take ss
9. ***String***: replace string using regX, split 2 lines, should be string
10. ***telnet***: telnet connections
11. XML framework
12. ***Selenium Library***
13. ***Db library***

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

***Keywords***
1. Library keywords: pre defined keywords in languages like python, Java etc.
2. User keywords: Custom high level keywords craeted by users

eg. of library settings importing:
```
*** Settings ***
Library  OperatingSystem
Library  lib/LoginLibrary.py
```

```
*** Keywords ***
Clear login database
  Remove file  ${DATABASE FILE}
  
Create valid user
  [Arguments]  ${username}  ${password}
  Create user ${username}  ${password}
  Status should be  SUCCESS

Creating user with invalid password should fail
  [Arguments]  ${password}  ${error}
  Create user  example  {password}
  Status should be  Creating user failed: ${error}
  
Login
  [Arguments]  ${username}  ${password}
  Attempt to login with credentials  ${username}  ${password}
  Status should be  Logged In
  
A user has a valid account
  Create  valid user  {USERNAME}  {PASSWORD}

She changes her password
  Change Password  {USERNAME}  {PASSWORD}  {NEW PASSWORD}
  Status should be   SUCCESS
  
She can login with the new password
  LOGIN  {USERNAME}  {NEW PASSWORD}
  
She cannot use the old password anymore
  Attempt to login with credentials  {USERNAME}  {PASSWORD}
  Status should be  Access Denied
 
```

***Defining Variables***
```
*** Variables ***
${USERNAME}  janedoe
${PASSWORD}  JANEDOE
${NEW PASSWORD}  JANEDOE1
${DATABASE FILE}  ${TEMPDIR}${/}robotframework-quickstart-db.txt
${PWD INVALID LENGTH}  Password must be 7-12 characters long 
```

***Using Variables***
```
*** Test Cases ***
User status is stored in database
  [Tags]  variables  database
  Create Valid User  {USERNAME}  {PASSWORD}
  Database should contain  {USERNAME}  {PASSWORD}  Inactive
  Login  {USERNAME}  {PASSWORD}
  Database should contain  {USERNAME}  {PASSWORD} Active
  
*** Keywords ***
Database should contain
  [Arguments]  ${username}  {password}  ${status}
  ${database} =  Get File  ${DATABASE FILE}
  Should Contain   ${database}  ${username}t{password}t${status}n
```
  
*** Organizing Test Cases ***

```
*** Settings ***
Suite Setup  Clear Login Database
Test Teardown  Clear Login Database

*** Settings ***
Force.Tags  quickstart
Default tags  example  smoke
```
  
  
***Robot Framework Selenium Library***
- pip install webdrivermanager - to manage web browsers

```
*** Setings ***
Documentation  Simple example using Selenium Library.
Library  SeleniumLibrary

*** Variables ***
${LOGIN URL}  <a href="http://localhost:7272">http://localhost:7272</a>
${BROWSER}  Chrome

*** Test Cases ***
Valid Login
  Open Browser to Login Page
  Input Username  demo
  Input Password  mode
  Submit Credentials
  Welcome Page Should Be Open
  [Teardown]  Close Browser
  
*** Keywords ***
Open Browser to Login Page
  Open Browser  ${LOGIN URL}  ${BROWSER}
  Title Should be  Login Page
  
Input Username
  [Arguments]  ${username}
  Input Text  username_field  ${username}
  
Input Password
  [Arguments]  ${password}
  Input Text  password_field  ${password}

Submit Credentials
  Click Button  login_button
  
Welcome Page Should Be Open
  Title Should Be  Welcome Page
```




Working Examples:
1. 
*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Login Test
        Open Browser  https://www.facebook.com  Firefox
        Input Text  name:email  demo
        Input Text  name:pass  demo
        Click Element  name:login
        Close Browser

Login Test2
        Open Browser  https://www.facebook.com  Firefox
        Input Text  id:email  demo
        Input Text  id:pass  demo
        Click Element  name:login
        Close Browser
