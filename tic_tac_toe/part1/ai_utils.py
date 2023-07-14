import random
from tic_tac_toe.part1.game_functions import get_all_line_coords


def moves_ai(board):
    # 后手: 中心 > 角落 > 与对手相邻
    if board[1][1] is None:
        move_coords = (1, 1)
    else:
        none_coords = get_corners_none_coords(board)
        if none_coords[0] is None:
            none_coords = get_all_none_coords(board)
        move_coords = random.choice(none_coords)
    return move_coords


def get_corners_none_coords(board):
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    none_list = []
    for (x, y) in corners:
        if board[x][y] is None:
            none_list.append((x, y))
    return none_list


def get_all_none_coords(board):
    all_none_coords = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] is None:
                all_none_coords.append((x, y))
    return all_none_coords


def finds_winning_moves_ai(board, current_player):
    """
    :param board:
    :param current_player:
    :return: 获胜点的坐标
    """
    all_line_coords = get_all_line_coords()
    for line in all_line_coords:
        # line = [(),(),()]
        # line_values = ['','','']
        line_values = [board[x][y] for (x, y) in line]
        # 直线上有两个current_player, 且有一个位置为none
        if line_values.count(current_player) == 2 and None in line_values:
            for (x, y) in line:
                if board[x][y] is None:
                    return x, y