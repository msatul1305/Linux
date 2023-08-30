def lengthOfLastWord(s: str) -> int:
    i = -1
    while s.split(" ")[i] == "":
        i = i - 1
    return len(s.split(" ")[i])


s = "hello world   "
lengthOfLastWord(s)
