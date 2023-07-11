- most commonly used built-in modules in Python?
  - os 
  - math
  - sys 
  - random 
  - re 
  - datetime 
  - JSON
  - log
- generate random numbers
  -  import random
     print(random.random())
- randrange(beginning, end, step)
  - import random
    print(random.randrange(5,100,2))
- check if all characters in the given string is alphanumeric
  - "abdc1321".isalnum() #Output: True
    "xyz@123$".isalnum() #Output: False
  - import re
    print(bool(re.match('[A-Za-z0-9]+$','abdc1321'))) # Output: True
    print(bool(re.match('[A-Za-z0-9]+$','xyz@123$'))) # Output: False
- Define GIL.
  - GIL stands for Global Interpreter Lock. 
  - This is a mutex used for limiting access to python objects 
  - and aids in effective thread synchronization by avoiding deadlocks.
  - GIL helps in achieving multitasking (and not parallel computing)
- PIP: Python Installer Package.
  - pip install <package_name>
- tools for identifying bugs and performing static analysis in python?
  - PyChecker and Pylint which are used as static analysis and linting tools respectively.
  - PyChecker helps find bugs in python source code files and 
  - raises alert for code issues and their complexity. 
  - Pylint checks for the module’s coding standards and supports different plugins 
  - to enable custom features to meet this requirement.
- deep and shallow copies.
  - Shallow copy does the task of creating new objects storing references of original elements. 
  - This does not undergo recursion to create copies of nested objects. 
  - It just copies the reference details of nested objects.
  - Deep copy creates an independent and new copy of an object and 
  - even copies all the nested objects of the original element recursively.
- main function in python
  - def main():
    print("Hi Interviewbit!")
    if __name__=="__main__":
    main()
- 