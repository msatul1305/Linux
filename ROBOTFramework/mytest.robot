*** Settings ***
Library    Collections
*** Variables ***
&{DICT}          a=1    b=2    c=3

*** Test Cases ***
Dictionary iteration with FOR loop
    FOR    ${key}    ${value}    IN    &{DICT}
        Log    Key is '${key}' and value is '${value}'.
    END

Dictionary iteration with FOR-IN-ENUMERATE loop
    FOR    ${index}    ${key}    ${value}    IN ENUMERATE    &{DICT}
        Log    On round ${index} key is '${key}' and value is '${value}'.
    END

Multiple dictionaries and extra items in 'key=value' syntax
    &{more} =    Create Dictionary    e=5    f=6
    FOR    ${key}    ${value}    IN    &{DICT}    d=4    &{more}    g=7
        Log    Key is '${key}' and value is '${value}'.

One loop variable
    FOR    ${item}    IN    &{DICT}
        Log    Key is '${item}[0]' and value is '${item}[1]'.
    END

One loop variable with FOR-IN-ENUMERATE
    FOR    ${item}    IN ENUMERATE    &{DICT}
        Log    On round ${item}[0] key is '${item}[1]' and value is '${item}[2]'.
    END

Two loop variables with FOR-IN-ENUMERATE
    FOR    ${index}    ${item}    IN ENUMERATE    &{DICT}
        Log    On round ${index} key is '${item}[0]' and value is '${item}[1]'.
    END


Iterate over keys2
    IF    ${key}    IN    @{DICT}
        Log    Key is '${key}' and value is '${DICT}[${key}]'.
    END
