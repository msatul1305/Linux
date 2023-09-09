names = ['David IX', 'Mary L', 'Mary V', 'Mary XII', 'Mary XV', 'Mary XX', 'Steven XL', 'Steven XVI']

# Define a dictionary to convert Roman numerals to integers
roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50}

def roman_to_integer(roman_numeral):
    result = 0
    prev_value = 0
    for letter in roman_numeral:
        value = roman_values.get(letter, 0)
        if value > prev_value:
            result += value - 2 * prev_value  # Handle cases like IV, IX, etc.
        else:
            result += value
        prev_value = value
    return result

def custom_sort_key(name):
    # Split the name into two parts: name and Roman numeral
    parts = name.split()
    name_part = parts[0]
    roman_numeral = parts[1]

    # Calculate the integer value of the Roman numeral
    roman_value = roman_to_integer(roman_numeral)

    return (name_part, roman_value)


# Sort the names using the custom_sort_key with list.sort
names.sort(key=custom_sort_key)

print(names)
