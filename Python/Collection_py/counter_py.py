# Tally occurrences of words in a list
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
words = re.findall(r'\w+', open('atul.txt').read().lower())
print(Counter(words).most_common(10))

# elements
c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))
