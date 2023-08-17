# Custom class CompRes
class CompRes:
    def __init__(self, diff, t):
        self.diff = diff
        self.t = t

# Given list of CompRes instances
comp = [
    CompRes(diff={'Acc': ('expected1', 'actual1')}, t=False),
    CompRes(diff={'xyz': ('expected2', 'actual2')}, t=False),
]

# Create a new dictionary from the "diff" field
new_dict = {tuple_obj[0]: tuple_obj[1] for item in comp for tuple_obj in item.diff.values()}

print("New dictionary from 'diff':", new_dict)
