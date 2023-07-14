import copy
import time
from life_game.utils import *
import matplotlib.pyplot as plt
from matplotlib import animation

NUM = 0


class GameOfLife:
    """生命游戏类"""
    def __init__(self, width=70, height=20):
        self.width = width
        self.height = height

    def dead_state(self):
        """死亡状态"""
        dead_board = []
        for w in range(self.height):
            row = []
            for h in range(self.width):
                row.append(0)
            dead_board.append(row)
        return dead_board

    def random_state(self):
        board_state = self.dead_state()
        for x in range(self.height):
            for y in range(self.width):
                cell_state = random_alive()
                board_state[x][y] = cell_state
        return board_state

    def render(self, board_state):
        """画出生命图"""
        print("-" * (self.width + 2))
        for x in range(self.height):
            output = ''
            for y in range(self.width):
                if board_state[x][y] == 1:
                    output += 'O'
                else:
                    output += ' '
            print("|%s|" % output)
        print("-" * (self.width + 2))

    def count_neighbors(self, initial_state, row, col):
        """
            计算邻居的活细胞总数
        :param initial_state: 初始细胞状态表
        :param row: 当前细胞的行数
        :param col: 当前细胞的列数
        :return: 邻居的活细胞总数
        """
        up = row - 1
        down = (row + 1) % self.height
        left = col - 1
        right = (col + 1) % self.width
        total_alive = initial_state[up][left] + initial_state[up][col] + initial_state[up][right] + \
                      initial_state[row][left] + initial_state[row][right] + \
                      initial_state[down][left] + initial_state[down][col] + initial_state[down][right]
        return total_alive

    def next_board_state(self, initial_state):
        new_board = copy.deepcopy(initial_state)
        for x in range(self.height):
            for y in range(self.width):
                total_alive = self.count_neighbors(initial_state, x, y)
                if initial_state[x][y] == 1:
                    if total_alive < 2 or total_alive > 3:
                        new_board[x][y] = 0
                else:
                    if total_alive == 3:
                        new_board[x][y] = 1
        initial_state = new_board
        return initial_state


def generator(frame_num, img, plt, initial_state):
    life = GameOfLife()
    global NUM
    NUM += 1
    plt.title(f"{NUM} board_state")
    height = len(initial_state)
    width = len(initial_state[0])
    new_board = copy.deepcopy(initial_state)
    for x in range(height):
        for y in range(width):
            total_alive = life.count_neighbors(initial_state, x, y)
            if initial_state[x][y] == 1:
                if total_alive < 2 or total_alive > 3:
                    new_board[x][y] = 0
            else:
                if total_alive == 3:
                    new_board[x][y] = 1
    img.set_data(new_board)
    initial_state = new_board
    return img


def update(initial_state, save_name):
    update_interval = 50
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    img = ax.imshow(initial_state, cmap='autumn', interpolation='nearest')
    ani = animation.FuncAnimation(fig, generator, fargs=(img, plt, initial_state),
                                  frames=20, interval=update_interval, save_count=50)
    if save_name:
        ani.save(save_name, fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()


def main():
    # board_state = game.random_state()
    # board_state = load_board_state('toad.txt')
    # board_state = load_board_state('Beacon.txt')
    # board_state = load_board_state('Blinker.txt')
    # board_state = load_board_state('Glider.txt')
    board_state = load_board_state('Gosper_Glider_Gun.txt')
    width = len(board_state[0])
    height = len(board_state)
    game = GameOfLife(width, height)
    while True:
        print('\n' * 50)
        game.render(board_state)
        board_state = game.next_board_state(board_state)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
