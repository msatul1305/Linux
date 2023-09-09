def roman_to_integer(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    result = 0
    prev_value = 0
    for letter in roman_numeral:
        value = roman_values.get(letter, 0)
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
    return result


def custom_sort_key(name):
    parts = name.split()
    name_part = parts[0]
    roman_numeral = parts[1]

    roman_value = roman_to_integer(roman_numeral)

    return name_part, roman_value


def sortRoman(names):
    sorted_names = sorted(names, key=custom_sort_key)
    return sorted_names


names = ['David IX', 'Mary L', 'Mary V', 'Mary XII', 'Mary XV', 'Mary XX', 'Steven XL', 'Steven XVI']
print(sortRoman(names))
