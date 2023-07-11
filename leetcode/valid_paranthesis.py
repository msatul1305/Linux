# trial 1
class Solution:
    def isValid(self, s: str) -> bool:
        new_str = []
        count = 0
        for i, x in enumerate(s):
            if x == '(' or x == '{' or x == '[':
                new_str.append(x)
                count += 1
            elif x == ')' or x == '}' or x == ']':
                if x == ')' and new_str[-1] == '(':
                    new_str[-1].remove("(")
                elif x == '}' and new_str[-1] == '{':
                    new_str[-1].remove("{")
                elif x == ']' and new_str[-1] == '[':
                    new_str[-1].remove("[")
        if len(new_str) == count and "(" not in new_str and "{" not in new_str and "(" not in new_str:
            return True
        else:
            return False

# s = "()"
# s = "()[]{}"
# s = "(]"
s = "{[]}"
k = Solution()
k.isValid(s)
