# TLE: still bruteforce
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        subs_list = []
        k = 0
        result = []
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                curr = s[start:end]
                if curr[0] == curr[-1] == c:
                    count = count + 1
        return count


s = "hello"
c = "l"
obj = Solution()
print(obj.countSubstrings(s, c))
