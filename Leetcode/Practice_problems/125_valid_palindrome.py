# A phrase is a palindrome if, after
# converting all uppercase letters into lowercase letters
# removing all non-alphanumeric characters
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
import re

from pandas.io.formats.format import return_docstring

s = "A man, a plan, a canal: Panama"
s = s.lower()
s = re.sub(r'[^a-zA-Z0-9]', '', s)
x = s[::-1]
print(s)
