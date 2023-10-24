- history
  - Named after the Monty Python comedy troupe
  - hobby project created by Guido van Rossum and first released in 1991
    - in the late 1980s while working at the Centrum Wiskunde & Informatica (CWI) in the Netherlands.
    - language that was easy to read and write, with a clear and straightforward syntax.
    - 
- most commonly used built-in modules in Python
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
- swapcase function in Python?
  - string = "GeeksforGeeks"
    string.swapcase() ---> "gEEKSFORgEEKS"
- floor a number in Python?
  - floor(x) method: largest integer not greater than x. 
  - ceil(x): smallest integer greater than or equal to x.
- difference between a shallow copy and a deep copy?
  - Shallow copy is used when a new instance type gets created and 
  - it keeps values that are copied whereas deep copy stores values that are already copied. 
  - A shallow copy has faster program execution whereas a deep copy makes it slow.
- sorting technique is used by sort() and sorted() functions of python
  - Python uses the [Tim Sort](https://www.geeksforgeeks.org/timsort/) algorithm for sorting. 
  - It’s a stable sorting whose worst case is O(N log N). 
  - It’s a hybrid sorting algorithm, derived from merge sort and insertion sort,
  - designed to perform well on many kinds of real-world data.
  - sort() vs sorted()
    - sort() sorts the current list
    - syntax:
      - list.sort()
    - sorted returns a new list with sorted items
      - syntax:
        - new_list = sorted(list)
- Important methods
  - [sort](sort_py.py):  
  - [sorted](sorted_py.py)
  - [zip](zip_func.py)


- Others
  - * vs ** in function call: https://stackoverflow.com/questions/2921847/what-do-double-star-asterisk-and-star-asterisk-mean-in-a-function-call
  - zip vs zip*: https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist#:~:text=zip%20wants%20a%20bunch%20of,%2C5%2C6%5D%5D%20)%20.
