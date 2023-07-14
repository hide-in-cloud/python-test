"""
    井字棋
"""
BOARD_WIDTH = 3
BOARD_HEIGHT = 3


def new_board():
    """
    :return: 返回一个空的3x3网格
    """
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]


def render(board):
    print("  ", end="")
    for column in range(BOARD_WIDTH):
        print(column+1, end=" ")
    print()
    print(" -------")
    for row in range(BOARD_HEIGHT):
        output_row = ""
        for column in range(BOARD_WIDTH):
            if board[row][column] is None:
                output_row += " "
            else:
                output_row += board[row][column]
        print("%d|%s|" % (row+1, " ".join(output_row)))
    print(" -------")


def get_move():
    x = int(input("X co-ordinate (1-3):"))
    y = int(input("Y co-ordinate (1-3):"))
    return x-1, y-1


def execute_move(board, co_ords, player):
    row = co_ords[0]
    column = co_ords[1]
    board[row][column] = player


def is_valid_move(board, co_ords):
    if board[co_ords[0]][co_ords[1]] is None:
        return True
    else:
        return False


def is_game_over(board, current_player):
    all_line_coords = get_all_line_coords()
    for line in all_line_coords:
        line_values = [board[x][y] for (x, y) in line]
        if line_values.count(current_player) == 3:
            return True
    return False


def get_all_line_coords():
    rows = []
    for x in range(BOARD_WIDTH):
        row = []
        for y in range(BOARD_HEIGHT):
            row.append((x, y))
        rows.append(row)

    cols = []
    for y in range(BOARD_WIDTH):
        col = []
        for x in range(BOARD_HEIGHT):
            col.append((x, y))
        cols.append(col)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return rows + cols + diagonals


def is_board_full(board):
    for row in board:
        for col in row:
            if col is None:
                return False
    return True


