# https://github.com/robotframework/robotframework/blob/master/atest/testdata/standard_libraries/collections/dictionary.robot
*** Settings ***
Library    Collections

*** Test Cases ***
#Run Keyword If    $var_in_py_expr1 == $var_in_py_expr2
#...    Keyword    @args
#...  ELSE IF    condition_in_py_expr
#...    Keyword    @args
#...  ELSE
#...    Keyword    @args

Iterate over keys
    Dictionary Should Not Contain Key   ${DICT}  a

IF COndition check
    IF    $var_in_py_expr1 == $var_in_py_expr2
         bla bla bla
    END
    
    IF    $var_in_py_expr1 == $var_in_py_expr2
        Call Keyword
    ELSE
         
    END
