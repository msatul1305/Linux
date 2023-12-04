def is_valid_coord(x, y, size):
    return 0 <= x < size and 0 <= y < size

def sum_part_numbers(engine_schematic):
    size = len(engine_schematic)
    symbols = ['*', '#', '+', '$']
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    part_numbers = set()

    for i in range(size):
        for j in range(size):
            if engine_schematic[i][j] in symbols:
                for k in range(8):
                    x, y = i + dx[k], j + dy[k]
                    if is_valid_coord(x, y, size) and engine_schematic[x][y].isdigit():
                        part_numbers.add(int(engine_schematic[x][y]))

    return sum(part_numbers)

engine_schematic_10x10 = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

result_10x10 = sum_part_numbers(engine_schematic_10x10)
print("Sum of all part numbers in the 10x10 engine schematic:", result_10x10)
