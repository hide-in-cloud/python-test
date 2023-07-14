"""
    数据模型
"""


class DirectionModel:
    """
        方向数据模型
        枚举
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Location:
    """
        位置
    """
    def __init__(self, row, column):
        self.row_index = row
        self.column_index = column
