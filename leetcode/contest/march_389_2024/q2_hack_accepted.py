# TLE: still bruteforce
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        for x in s:
            if x == c:
                count = count + 1
        z = int(count*(count+1)/2)
        return z


s = "zzz"
c = "z"
obj = Solution()
print(obj.countSubstrings(s, c))
