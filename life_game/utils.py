import random


def load_board_state(filename):
    """根据文件输入状态加载生命游戏"""
    board_state = []
    with open(filename, 'r') as f:
        row = list(map(int, f.readline().strip()))
        while row:
            board_state.append(row)
            row = list(map(int, f.readline().strip()))
    return board_state


def random_alive():
    """随机存活"""
    random_number = random.random()  # [0,1)
    if random_number >= 0.5:  # 存活的几率为50%
        cell_state = 0
    else:
        cell_state = 1
    return cell_state
