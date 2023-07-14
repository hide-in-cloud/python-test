from tic_tac_toe.patr2.minimax_ai import *

BOARD_WIDTH = 3
BOARD_HEIGHT = 3


def create_new_board():
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
    x = int(input("X co-ordinate:"))
    y = int(input("Y co-ordinate:"))
    return x+1, y+1


def is_valid_move(board, co_ords):
    if board[co_ords[0]][co_ords[1]] is None:
        return True
    else:
        return False


def execute_move(board, co_ords, player):
    row = co_ords[0]
    column = co_ords[1]
    board[row][column] = player


def get_winner(board):
    all_line_coords = get_all_line_coords()
    for line in all_line_coords:
        line_values = [board[x][y] for (x, y) in line]
        if line_values[0] is not None and line_values.count(line_values[0]) == 3:
            return line_values[0]
    return None


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


def play():
    board = create_new_board()
    players = ['X', 'O']
    turn_number = 0
    while True:
        render(board)
        current_player = players[turn_number % len(players)]
        print('It is %s turn' % current_player)

        if current_player == 'X':
            move_coords = minimax_ai(board, current_player)
        else:
            while True:
                move_coords = get_move()
                if is_valid_move(board, move_coords):
                    break
                else:
                    print("Illegal move, try again!")

        execute_move(board, move_coords, current_player)

        winner = get_winner(board)
        if winner is not None:
            render(board)
            print("GAME OVER!")
            print("The winner is %s" % current_player)
            break
        if is_board_full(board):
            render(board)
            print("It is a DRAW!")
            break
        turn_number += 1
