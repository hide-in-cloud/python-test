"""
    列表助手模块
"""


class ListHelper(object):
    """
        列表助手类
    """
    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找列表中符合某个条件的所有元素的方法
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件，函数类型
                格式：函数名(参数1) --> bool
        :return:需要查找的元素，生成器类型
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def search(list_target, func_condition):
        """
            通用的查找列表中符合某个条件的单个元素的方法
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件，函数类型
                格式：函数名(参数1) --> bool
        :return:需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target, func_condition):
        """
            通用的计算列表中符合某个条件的所有元素的个数
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件，函数类型
                格式：函数名(参数1) --> bool
        :return:需要计算的元素数量
        """
        count = 0
        for item in list_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def is_exist(list_target, func_condition):
        """
            通用的判断列表中符合某个条件的元素是否存在
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型
                格式：函数名(参数1) --> bool
        :return: True or False
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum(list_target, func_handle):
        """
            通用的计算列表中某个元素的总和
        :param list_target: 需要求和的列表
        :param func_handle: 需要求和的处理逻辑，函数类型
                格式：函数名(参数1) --> 值
        :return: 和值
        """
        sum_value = 0
        for item in list_target:
            sum_value += func_handle(item)
        return sum_value

    @staticmethod
    def mapped(list_target, func_handle):
        """
            通用的映射（筛选）方法
        :param list_target: 需要映射的列表
        :param func_handle: 需要映射的处理逻辑，函数类型
                格式：函数名(参数1) --> int/float/str...
        :return: 生成器
        """
        for item in list_target:
            yield func_handle(item)

    @staticmethod
    def get_max(list_target, func_handle):
        """
            通用的获取列表中的最大值
        :param list_target: 目标列表
        :param func_handle: 需要搜索的处理逻辑，函数类型
                格式：函数名(参数1) --> 需要获取的对象
        :return: 最大值
        """
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_handle(list_target[i]) > func_handle(max_value):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def order_by(list_target, func_handle):
        """
            通用的升序排列方法
        :param list_target: 目标列表
        :param func_handle: 排序的逻辑，函数类型
                格式：函数名(参数1) --> 需要比较的数据值
        :return:
        """
        for i in range(len(list_target)):
            for j in range(i + 1, len(list_target)):
                if func_handle(list_target[j]) < func_handle(list_target[i]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def square_matrix_transpose(sqr_matrix):
        """
            方阵转置
        :param sqr_matrix:二维列表的方阵
        """
        for i in range(1, len(sqr_matrix)):
            for j in range(i):
                sqr_matrix[i][j], sqr_matrix[j][i] = sqr_matrix[j][i], sqr_matrix[i][j]
