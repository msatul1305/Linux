class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        print(rev)
        subs_list = []
        k = 0
        for i in range(len(s)-1):
            x = s[k] + s[k+1]
            k = k + 1
            subs_list.append(x)
        print(subs_list)
        for m in subs_list:
            if m in rev:
                return True
        return False
        # ans = True
        # return ans


str = "hello"
print(str)
obj = Solution()
print(obj.isSubstringPresent(str))
