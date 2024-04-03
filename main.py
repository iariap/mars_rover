def get_position(matrix_size: int, cmds: list[str]) -> int:
    position = 0
    for cmd in cmds:
        if cmd == "UP" and position > matrix_size - 1:
            position -= matrix_size
        elif cmd == "DOWN" and position < matrix_size * matrix_size - matrix_size:
            position += matrix_size
        elif cmd == "LEFT" and position % matrix_size != 0:
            position -= 1
        elif cmd == "RIGHT" and position % matrix_size != matrix_size - 1:
            position += 1

    return position


"""
    0   1   2   3
    4   5   6   7
    8   9   10  11
    12  13  14  15
"""

cmds = ["RIGHT", "UP", "DOWN", "LEFT", "DOWN", "DOWN"]
position = get_position(4, cmds)
assert position == 12
