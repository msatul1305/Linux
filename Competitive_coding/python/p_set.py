my_set = set()
my_set.add(5)
my_set.add(6)
if 5 in my_set:
    my_set.remove(5)
other_set = {4, 5, 6}
union_set = my_set.union(other_set)
intersection_set = my_set.intersection(other_set)
difference_set = other_set.difference(my_set)
print(difference_set)
