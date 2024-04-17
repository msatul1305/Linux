class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        subs_list = []
        k = 0
        result = []
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                result.append(s[start:end])
        print(result)
        rev_res = []
        for m in result:
            rev_res.append(m[::-1])
        for x in range(len(result)):
            if result[x][0] == c and rev_res[x][0] == c:
                count = count + 1
        print(rev_res)
        return count


s = "hello"
c = "l"
count = 0
for x in s:
    if x == c:
        count = count + 1
print(f'count={count}')
z = count*(count+1)/2
print(int(z))
obj = Solution()
print(obj.countSubstrings(s, c))


# 1->1
# 2->3
# 3->6
# 4->10
# 5->15
