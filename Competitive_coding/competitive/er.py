def winner(erica, bob):
    d = {'E': 1, 'M': 3, 'H': 5}
    op1 = sum([d[char] for char in erica])
    op2 = sum([d[char] for char in bob])
    print(op1)
    print(op2)
    if op1 == op2:
        return "Tie"
    elif op1>op2:
        return "Erica"
    else:
        return "Bob"


er = "E"
bob = "H"
print(winner(er, bob))
