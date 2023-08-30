def plusOne(digits):
    carry = 0
    addition = 1
    l = len(digits) - 1
    # if l == 0 and digits[l] == 9:
    #     return [1,0]
    while l >= 0:
        if digits[l] + carry + addition <= 9:
            digits[l] = digits[l] + 1
            carry = 0
        else:
            digits[l] = 0
            carry = 1
        if carry == 0:
            return digits
        addition = 0
        l = l - 1
    if carry == 1:
        digits.insert(0, 1)
    return digits


arr = [8, 9, 9, 9]
print(plusOne(arr))
