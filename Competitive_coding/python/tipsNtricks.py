# take array as user input
inp = input().split()
arr = [int(num) for num in inp]
print(arr)

# # take list as integer input
# for i in range(int(input())):
#     a, b, c = map(int, input().split())

# take user input as hashmap/dict python for counting no. of occurance of each input
input_counts = {}
for item in arr:
    if item in input_counts:
        input_counts[item] += 1
    else:
        input_counts[item] = 1
print("Input counts:", input_counts)

# sort dictionary in python by value
my_dict = {"apple": 5, "banana": 3, "orange": 7, "grape": 2}
sorted_list = sorted(my_dict.items(), key=lambda x: x[1])
sorted_dict = dict(sorted_list)

# print the sorted dictionary
print("Sorted dictionary:", sorted_dict)

# print the last element of a dictionary in Python:
last_key = list(my_dict.keys())[-1]
last_value = my_dict[last_key]
