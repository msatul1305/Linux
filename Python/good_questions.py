# Program to add two integers >0 without using the plus operator.
def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1
print(add_nums(2, 10))

# Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s.
import re
def match_text(txt_data):
    pattern = 'ab{4,8}'
    if re.search(pattern,  txt_data):    #search for pattern in txt_data
        return 'Match found'
    else:
        return('Match not found')
print(match_text("abc"))         #prints Match not found
print(match_text("aabbbbbc"))    #prints Match found

# Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.
from datetime import datetime
new_date = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d:%m:%Y")
print(new_date)
