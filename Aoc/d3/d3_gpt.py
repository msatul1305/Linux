def is_part_number(grid, row, col):
    # Check if the position contains a number adjacent to a symbol
    symbols = ['*', '#', '+', '$', '&', '%', '=', '-', '/']  # Symbols to check for adjacency

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i != row or j != col) and 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j].isdigit() and any(grid[i][j] == sym for sym in symbols):
                    return True
    return False


def sum_part_numbers(engine_schematic):
    total_sum = 0

    for r in range(len(engine_schematic)):
        for c in range(len(engine_schematic[0])):
            if engine_schematic[r][c].isdigit() and is_part_number(engine_schematic, r, c):
                total_sum += int(engine_schematic[r][c])

    return total_sum

# Example engine schematic
schematic = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

result = sum_part_numbers(schematic)
print("Sum of all part numbers:", result)
