- Question:
- find a in b:
-     a = "xyz"
-     b = "abcxyzabc"
-     output = 3
-     if not found, o/p = -1
- Naive/Bruteforce Approach: Iterate through 'b' char by char, match if same as in 'a'
- if not same, move one step ahead(slide) in 'b' and check again
- Time complexity: O(n*m) for the worst case
- Issue example:
- b = aacaadaabaak
- a = aab
- eg. 2
  - b = aaaaaaaaab
  - a = aaab
- here everytime we need to start again with second 'a' and recheck again, but we know this is not the answer
- so, we can use prefix matching to move to next word instead.[KMP_ALGO](101_KMP_Algo_String_Matching_self_working.py)
  - this will have O(M+N) complexity
- Otherwise, we can make a hash map of each character with a = 1, b = 2 (or ASCII) etc... [Rabin_Karp_Algo](100_Rabin_Karp_Algo_String_Matching.py)
  - and then, find the sum of characters in 'a' and match that with characters in 'b'
  - To remove cases like aac = 5 and abb = 5 and also cases like 'pi' and 'ip', we can use power for each character
  - e.g. if a = 'aad'
    - then the sum = 1*10^2 + 1*10^1 + 4*10^0 = 114