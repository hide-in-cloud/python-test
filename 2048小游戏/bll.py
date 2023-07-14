"""
    2048核心算法
"""
from model import *
import random


class GameCoreController:
    def __init__(self):
        self.__list_merge = []
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end01(self):
        """
            把所有的零移到列表的末尾
        """
        # 简单暴力的算法
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __zero_to_end02(self):
        """
            把所有的零移到列表的末尾
        """
        # 性能更高的算法(还可改进)
        for i in range(len(self.__list_merge)):
            if self.__list_merge[i] == 0:
                for j in range(i + 1, len(self.__list_merge)):
                    if self.__list_merge[j] != 0:
                        self.__list_merge[i], self.__list_merge[j] = self.__list_merge[j], self.__list_merge[i]
                        break
                        # exchange = True

    def __merge(self):
        """
            合并
        """
        # 先将中间的零元素移到末尾
        # 再合并相邻且相同的元素
        self.__zero_to_end01()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
            向左移动
        """
        # 将二维数组的每一行交给merge函数进行操作
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            向右移动
        """
        # 将二维数组的每一行(从右往左)交给merge函数进行操作
        for line in self.__map:
            # 从右往左取出数据形成新的数组
            self.__list_merge = line[::-1]
            self.__merge()
            # 从右往左接收合并后的数据
            line[::-1] = self.__list_merge

    def __square_matrix_transpose(self):
        """
            方阵转置
        """
        for i in range(1, len(self.__map)):
            for j in range(i):
                self.__map[i][j], self.__map[j][i] = self.__map[j][i], self.__map[i][j]

    def __move_up(self):
        """
            向上移动
        """
        # 先把方阵转置
        self.__square_matrix_transpose()
        # 将方阵进行向左操作
        self.__move_left()
        # 再把方阵转置回来
        self.__square_matrix_transpose()

    def __move_down(self):
        """
            向下移动
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def move(self, dir):
        """
            移动
        :param dir: 方向，DirectionModel类型
        :return:
        """
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    def generate_new_number(self):
        """
            在空白位置随机生成一个数(2或4)
        :return:
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.row_index][loc.column_index] = 2 if random.randint(1, 10) != 10 else 4
        # 移除生成新数字的位置
        self.__list_empty_location.remove(loc)

    def __get_empty_location(self):
        """
            获取空白位置
        :return:
        """
        # 每次统计空位置前，先清空之前的数据
        self.__list_empty_location.clear()
        for row in range(len(self.__map)):
            for column in range(len(self.__map[row])):
                if self.__map[row][column] == 0:
                    self.__list_empty_location.append(Location(row, column))

    def is_game_over(self):
        """
            游戏是否结束
        :return: False表示没有结束，True表示游戏结束
        """
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == self.__map[r][c+1] or self.__map[c][r] == self.__map[c][r+1]:
                    return False
        return True


# ---------测试代码-------------
if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    player1 = GameCoreController()
    player1.generate_new_number()
    player1.generate_new_number()
    player1.generate_new_number()

    # list_zeros = []
    # for i in range(len(map)):
    #     for j in range(len(map[i])):
    #         if map[i][j] == 0:
    #             list_zeros.append((i, j))
    # loc = random.choice(list_zeros)
    # print(loc)
