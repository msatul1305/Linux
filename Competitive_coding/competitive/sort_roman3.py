def conv_to_int(s):
    d = {
        'I':  1,
        'V': 5,
        'X': 10,
        'L': 50
    }
    ans = 0
    prev = d['I']
    for x in s[::-1]:
        curr = d[x]
        if curr < prev:
            ans = ans - curr
        else:
            ans = ans + curr
        prev = curr
    return ans


def custom_sort_key(name):
    name_part = name.split()[0]
    roman_part = name.split()[1]
    int_val = conv_to_int(roman_part)
    return name_part, int_val


def sortRoman(names):
    sorted_names = sorted(names, key=custom_sort_key)
    return sorted_names


names = ['David IX', 'Mary L', 'Mary V', 'Mary XII', 'Mary XV', 'Mary XX', 'Steven XL', 'Steven XVI']
print(sortRoman(names))
