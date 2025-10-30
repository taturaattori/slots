def flip_horizontal(result):
    # Flip results horizontally to make the more readable
    horizontal_values = []

    for value in result.values():
        horizontal_values.append(value)

    rows, cols = len(horizontal_values), len(horizontal_values[0])
    hvals2 = [[""] * rows for _ in range(cols)]

    for x in range(rows):
        for y in range(cols):
            hvals2[y][rows - x - 1] = horizontal_values[x][y]
    
    hvals3 = [item[::-1] for item in hvals2]
    return hvals3
